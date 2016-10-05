#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import integrate
from matplotlib.pylab import *
import importlib.util
import os

# set working directory
path='D:\\Dropbox\\PythonModelling\\SourceForPlosONE\\'
# path='C:\\Users\\lxue\\Dropbox\\PythonModelling\\FT\\'
os.chdir(path)
# loading parameter values

from LoadParametersFromFile_Leaf import *
from LoadParametersFromFile_Meristem import *
from ode_equations import *
from LoadData import *


# settings
time_begin = 5
time_end   = 17
interval = 0.0001
time_odes =    np.arange(time_begin, time_end, interval)


# Set the time range
floweringTime_WT_Col0=12.63
delta_t = 0.001
FT_range_time= np.arange(5,floweringTime_WT_Col0,0.001)
num_steps = FT_range_time.shape[0] + 1

# Set initial condition(s): for integrating variable and time!
initial_Expression = np.array([dataTotal[1-1,1-1], dataTotal[1-1,2-1], dataTotal[1-1,3-1], dataTotal[1-1,4-1], dataTotal_leaf[1-1,3-1], dataTotal[1-1,8-1]])
t_start = 5

# Additional Python step: create vectors to store trajectories
t_flower_t = np.zeros((num_steps, 1))
t_flower_out = []
t_flower_out.append(initial_Expression.tolist())
t_flower_t[0] = t_start
#

if __name__ == '__main__':
    # Start by specifying the integrator:
    # use ``vode`` with "backward differentiation formula"
    r = integrate.ode(ode_equations).set_integrator('vode', method='bdf')
    r.set_initial_value(initial_Expression, t_start).set_f_params(ode_parameters, ode_parameters_leaf)

    # Integrate the ODE(s) across each delta_t timestep
    k = 1
    while r.successful() and k < num_steps:
        r.integrate(r.t + delta_t)
        # Store the results to plot later
        t_flower_t[k] = r.t
        #np.append(t_flower_out,r.y)
        t_flower_out .append( r.y.tolist())
        k += 1
    # All done!  Plot the trajectories:

    out_mat = np.array(t_flower_out)
    AP1_expression_flowering = out_mat[out_mat.shape[0]-1,3]
    t_flower_out(t_flower_out, 3)
    # plot
    #plot(t_flower_t, out_mat[:, 0])
    #plot(t_flower_t, out_mat[:, 1])
    plot(t_flower_t, out_mat[:, 2])
    plot(t_flower_t, out_mat[:, 3])
    plot(t_flower_t, out_mat[:, 4])
    plot(t_flower_t, out_mat[:, 5])
    plt.legend(['LFY', 'AP1','FT','FD'], loc='upper left')
    #plt.legend(['AGL24' 'SOC1', 'LFY', 'AP1','FT','FD'], loc='upper left')
    show()

