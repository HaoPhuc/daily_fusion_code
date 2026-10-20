% time: ?? min
% Gyro-radius in a tokamak: your first MATLAB functions (CTRL-1.1)
% Run:  type  solution  in the MATLAB Command Window,  or  octave-cli solution.m
%
% This is a FUNCTION FILE: the first function, solution(), has the same name
% as the file and is what runs. The functions below it are LOCAL functions:
% only code in this file can call them.

function solution()
  e   = 1.602e-19;   % elementary charge [C]
  m_D = 3.344e-27;   % deuteron mass [kg]
  m_e = 9.109e-31;   % electron mass [kg]
  B   = 5.3;         % magnetic field [T]
  T   = 10e3;        % temperature: 10 keV, written in eV

  v_D = thermal_speed(T, m_D);
  r_D = larmor_radius(v_D, m_D, e, B);
  fprintf('deuteron: v = %.3e m/s,  r_L = %.3e m\n', v_D, r_D);

  % TODO 2a: the same two calls for the electron (use m_e)
  v_e = 0;
  r_e = 0;
  fprintf('electron: v = %.3e m/s,  r_L = %.3e m\n', v_e, r_e);

  % TODO 2b: uncomment the next line, run, read the error, then comment it out again
  % disp(v)
end


function v = thermal_speed(T_eV, m)
  % Thermal speed sqrt(k_B T / m) for a temperature T_eV given in eV.
  e = 1.602e-19;     % J per eV
  v = 0;             % TODO 1a
end


function r = larmor_radius(v, m, q, B)
  % Larmor (gyro) radius of a particle with speed v, mass m, charge q in field B.
  r = 0;             % TODO 1b
end

% TODO 2b: complete the sentence.
% disp(v) fails in solution() because ___.
