#!/usr/bin/env python3
"""Update the progress views from LOG.md and curriculum/*.md.

Writes:
  progress.svg        panel shown at the top of the README
  curriculum/*.md     a status mark in front of every topic

Usage: python3 tools/progress.py [--today YYYY-MM-DD]
"""
import datetime as dt
import html
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
TZ_NOTE = "Europe/Amsterdam"
WEEK_1_MONDAY = dt.date(2026, 10, 12)
INTERVALS = [7, 30, 90, 180]  # days until the next recall, by recalls passed so far

TRACKS = [
    # id, file, light colour, dark colour (categorical slots 1-4, validated)
    ("NUM", "NUM.md", "#2a78d6", "#3987e5"),
    ("CTRL", "CTRL.md", "#eb6834", "#d95926"),
    ("FT", "FT.md", "#1baf7a", "#199e70"),
    ("DSA", "DSA.md", "#eda100", "#c98500"),
]
MARKS = {"mastered": "✅", "retry": "🔁", "open": "🟡", "todo": "⬜"}
LEGEND = "Status: ✅ mastered · 🔁 not mastered yet · 🟡 posted, waiting for your solution · ⬜ not started"
ID_RE = re.compile(r"[A-Z]+-\d+\.\d+")
TOPIC_LINE = re.compile(r"^- (?:(?:✅|🔁|🟡|⬜) )?\*\*([A-Z]+-\d+\.\d+)\*\*\s*(.*)$")
RECALL_RE = re.compile(r"([A-Z]+-\d+\.\d+)\s*#(\d+)\s*([✓✗])?")


def parse_curriculum():
    tracks = []
    for tid, fname, light, dark in TRACKS:
        path = REPO / "curriculum" / fname
        text = path.read_text(encoding="utf-8")
        title = re.search(r"^# \S+ — (.+?)(?: \(.*\))?$", text, re.M)
        topics = []
        for line in text.splitlines():
            m = TOPIC_LINE.match(line)
            if m:
                name = re.sub(r"\s*\*\(.*?\)\*\s*$", "", m.group(2)).replace("`", "").strip()
                topics.append((m.group(1), name))
        tracks.append({"id": tid, "file": path, "name": title.group(1) if title else tid,
                       "light": light, "dark": dark, "topics": topics})
    return tracks


def parse_log():
    rows = []
    for line in (REPO / "LOG.md").read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*\d{4}-\d{2}-\d{2}", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        cells += [""] * (8 - len(cells))
        date = dt.date.fromisoformat(cells[0])
        status = cells[6].lower()
        verdict = status.split(":", 1)[1].strip() if status.startswith("checked") else None
        recalls = [(m.group(1), int(m.group(2)), m.group(3)) for m in RECALL_RE.finditer(cells[7])]
        rows.append({"date": date, "track": cells[2].upper(), "topics": ID_RE.findall(cells[4]),
                     "status": status, "verdict": verdict, "recalls": recalls})
    return rows


def topic_states(rows):
    state, mastered_on, last_checked, n_checked = {}, {}, {}, {}
    for r in rows:
        if r["track"] == "REVIEW":
            continue
        for t in r["topics"]:
            if r["verdict"] == "correct":
                state[t] = "mastered"
                mastered_on[t] = min(mastered_on.get(t, r["date"]), r["date"])
            elif r["verdict"]:
                if state.get(t) != "mastered":
                    state[t] = "retry"
                last_checked[t] = r["date"]
                n_checked[t] = n_checked.get(t, 0) + 1
            elif state.get(t) not in ("mastered", "retry"):
                state[t] = "open"
    return state, mastered_on, last_checked, n_checked


