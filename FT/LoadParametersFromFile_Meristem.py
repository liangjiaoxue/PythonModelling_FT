#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
from sys import platform



# Global variables
# The parameters of the equations

global ode_parameters
global FLC_expression
global SVP_expression
global FT_expression


ode_parameters = [None]	*4
FLC_expression =  [None]*(16+1)
SVP_expression =  [None]*(16+1)
FT_expression =  [None]*(16+1)

MichaelisMenten_parameters_values_file = os.path.join(os.getcwd(),'parameters/meristem/MichaelisMenten_parameters_values.txt')
# File with the values of Michaelis Menten parameters
Decay_parameters_values_file = os.path.join(os.getcwd(),'parameters/meristem/Decay_parameters_values.txt')
# File with the values of decay parameters
Other_parameters_values_file = os.path.join(os.getcwd(),'parameters/meristem/Other_parameters_values.txt')
# File with the values of other parameters
FD_parameters_values_file = os.path.join(os.getcwd(),'parameters/meristem/FD_parameters_values.txt')

if platform.startswith('win'):
	MichaelisMenten_parameters_values_file = os.path.join(os.getcwd(), 'parameters\\meristem\\MichaelisMenten_parameters_values.txt')
	# File with the values of Michaelis Menten parameters
	Decay_parameters_values_file = os.path.join(os.getcwd(), 'parameters\\meristem\\Decay_parameters_values.txt')
	# File with the values of decay parameters
	Other_parameters_values_file = os.path.join(os.getcwd(), 'parameters\\meristem\\Other_parameters_values.txt')
	# File with the values of other parameters
	FD_parameters_values_file = os.path.join(os.getcwd(), 'parameters\\meristem\\FD_parameters_values.txt')

# ########## LOAD THE PARAMETER VALUES ################################################
MichaelisMenten_parameters = np.loadtxt(MichaelisMenten_parameters_values_file)
Decay_parameters		   = np.loadtxt(Decay_parameters_values_file)

Other_parameters		   = np.loadtxt(Other_parameters_values_file)

FD_parameters		   = np.loadtxt(FD_parameters_values_file)

ode_parameters_0 =np.append(MichaelisMenten_parameters.tolist(), Decay_parameters.tolist())
ode_parameters_1 = np.append(ode_parameters_0.tolist(), Other_parameters.flatten().tolist())
ode_parameters =np.append(ode_parameters_1.tolist(), FD_parameters.tolist())

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Fit FLC expression
FLC_expression[16]=-1.151618649491879e+003
FLC_expression[15]=1.154358982837153e+003
FLC_expression[14]=-5.083673796371651e+002
FLC_expression[13]=1.303269284718195e+002
FLC_expression[12]=-21.760709882600381
FLC_expression[11]=2.512699005039366
FLC_expression[10]=-0.208037619654221
FLC_expression[9]=0.012630096859507
FLC_expression[8]=-5.693916747403002e-004
FLC_expression[7]=1.914208476296976e-005
FLC_expression[6]=-4.778214433598770e-007
FLC_expression[5]=8.727369278585306e-009
FLC_expression[4]=-1.132558929532852e-010
FLC_expression[3]=9.885128932383386e-013
FLC_expression[2]=-5.201397833122582e-015
FLC_expression[1]=1.246470626086996e-017
del FLC_expression[0]
# Fit SVP expression
SVP_expression[16]=-5.523660050362068e+004
SVP_expression[15]=5.828177432591093e+004
SVP_expression[14]=-2.685354821464235e+004
SVP_expression[13]=7.161567530925968e+003
SVP_expression[12]=-1.237772249023380e+003
SVP_expression[11]=1.473057791814383e+002
SVP_expression[10]=-12.522714267250171
SVP_expression[9]=0.778101634969475
SVP_expression[8]=-0.035802708113345
SVP_expression[7]=0.001225602226814
SVP_expression[6]=-3.108942022337164e-005
SVP_expression[5]=5.760684190005275e-007
SVP_expression[4]=-7.572810025668374e-009
SVP_expression[3]=6.687028309495522e-011
SVP_expression[2]=-3.555881938702022e-013
SVP_expression[1]=8.603372112575900e-016
del SVP_expression[0]
# Fit FT expression
FT_expression[16]=-0.006226245259489
FT_expression[15]=-0.668914766959784
FT_expression[14]=0.259918945139703
FT_expression[13]=-0.016390391774916
FT_expression[12]=-0.008549776636358
FT_expression[11]=0.002601202786480
FT_expression[10]=-3.780167465286363e-004
FT_expression[9]=3.477692239498646e-005
FT_expression[8]=-2.193367124773714e-006
FT_expression[7]=9.785024031300842e-008
FT_expression[6]=-3.117224177111983e-009
FT_expression[5]=7.046695208966971e-011
FT_expression[4]=-1.103779349569078e-012
FT_expression[3]=1.138786737254349e-014
FT_expression[2]=-6.958725764920688e-017
FT_expression[1]=1.907495859308863e-019
del FT_expression[0]