# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory


#%% __printlogo__

class __printlogo__(object):
    def __init__(self):
        super().__init__()
    def ___printlogo___(self):
        self.___printout___(self.ascii_art, self.YELLOW)
        self.___printout___("\nVersion 2.0 - Developed by Tahasanul Abraham\n\n", self.YELLOW)
        self.___printout___("Type 'list' to show all allowed commands\n")
        self.___printout___("Type 'FILE=y' to save results to files like '<target username>_<command>.txt (default is disabled)'\n")
        self.___printout___("Type 'FILE=n' to disable saving to files'\n")
        self.___printout___("Type 'JSON=y' to export results to a JSON files like '<target username>_<command>.json (default is disabled)'\n")
        self.___printout___("Type 'JSON=n' to disable exporting to files'\n")
