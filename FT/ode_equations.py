#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import integrate
import LoadData
import LoadParametersFromFile_Leaf 
import LoadParametersFromFile_Meristem


dataTotal = LoadData.dataTotal
#parameters = LoadParametersFromFile_Meristem.ode_parameters
SVP_expression = LoadParametersFromFile_Meristem.SVP_expression
FLC_expression = LoadParametersFromFile_Meristem.FLC_expression
FT_expression = LoadParametersFromFile_Meristem.FT_expression

dataTotal_leaf = LoadData.dataTotal_leaf
#parameters_leaf = LoadParametersFromFile_Leaf.ode_parameters_leaf
SVP_expression_leaf = LoadParametersFromFile_Leaf.SVP_expression_leaf
FLC_expression_leaf = LoadParametersFromFile_Leaf.FLC_expression_leaf

# regular function
def ode_equation_FT_leaf(t, x, parameters):
    global dataTotal
    global dataTotal_leaf
    global time
    global SVP_expression_leaf
    global FLC_expression_leaf

    Km_FT_1 = parameters[1 - 1]
    Km_FT_2 = parameters[2 - 1]
    Beta_FT_1 = parameters[3 - 1]
    dc_FT = parameters[4 - 1]
    SVP_leaf = np.polyval(SVP_expression_leaf, t)
    FLC_leaf = np.polyval(FLC_expression_leaf, t)
    FT = x
    if t < 5 :
        SVP_leaf = dataTotal_leaf[1-1, 1-1]
        FLC_leaf = dataTotal_leaf[1-1, 2-1]
    if t > 17:
        SVP_leaf = dataTotal_leaf[13-1, 1-1]
        FLC_leaf = dataTotal_leaf[13-1, 2-1]
    d_FT_dt = Beta_FT_1 * (((Km_FT_1) / (Km_FT_1 + SVP_leaf)) * ((Km_FT_2) / (Km_FT_2 + FLC_leaf))) - dc_FT * FT
    dxdt = np.transpose(np.array([d_FT_dt]))
    return dxdt


def ode_equations( t,y, parameters, parameters_leaf):
    global dataTotal
    global dataTotal_leaf
    global time
    global SVP_expression
    global FLC_expression
    global FT_expression
    global SVP_expression_leaf
    global FLC_expression_leaf


    Km_AGL24_1 = parameters[1-1]
    Km_SOC1_1 = parameters[2-1]
    Km_SOC1_2 = parameters[3-1]
    Km_SOC1_3 = parameters[4-1]
    Km_SOC1_4 = parameters[5-1]
    Km_SOC1_5 = parameters[6-1]
    Km_SOC1_6 = parameters[7-1]

    Km_LFY_1 = parameters[8-1]
    Km_LFY_2 = parameters[9-1]
    Km_LFY_3 = parameters[10-1]

    Km_AP1_1 = parameters[11-1]
    Km_AP1_2 = parameters[12-1]
    Km_AP1_3 = parameters[13-1]

    Beta_AGL24_1 = parameters[14-1]

    Beta_SOC1_1 = parameters[15-1]
    Beta_SOC1_2 = parameters[16-1]
    Beta_SOC1_3 = parameters[17-1]

    Beta_LFY_1 = parameters[18-1]
    Beta_LFY_2 = parameters[19-1]
    Beta_LFY_3 = parameters[20-1]

    Beta_AP1_1 = parameters[21-1]
    Beta_AP1_2 = parameters[22-1]
    Beta_AP1_3 = parameters[23-1]

    dc_AGL24 = parameters[24-1]
    dc_SOC1 = parameters[25-1]
    dc_LFY = parameters[26-1]
    dc_AP1 = parameters[27-1]

    Delay_FT = parameters[28-1]

    Km_FD_1 = parameters[29-1]
    beta_FD_1 = parameters[30-1]
    dc_FD = parameters[31-1]

    Km_FT_1 = parameters_leaf[1-1]
    Km_FT_2 = parameters_leaf[2-1]
    Beta_FT_1 = parameters_leaf[3-1]
    dc_FT = parameters_leaf[4-1]

    AGL24,SOC1,LFY,AP1 ,FT, FD = y.tolist()


    SVP = np.polyval(SVP_expression, t)
    FLC = np.polyval(FLC_expression, t)
    SVP_leaf = np.polyval(SVP_expression_leaf, t)
    FLC_leaf=np.polyval(FLC_expression_leaf, t)

    if t<5:
        SVP_leaf = dataTotal_leaf[1-1, 1-1]
        FLC_leaf = dataTotal_leaf[1-1, 2-1]
        SVP = dataTotal[1-1, 5-1]
        FLC = dataTotal[1-1, 6-1]
    elif t>17:
        SVP_leaf = dataTotal_leaf[13-1, 1-1]
        FLC_leaf = dataTotal_leaf[13-1, 2-1]
        SVP = dataTotal[13-1, 5-1]
        FLC = dataTotal[13-1, 6-1]

    if SVP_leaf<0:
        SVP_leaf = 0
    if FLC_leaf<0:
        FLC_leaf = 0
    if SVP<0:
        SVP = 0
    if FLC<0:
        FLC = 0
    if FT<0:
        FT = 0

    d_AGL24_dt = (Beta_AGL24_1 * SOC1 / (SOC1 + Km_AGL24_1)) - dc_AGL24 * AGL24

    d_SOC1_dt = (((Beta_SOC1_1 * AGL24 / (Km_SOC1_1 + AGL24)) + (Beta_SOC1_2 * SOC1 / (Km_SOC1_2 + SOC1))) + ((Beta_SOC1_3 * FT / (Km_SOC1_3 + FT)) * (FD / (Km_SOC1_4 + FD)))) * (Km_SOC1_5 / (Km_SOC1_5 + SVP) * Km_SOC1_6 / (Km_SOC1_6 + FLC)) - dc_SOC1 * SOC1

    d_LFY_dt = (((Beta_LFY_1 * AGL24 / (AGL24 + Km_LFY_1)) + (Beta_LFY_2 * SOC1 / (SOC1 + Km_LFY_2)) + (Beta_LFY_3 * AP1 / (AP1 + Km_LFY_3)))) - dc_LFY * LFY

    d_AP1_dt = (Beta_AP1_1 * (LFY ** 3) / ((LFY ** 3) + Km_AP1_1)) + (Beta_AP1_2 * (FT / (FT + Km_AP1_2))) + (Beta_AP1_3 * (FD / (FD + Km_AP1_3))) - dc_AP1 * AP1

    d_FT_dt = ode_equation_FT_leaf((t - Delay_FT), FT, parameters_leaf)
    d_FD_dt = beta_FD_1 * LFY / (LFY + Km_FD_1) - dc_FD * FD

    # Output from ODE function must be a COLUMN vector, with n rows
    out = np.array([d_AGL24_dt, d_SOC1_dt, d_LFY_dt, d_AP1_dt, d_FT_dt.tolist()[0], d_FD_dt])
    #dxdt = out
    #y = out
    return out





