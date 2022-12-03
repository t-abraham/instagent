# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:48:17 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import sys

#%% __printcolors__

class __printcolors__(object):
    def __init__(self):
        super().__init__()
        self.BLACK, self.RED, \
        self.GREEN, self.YELLOW, \
        self.BLUE, self.MAGENTA, \
        self.CYAN, self.WHITE = range(8)

    def ___printout___(self, text, colour=None):
        if colour is None:
            colour = self.WHITE 
        try:
            seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
            sys.stdout.write (seq)
        except:
            sys.stdout.write (text)
            
#%% Standalone Run    
if __name__ == "__main__":
    pass

