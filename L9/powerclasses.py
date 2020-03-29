#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:40:00 2020

@author: larsno
"""

class Switch:
# """ This class represents a physical element in the power system that
#   can open or close, meaning that it can swithc betwen zero impedance
#   or infinite impedance, the pos attribute is True if the Switch is
#   conducting, i.e. impedance is zero, ID represents a referencenumber"""

    def __init__(self, ID, pos = True):      
        self.ID = ID
        self.pos = pos
        
        
class Disconnector(Switch):
# """ This class represents a Disconnector, which is a Switch capable of
# receiving a send or open command, and while if asked change state.
    
    def open(self):
        if self.pos == True:
            self.pos = False
        
    def close(self):
        if self.pos == False:
            self.pos = True
             



class CircuitBreaker(Disconnector):
#   """This class represents a circuitbreaker,  The NoOfOps attribute is 
#  used to track the number of breaking operations. The NomCurr attribute
#  represents the operating current the CB is deisgned for"""
    
    def __init__(self, ID, NoOfOps, NomCurr, pos):
        super().__init__(ID, pos = True)
        self.NoOfOps = NoOfOps
        self.NomCurr = NomCurr
        
            
    def getInterruptedCurrent(self):
        return self.NoOfOps*self.NomCurr
    