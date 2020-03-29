#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:39:09 2020

@author: larsno
"""

import powerclasses as pc

CB42 = pc.CircuitBreaker(42,5,100,True)
print (type(CB42))
print (CB42.ID)



