# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:19:27 2022

@author: znoll
"""
import math 

def calc(shape,a,b,t):
    # shape from 'shs', 'chs', 'I' etc
    # a is width
    # b is height
    # t is thickness
    
    def rect(a,b):
        # Second moment area of rectangle
        #       base height
        return (a  *   b**3) / 12
        
    if shape == 'shs':
        # vertical half wall
        A_area = t*(0.5*b - 2*t)
        A_centroid = (0.5*b - 2*t) / 2
        A_sma = rect(t,0.5*b-2*t)
        A_sma_tot = A_sma + A_area*A_centroid**2
        
        # horizontal half roof
        B_area = t*(0.5*a - 2*t)
        B_centroid = 0.5*b - 0.5*t
        B_sma = rect(0.5*a-2*t,t)
        B_sma_tot = B_sma + B_area*B_centroid**2
        
        # radius
        radius_contribute = True
        C_area = 0.75*math.pi*t**2 * radius_contribute
        C_centroid = (28/(9*math.pi))*t + 0.5*b
        C_sma = (15/16)*math.pi*t**4
        C_sma_tot = C_sma + C_area*C_centroid**2
        
        return 4*(A_sma_tot + B_sma_tot + C_sma_tot)
        
        