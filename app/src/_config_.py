# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:48:17 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import configparser
import sys

#%% __config__

class __config__(object):
    def __init__(self):
        super().__init__()
    def _load_config_file(self):
        try:
            self.config = configparser.ConfigParser(interpolation=None)
            self.config.read(self.conf_dir)
 
        except FileNotFoundError:
            self.___printout___('Error: file "config -> credentials.ini" not found!\n', self.RED)
            sys.exit(0)
        except Exception as e:
            self.___printout___("Error: {}\n".format(e), self.RED)
            sys.exit(0)
            
    def ___updateCredentials___(self):
        try:
            self.config = configparser.ConfigParser(interpolation=None)
            self.config.read(self.conf_dir)
            self.config["Credentials"]["username"] = self.username
            self.config["Credentials"]["password"] = self.password
            
            with open(self.conf_dir, 'w') as f:
                self.config.write(f)
 
        except FileNotFoundError:
            self.___printout___('Error: file "config -> credentials.ini" not found!\n', self.RED)
            sys.exit(0)
        except Exception as e:
            self.___printout___("Error: {}\n".format(e), self.RED)
            sys.exit(0)
                
    def ___getUsername___(self):
        try:
            self._load_config_file()
            self.username = self.config["Credentials"]["username"]
    
            if self.username == '':
                self.___printout___('Error: "username" field cannot be blank in "config -> credentials.ini"\n', self.RED)
                sys.exit(0)
    
        except KeyError:
            self.___printout___('Error: missing "username" field in "config -> credentials.ini"\n', self.RED)
            sys.exit(0)
    
    def ___getPassword___(self):
        try:
            self._load_config_file()
            self.password = self.config["Credentials"]["password"]
    
            if self.password == '':
                self.___printout___('Error: "password" field cannot be blank in "config -> credentials.ini"\n', self.RED)
                sys.exit(0)
    
        except KeyError:
            self.___printout___('Error: missing "password" field in "config -> credentials.ini"\n', self.RED)
            sys.exit(0)
            
#%% Standalone Run    
if __name__ == "__main__":
    pass