def recall_stats(rows, state, mastered_on, last_checked, n_checked, today):
    events = {}
    passed = failed = 0
    for r in rows:
        for t, _, mark in r["recalls"]:
            if mark:
                events.setdefault(t, []).append((r["date"], mark))
                passed += mark == "✓"
                failed += mark == "✗"
    due = 0
    for t, s in state.items():
        ev = sorted(events.get(t, []))
        if s == "mastered":
            ok = [d for d, m in ev if m == "✓"]
            last_ok = max([mastered_on[t]] + ok)
            bad_after = [d for d, m in ev if m == "✗" and d >= last_ok]
            nxt = (max(bad_after) + dt.timedelta(7)) if bad_after else \
                last_ok + dt.timedelta(INTERVALS[min(len(ok), 3)])
            due += nxt <= today
        elif s == "retry" and n_checked.get(t, 0) >= 2:
            due += last_checked[t] + dt.timedelta(7) <= today
    rate = f"{round(100 * passed / (passed + failed))}%" if passed + failed else "–"
    return rate, passed + failed, due


def streak(today):
    try:
        out = subprocess.run(["git", "-C", str(REPO), "log", "--format=%cs%x09%ce"],
                             capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return 0
    days = {dt.date.fromisoformat(d) for d, e in (l.split("\t") for l in out.splitlines() if "\t" in l)
            if e.strip() != "noreply@anthropic.com"}
    day = today if today in days else today - dt.timedelta(1)
    n = 0
    while day in days:
        n += 1
        day -= dt.timedelta(1)
    return n


def write_curriculum_marks(tracks, state):
    for tr in tracks:
        lines = tr["file"].read_text(encoding="utf-8").splitlines()
        out, legend_done = [], any(l.startswith("Status: ") for l in lines)
        for line in lines:
            if line.startswith("Status: "):
                out.append(LEGEND)
                continue
            if not legend_done and line.startswith("## "):
                out += [LEGEND, ""]
                legend_done = True
            m = TOPIC_LINE.match(line)
            if m:
                line = f"- {MARKS[state.get(m.group(1), 'todo')]} **{m.group(1)}** {m.group(2)}"
            out.append(line)
        tr["file"].write_text("\n".join(out) + "\n", encoding="utf-8")


def tint(hex_color, amount, base="#fcfcfb"):
    a = [int(hex_color[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(base[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(y + (x - y) * amount) for x, y in zip(a, b))


def esc(s):
    return html.escape(s, quote=True)


def build_svg(tracks, state, today, stats):
    W, pad = 880, 24
    total = sum(len(t["topics"]) for t in tracks)
    mastered = sum(1 for t in tracks for i, _ in t["topics"] if state.get(i) == "mastered")
    week = (today - WEEK_1_MONDAY).days // 7 + 1
    tiles = [
        ("Topics mastered", f"{mastered}", f"of {total}"),
        ("Streak", f"{stats['streak']}", "day" if stats["streak"] == 1 else "days"),
        ("Waiting for you", f"{stats['open']}", "exercise" if stats["open"] == 1 else "exercises"),
        ("Recall pass rate", stats["rate"], f"{stats['due']} due now"),
    ]
    row_h, top_rows = 64, 168
    H = top_rows + row_h * len(tracks) + 12

    css_vars_light = "".join(
        f"--c{i}:{t['light']};--c{i}b:{tint(t['light'], .45)};--c{i}t:{tint(t['light'], .14)};" for i, t in enumerate(tracks))
    css_vars_dark = "".join(
        f"--c{i}:{t['dark']};--c{i}b:{tint(t['dark'], .62, '#1a1a19')};--c{i}t:{tint(t['dark'], .17, '#1a1a19')};" for i, t in enumerate(tracks))
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="Learning progress: {mastered} of {total} topics mastered">',
         "<style>",
         f"svg{{--bg:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--mut:#898781;--line:#e1e0d9;--tile:#f4f3f0;{css_vars_light}}}",
         f"@media (prefers-color-scheme: dark){{svg{{--bg:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--mut:#898781;--line:#2c2c2a;--tile:#232322;{css_vars_dark}}}}}",
         "text{font-family:system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;fill:var(--ink)}",
         ".h{font-size:17px;font-weight:650}.s{font-size:12.5px;fill:var(--ink2)}.m{font-size:12px;fill:var(--mut)}",
         ".tl{font-size:12px;fill:var(--ink2)}.tv{font-size:26px;font-weight:650}.tu{font-size:12.5px;fill:var(--ink2)}",
         ".tr{font-size:14px;font-weight:600}.cnt{font-size:13px;fill:var(--ink2)}",
         "</style>",
         f'<rect width="{W}" height="{H}" rx="12" fill="var(--bg)" stroke="var(--line)"/>',
         f'<text x="{pad}" y="36" class="h">Progress</text>',
         f'<text x="{W - pad}" y="36" class="m" text-anchor="end">Week {week} · updated {today.strftime("%a %-d %b %Y")}</text>']

    gap = 12
    tw = (W - 2 * pad - gap * (len(tiles) - 1)) / len(tiles)
    for i, (label, value, unit) in enumerate(tiles):
        x = pad + i * (tw + gap)
        p.append(f'<rect x="{x:.1f}" y="54" width="{tw:.1f}" height="76" rx="8" fill="var(--tile)"/>')
        p.append(f'<text x="{x + 14:.1f}" y="76" class="tl">{esc(label)}</text>')
        p.append(f'<text x="{x + 14:.1f}" y="113" class="tv">{esc(value)}'
                 f'<tspan class="tu" dx="6">{esc(unit)}</tspan></text>')

    # legend for the two bar segments (shown with the first track's colours)
    ly = 156
    p.append(f'<rect x="{pad}" y="{ly - 9}" width="10" height="10" rx="2" fill="var(--c0)"/>')
    p.append(f'<text x="{pad + 15}" y="{ly}" class="m">mastered</text>')
    p.append(f'<rect x="{pad + 84}" y="{ly - 9}" width="10" height="10" rx="2" fill="var(--c0b)"/>')
    p.append(f'<text x="{pad + 99}" y="{ly}" class="m">in progress (posted or retrying)</text>')

    bw = W - 2 * pad
    for i, tr in enumerate(tracks):
        y = top_rows + i * row_h
        ids = [t for t, _ in tr["topics"]]
        n = len(ids)
        m = sum(state.get(t) == "mastered" for t in ids)
        ip = sum(state.get(t) in ("retry", "open") for t in ids)
        nxt = next(((t, name) for t, name in tr["topics"] if t not in state), None)
        p.append(f'<text x="{pad}" y="{y + 14}" class="tr">{esc(tr["name"])}'
                 f'<tspan class="m" dx="8">{tr["id"]}</tspan></text>')
        p.append(f'<text x="{W - pad}" y="{y + 14}" class="cnt" text-anchor="end">{m} / {n} mastered</text>')
        by = y + 24
        p.append(f'<rect x="{pad}" y="{by}" width="{bw}" height="10" rx="4" fill="var(--c{i}t)"/>')
        wm = bw * m / n if m else 0
        wi = max(bw * ip / n, 6) if ip else 0
        if wm:
            p.append(f'<rect x="{pad}" y="{by}" width="{max(wm, 6):.1f}" height="10" rx="4" fill="var(--c{i})"/>')
        if wi:
            xi = pad + (max(wm, 6) + 2 if wm else 0)
            p.append(f'<rect x="{xi:.1f}" y="{by}" width="{wi:.1f}" height="10" rx="4" fill="var(--c{i}b)"/>')
        label = f"Next: {nxt[0]} {nxt[1]}" if nxt else "All topics posted"
        if len(label) > 92:
            label = label[:89].rstrip() + "…"
        p.append(f'<text x="{pad}" y="{by + 27}" class="s">{esc(label)}</text>')
    p.append("</svg>")
    return "\n".join(p)


def main():
    today = dt.date.today()
    if "--today" in sys.argv:
        today = dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1])
    tracks = parse_curriculum()
    rows = parse_log()
    state, mastered_on, last_checked, n_checked = topic_states(rows)
    rate, n_recalls, due = recall_stats(rows, state, mastered_on, last_checked, n_checked, today)
    stats = {"streak": streak(today), "open": sum(r["status"] == "open" for r in rows),
             "rate": rate, "due": due}
    write_curriculum_marks(tracks, state)
    (REPO / "progress.svg").write_text(build_svg(tracks, state, today, stats), encoding="utf-8")
    print(f"progress: {sum(s == 'mastered' for s in state.values())} mastered, "
          f"{stats['open']} open, streak {stats['streak']}, recall {rate}, {due} due")


if __name__ == "__main__":
    main()
