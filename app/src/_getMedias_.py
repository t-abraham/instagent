# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

#%% __getMedias__

class __getMedias__(object):
    def __init__(self):
        super().__init__()
    def ___getMedias___(self, length=0):
        self.target_medias = self.api.user_medias(self.target_id, length)
        
#%% Standalone Run

if __name__ == "__main__":
    pass