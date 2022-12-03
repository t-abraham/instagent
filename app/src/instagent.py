# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:50:01 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import sys

from instagrapi import Client
from geopy.geocoders import Nominatim
from pathlib import Path

from src._handelExceptions_ import __handelExceptions__
from src._artwork_ import __artwork__
from src._printlogo_ import __printlogo__
from src._userInput_ import __userInput__
from src._printTargetBanner_ import __printTargetBanner__
from src._login_ import __login__
from src._setTarget_ import __setTarget__
from src._config_ import __config__
from src._printcolors_ import __printcolors__
from src._getMedias_ import __getMedias__
from src._getLocations_ import __getLocations__
from src._getComments_ import __getComments__
from src._getFollowers_ import __getFollowers__
from src._getFollowings_ import __getFollowings__
from src._getUserInfo_ import __getUserInfo__
from src._getLikes_ import __getLikes__
from src._getCaptions_ import __getCaptions__
from src._getTags_ import __getTags__
from src._getAllMediaCounts_ import __getAllMediaCounts__
from src._storeMedias_ import __storeMedias__


#%% instagent

class instagent(
            __handelExceptions__,
            __artwork__,
            __printlogo__,
            __userInput__,
            __printTargetBanner__,
            __login__,
            __setTarget__,
            __config__,
            __printcolors__,
            __getMedias__,
            __getLocations__,
            __getComments__,
            __getFollowers__,
            __getFollowings__,
            __getUserInfo__,
            __getLikes__,
            __getCaptions__,
            __getTags__,
            __getAllMediaCounts__,
            __storeMedias__,
        ):

    def __init__(self):
        super().__init__()
    
    def initialize(self, 
                 target, 
                 defaultcount,
                 defaultmedia,
                 proxy=None,
                 new_cookie=False,
                 is_file=False, 
                 is_json=False, 
                 is_cli=False, 
                 output_dir=None, 
                 is_timeout=5, 
                 main_dir=Path(__file__).parent.resolve()
                 ):
        
        if proxy is None:
            self.api = Client()
            self.proxy = proxy
        else:            
            self.proxy = proxy
            self.api = Client(proxy=self.proxy)
        
        # self.api.handle_exception = self.___handelExceptions___
        self.geolocator = Nominatim(user_agent="http")
        
        self.my_following = None
        
        self.following_target = None
        self.target_user_info = None
        self.target_is_private = None
        self.target_medias = None
        self.target_comments = None
        self.target_followers = None
        self.target_followings = None
        
        try:
            self.main_dir = Path(main_dir)
        except:
            self.main_dir = Path(__file__).parent.resolve()
            
        try:
            self.output_dir = Path(output_dir) or self.main_dir.joinpath(self.output_dir)            
        except:
            self.output_dir = self.main_dir.joinpath("output")
            
        self.output_dir_origin = self.output_dir
        
        try:
            self.timeout = int(is_timeout)
        except:
            self.timeout = 5
            
        if target is None:
            self.___printout___("Target is not assigned. Please enter target's username:\n", self.RED)
            self.target = self.___userInput___()
            if self.target == "":
                sys.exit(0)
        else:
            self.target = target
            
        if defaultcount is None:
            self.defaultcount = None
        else:
            try:
                self.defaultcount = int(defaultcount)
            except:
                self.defaultcount = None
                
        if defaultmedia is None:
            self.defaultmedia = None
        else:
            try:
                self.defaultmedia = int(defaultmedia)
            except:
                self.defaultmedia = None
            
        self.is_cli = is_cli
        if not is_cli:
          print("\nAttempt to login...")
        
        self.is_file = is_file
        self.is_json = is_json
        
        self.conf_dir = self.main_dir.joinpath("config","credentials.ini")
        self.___getUsername___()
        self.___getPassword___()
        self.___login___(self.username, self.password, new_cookie)
        self.___setTarget___()
        self.___printTargetBanner___()        
    
    def set_timeout(self):
        self.___printout___("Insert new input timeout in seconds: ", self.YELLOW)
        is_timeout = self.timedinput()
        try:
            self.timeout = int(is_timeout)
        except:
            pass
        
    def set_is_file(self, flag: bool):
        if flag:
            self.___printout___("Write to file: ")
            self.___printout___("enabled to directory -> {}".format(self.main_dir.joinpath("output")), self.GREEN)
            self.___printout___("\n")
        else:
            self.___printout___("Write to file: ")
            self.___printout___("disabled from directory -> {}".format(self.main_dir.joinpath("output")), self.RED)
            self.___printout___("\n")

        self.is_file = flag

    def set_is_json(self, flag: bool):
        if flag:
            self.___printout___("Export to JSON: ")
            self.___printout___("enabled to directory -> {}".format(self.main_dir.joinpath("output")), self.GREEN)
            self.___printout___("\n")
        else:
            self.___printout___("Export to JSON: ")
            self.___printout___("disabled from directory -> {}".format(self.main_dir.joinpath("output")), self.RED)
            self.___printout___("\n")

        self.is_json = flag
        
    def printlogo(self):
        self.___printlogo___()
        
    def clear_cache(self):
        file = self.main_dir.joinpath("config","{}.json".format(self.username))
        file.unlink()
        self.___printout___("\nCache for user: {} is cleared\n".format(self.username), self.YELLOW)
        self.___printout___("\nCache file deleted - Path '{}'\n".format(file), self.YELLOW)
        
    def change_target(self):
        self.___printout___("Insert new target username:\n", self.YELLOW)
        self.target = self.___userInput___(
                                                default = self.target
                                           )
        self.___setTarget___()        
        self.___printTargetBanner___()
        
    def get_locations(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getLocations___(length)
        
    def get_comments(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getComments___(length, False)

    def get_likes(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getLikes___(length)
    
    def get_captions(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getCaptions___(length)
    
    def get_followers(self):
        self.___getFollowers___()
    
    def get_followings(self):
        self.___getFollowings___()
        
    def get_followers_detailed(self):
        self.___getFollowers___(True)
    
    def get_followings_detailed(self):
        self.___getFollowings___(True)
    
    def get_hashtags(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getTags___(length, "#", False)
        
    def get_hashtags_counts(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getTags___(length, "#", True)
    
    def get_user_info(self):
        self.___getUserInfo___()
    
    def get_all_media_counts(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getAllMediaCounts___(length)
    
    def store_media(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 0)\n", self.YELLOW)
            length = self.___userInput___(
                                                answers = [0,1,2,3,4,5],
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
            
        if self.defaultmedia is None:
            options = {
                "0": "Everything",
                "1": "Photos",
                "2": "Videos",
                "3": "IGTVs",
                "4": "Reels",
                "5": "Albums",
                }        
            self.___printout___("What kind of media do you wish to store?\n", self.YELLOW)
            for key in options.keys():
                self.___printout___("{}: {}\n".format(key, options[key]), self.YELLOW)
    
            self.___printout___("You can select multiple types with a comma in betwwen (ex. 2,3,5)\n", self.YELLOW)
            
            selection = self.___userInput___()
        else:
            selection = self.defaultmedia
            
        if len(selection) == 0:
            selection = ["0"]
        else:
            selection = [i.strip() for i in selection.split(",")]
        
        if "0" in selection:        
            self.___storeMedias___(length, "all")
        else:
            for key in selection:
                self.___storeMedias___(length, options[key].lower())
    
    def get_people_who_commented(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getComments___(length, True)
        
    def get_people_who_tagged(self):
        if self.defaultcount is None:
            self.___printout___("For how many recent posts? (default 10)\n", self.YELLOW)
            length = self.___userInput___(
                                                default = 10
                                          )
            if length == "":
                length = 10
            else:
                try:
                    length = int(length)
                except:
                    length = 10
        else:
            length = self.defaultcount
        self.___getTags___(length, "@", True)    
        
#%% Standalone Run

if __name__ == "__main__":
    pass