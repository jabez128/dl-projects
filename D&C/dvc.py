#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################

"""
    @author: zhanghaoran@baidu.com
"""

import os
import keras
import numpy as np
from sklearn.model_selection import train_test_split

dataset_dir = './dog_cat/train'

dataset = np.array(os.listdir(dataset_dir))
np.random.shuffle(dataset)

extractname = np.vectorize(lambda name: 'cat' if 'cat' in name else 'dog')

target = extractname(dataset)

print(target)

'''
train_dataset, test_dataset = train_test_split(dataset, target, split=0.2)

print(len(train_dataset))
'''









