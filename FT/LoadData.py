#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import os
import scipy.io as spio


global Meri_mat
global Leaf_mat
global dataTotal
global dataTotal_leaf

# loading all the expression data
Meri_mat = spio.loadmat('dataset_qPCR_normalized_Meristem.mat')
Leaf_mat = spio.loadmat('dataset_qPCR_normalized_Leaf.mat')
dataTotal    = Meri_mat['xdata']
dataTotal_leaf = Leaf_mat['xdata_leaf']

