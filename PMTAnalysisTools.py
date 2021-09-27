"""
developing OOP approach to this here, then putting it in a separate
.py module
"""

import numpy as np

class PMT():
    
    def __init__(self,paramters):
        
        self.x = paramters[0]
        self.y = paramters[1]
        self.z = paramters[2]
        
    def GetPosition(self):
        
        return(x,y,z)


class Ophit:
    
    def __init__(self,parameters):
        
        self.run          = parameters[0]
        self.event            = parameters[1]
        self.timestamp      = parameters[2]
        self.flash_id       = parameters[3]
        self.channel_id     = parameters[4]
        self.integral       = parameters[5]
        self.amplitude      = parameters[6]
        self.start_time     = parameters[7]
        self.abs_start_time = parameters[8]
        self.pe             = parameters[9]
        self.width          = parameters[10]
        self.fast_to_total  = parameters[11]
        
    def GetPosition(self, pmt_directory):
        
        """
        returns a tuple with x, y, and z coordinate associated with an
        optical hit
        """
        
        return(pmt_directory[self.channel_id].GetPosition())
    
class Flash():
    
    def __init__(self,parameters):
        
        self.ophits = []
        
        self.run                = parameters[0]
        self.event              = parameters[1]
        self.timestamp          = parameters[2]
        self.flash_id           = parameters[3]
        self.multiplicity       = parameters[4]
        self.multiplicity_right = parameters[5]
        self.multiplicity_left  = parameters[6]
        self.sum_pe             = parameters[7]
        self.sum_pe_right       = parameters[8]
        self.sum_pe_left        = parameters[9]
        self.flash_time         = parameters[10]
        self.flash_y            = parameters[11]
        self.flash_width_y      = parameters[12]
        self.flash_z            = parameters[13]
        self.flash_width_z      = parameters[14]
        
    def AddOpHit(self,ophit):
        
        self.ophits.append(ophit)
        
    def GetOpHits(self):
        
        return self.ophits
    
class Event():
    
    def __init__(self,parameters):
        
        self.flashes = {}
        
        self.run             = parameters[0]
        self.event           = parameters[1]
        self.timestamp       = parameters[2]
        self.nflashes        = parameters[3]
        self.nophits         = parameters[4]
        self.beam_gate_start = parameters[5]
        self.beam_gate_width = parameters[6]
        self.beam_type       = parameters[7]
        
    def AddFlash(self,flash):
        
        self.flashes[flash.flash_id]=flash
        
    def GetFlashes(self):
        
        return self.flashes