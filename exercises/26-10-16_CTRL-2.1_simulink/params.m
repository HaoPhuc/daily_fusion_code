% params.m -- parameters for the coil-current model
% Run this before simulating, or call it from Model Properties > Callbacks > InitFcn.

L      = 0.02;   % coil inductance [H]
R      = 0.1;    % coil + supply resistance [Ohm]
V0     = 50;     % supply voltage after switch-on [V]
t_stop = 1.5;    % simulation stop time [s]
