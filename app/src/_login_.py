# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:24:45 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory


#%% Standalone Run

class __login__(object):
    def __init__(self):
        super().__init__()
    def ___login___(self, u, p, new_cookie=False):
        settings_file = self.main_dir.joinpath("config","{}.json".format(u))
        if new_cookie is True or not settings_file.exists():
            # settings file does not exist
            print(f'Unable to find file: {settings_file!s}')
    
            # login new
            self.api.login(u, p)
            self.api.dump_settings(settings_file)
    
        else:
            self.api.load_settings(settings_file)
            self.api.login(u, p)
#%% Standalone Run

if __name__ == "__main__":
    pass