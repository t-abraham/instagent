# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

#%% __setTarget__

class __setTarget__(object):
    def __init__(self):
        super().__init__()
    def ___setTarget___(self):
        if self.target_user_info is None or self.target_id is None:
            try:
                self.target_id = int(self.target)
                self.target_user_info = self.api.user_info(self.target_id)
            except:
                self.target_user_info = self.api.user_info_by_username(self.target)
                self.target_id = self.target_user_info.pk
            self.target_is_private = self.target_user_info.is_private
                
        if self.my_following is None:
            self.my_following = self.api.user_following(self.api.user_id)
                    
        self.following_target = self.target_user_info.pk in self.my_following
        
        if self.following_target is False:
            self.___printout___("You are NOT FOLLOWING {}. Do you want to follow the user? (y/n)\n".format(self.target), self.RED)
            user_input = str(self.___userInput___(
                                                   answers=["yes","no","y","n",],
                                                   default="n"
                                                 )).lower()[0]
            if user_input == "y":
                self.api.user_follow(self.target_id)
            if self.target_is_private is False:
                self.my_following = self.api.user_following(self.api.user_id)
                self.following_target = self.target_user_info.pk in self.my_following
                
        self.output_dir = self.output_dir_origin.joinpath(str(self.target))
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
#%% Standalone Run

if __name__ == "__main__":
    pass