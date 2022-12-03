# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable

#%% __getFollowers__

class __getFollowers__(object):
    def __init__(self):
        super().__init__()
    def ___getFollowers___(self, detailed=False):
        if self.target_followers is None:
            self.target_followers = self.api.user_followers(self.target_id)
        if len(self.target_followers) > 0:
            self.___printout___("\nWoohoo! We found " + str(len(self.target_followers)) + " followers\n", self.GREEN)
            if detailed is True:
                t = PrettyTable()

                t.field_names = [
                    "Target's Follower ID", 
                    "Target's Follower UserName", 
                    "Target's Follower Name",
                    "Target's Follower Private Profile",
                    "Target's Follower Verified", 
                    "Target's Follower Media Count", 
                    "Target's Follower Follower Count",
                    "Target's Follower Following Count",            
                    "Target's Follower Biography",            
                    "Target's Follower Email",            
                    "Target's Follower Phone"
                    ]
                t.align["Target's Follower ID"] = "l"
                t.align["Target's Follower UserName"] = "l"
                t.align["Target's Follower Name"] = "l"
                t.align["Target's Follower Private Profile"] = "l"
                t.align["Target's Follower Verified"] = "l"
                t.align["Target's Follower Media Count"] = "l"
                t.align["Target's Follower Follower Count"] = "l"
                t.align["Target's Follower Following Count"] = "l"
                t.align["Target's Follower Biography"] = "l"
                t.align["Target's Follower Email"] = "l"
                t.align["Target's Follower Phone"] = "l"                
                                
                follower_list = []
                
                for key in self.target_followers.keys():
                    targets_follower_user_info = self.api.user_info(self.target_followers[key].pk)                     
                    t.add_row([
                                    str(targets_follower_user_info.pk),
                                    str(targets_follower_user_info.username),
                                    str(targets_follower_user_info.full_name),
                                    str(targets_follower_user_info.is_private),
                                    str(targets_follower_user_info.is_verified),
                                    str(targets_follower_user_info.media_count),
                                    str(targets_follower_user_info.follower_count),
                                    str(targets_follower_user_info.following_count),
                                    str(targets_follower_user_info.biography),
                                    str(targets_follower_user_info.public_email),
                                    str(targets_follower_user_info.contact_phone_number),
                              ])            
    
                    if self.is_json:
                        follower_list.append({
                                                "Target's Follower ID"                 :       str(targets_follower_user_info.pk),
                                                "Target's Follower UserName"           :       str(targets_follower_user_info.username),
                                                "Target's Follower Name"               :       str(targets_follower_user_info.full_name),
                                                "Target's Follower Private Profile"    :       str(targets_follower_user_info.is_private),
                                                "Target's Follower Verified"           :       str(targets_follower_user_info.is_verified),
                                                "Target's Follower Media Count"        :       str(targets_follower_user_info.media_count),
                                                "Target's Follower Follower Count"     :       str(targets_follower_user_info.follower_count),
                                                "Target's Follower Following Count"    :       str(targets_follower_user_info.following_count),
                                                "Target's Follower Biography"          :       str(targets_follower_user_info.biography),
                                                "Target's Follower Email"              :       str(targets_follower_user_info.public_email),
                                                "Target's Follower Phone"              :       str(targets_follower_user_info.contact_phone_number),
                                            })
            else:
                t = PrettyTable()
    
                t.field_names = ['Follower ID', 'Follower UserName', 'Follower Name']
                t.align["Follower ID"] = "l"
                t.align["Follower UserName"] = "l"
                t.align["Follower Name"] = "l"                
                                
                follower_list = []
                
                for key in self.target_followers.keys():                    
                    t.add_row([
                                    str(self.target_followers[key].username), 
                                    str(self.target_followers[key].pk), 
                                    str(self.target_followers[key].full_name),
                              ])            
    
                    if self.is_json:
                        follower_list.append(
                                            {
                                                'Follower ID'           :       str(self.target_followers[key].pk),
                                                'Follower UserName'     :       str(self.target_followers[key].username),
                                                'Follower Name'         :       str(self.target_followers[key].full_name),
                                            }
                                         )

            json_data = {}
            
            if self.is_file is True:                
                file_name = self.output_dir.joinpath(self.target + "_followers.txt")
                if file_name.exists():
                    file_name.unlink() 
                file = open(file_name, "w")
                file.write(str(t))
                file.close()

            if self.is_json is True:
                json_data['follower'] = follower_list
                json_file_name = self.output_dir.joinpath(self.target + "_followers.json")
                if json_file_name.exists():
                    json_file_name.unlink()
                with open(json_file_name, 'w') as f:
                    json.dump(json_data, f)
                    
            print(t)
        else:
            self.___printout___("Sorry! No results found :-(\n", self.RED)
#%% Standalone Run

if __name__ == "__main__":
    pass