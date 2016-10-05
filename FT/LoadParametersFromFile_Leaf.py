#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
from sys import platform


# Global variables
global ode_parameters_leaf
global FLC_expression_leaf
global SVP_expression_leaf


ode_parameters_leaf = [None] * 2
FLC_expression_leaf = [None]*(5+1)
SVP_expression_leaf = [None]*(3+1)


# File with the values of Michaelis Menten parameters
MichaelisMenten_parameters_values_file = os.path.join(os.getcwd(),'parameters/leaf/MichaelisMenten_parameters_values.txt')
# File with the values of decay parameters
Decay_parameters_values_file=os.path.join(os.getcwd(),'parameters/leaf/Decay_parameters_values.txt')

if platform.startswith('win'):
    # File with the values of Michaelis Menten parameters
    MichaelisMenten_parameters_values_file = os.path.join(os.getcwd(),
                                            'parameters\\leaf\\MichaelisMenten_parameters_values.txt')
    # File with the values of decay parameters
    Decay_parameters_values_file = os.path.join(os.getcwd(), 'parameters\\leaf\\Decay_parameters_values.txt')

# ########## LOAD THE PARAMETER VALUES ################################################
# Load the values of Michaelis Menten parameters
MichaelisMenten_parameters_leaf =np.loadtxt(MichaelisMenten_parameters_values_file)
# Load the values of Decay parameters
Decay_parameters_leaf =np.loadtxt(Decay_parameters_values_file)

# Put all parameter values in one single vector
ode_parameters_leaf=np.append(MichaelisMenten_parameters_leaf .tolist(),Decay_parameters_leaf.tolist())

# Fit FLC expression
FLC_expression_leaf[1]=-0.000402201797134
FLC_expression_leaf[2]=0.017789844737076
FLC_expression_leaf[3]=-0.270793095966113
FLC_expression_leaf[4]=1.551677713707717
FLC_expression_leaf[5]=-1.864067996948016
del FLC_expression_leaf[0]

# Fit SVP expression
SVP_expression_leaf[1]=-0.531536924525477
SVP_expression_leaf[2]=15.426454188461598
SVP_expression_leaf[3]=1.006072065609388e+002
del SVP_expression_leaf[0]
