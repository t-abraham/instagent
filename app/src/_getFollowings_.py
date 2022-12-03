# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable

#%% __getFollowers__

class __getFollowings__(object):
    def __init__(self):
        super().__init__()
    def ___getFollowings___(self, detailed=False):
        if self.target_followings is None:
            self.target_followings = self.api.user_following(self.target_id)
        if len(self.target_followings) > 0:
            self.___printout___("\nWoohoo! We found " + str(len(self.target_followings)) + " followings\n", self.GREEN)
            if detailed is True:
                t = PrettyTable()

                t.field_names = [
                    "Target's Following ID", 
                    "Target's Following UserName", 
                    "Target's Following Name",
                    "Target's Following Private Profile",
                    "Target's Following Verified", 
                    "Target's Following Media Count", 
                    "Target's Following Follower Count",
                    "Target's Following Following Count",            
                    "Target's Following Biography",            
                    "Target's Following Email",            
                    "Target's Following Phone"
                    ]
                t.align["Target's Following ID"] = "l"
                t.align["Target's Following UserName"] = "l"
                t.align["Target's Following Name"] = "l"
                t.align["Target's Following Private Profile"] = "l"
                t.align["Target's Following Verified"] = "l"
                t.align["Target's Following Media Count"] = "l"
                t.align["Target's Following Follower Count"] = "l"
                t.align["Target's Following Following Count"] = "l"
                t.align["Target's Following Biography"] = "l"
                t.align["Target's Following Email"] = "l"
                t.align["Target's Following Phone"] = "l"                
                                
                follower_list = []
                
                for key in self.target_followings.keys():
                    targets_following_user_info = self.api.user_info(self.target_followings[key].pk)                   
                    t.add_row([
                                    str(targets_following_user_info.pk),
                                    str(targets_following_user_info.username),
                                    str(targets_following_user_info.full_name),
                                    str(targets_following_user_info.is_private),
                                    str(targets_following_user_info.is_verified),
                                    str(targets_following_user_info.media_count),
                                    str(targets_following_user_info.follower_count),
                                    str(targets_following_user_info.following_count),
                                    str(targets_following_user_info.biography),
                                    str(targets_following_user_info.public_email),
                                    str(targets_following_user_info.contact_phone_number),
                              ])            
    
                    if self.is_json:
                        follower_list.append({
                                                "Target's Following ID"                 :       str(targets_following_user_info.pk),
                                                "Target's Following UserName"           :       str(targets_following_user_info.username),
                                                "Target's Following Name"               :       str(targets_following_user_info.full_name),
                                                "Target's Following Private Profile"    :       str(targets_following_user_info.is_private),
                                                "Target's Following Verified"           :       str(targets_following_user_info.is_verified),
                                                "Target's Following Media Count"        :       str(targets_following_user_info.media_count),
                                                "Target's Following Follower Count"     :       str(targets_following_user_info.follower_count),
                                                "Target's Following Following Count"    :       str(targets_following_user_info.following_count),
                                                "Target's Following Biography"          :       str(targets_following_user_info.biography),
                                                "Target's Following Email"              :       str(targets_following_user_info.public_email),
                                                "Target's Following Phone"              :       str(targets_following_user_info.contact_phone_number),
                                            })
            else:
                t = PrettyTable()
    
                t.field_names = ['Following ID', 'Following UserName', 'Following Name']
                t.align["Following ID"] = "l"
                t.align["Following UserName"] = "l"
                t.align["Following Name"] = "l"
                
                following_list = []
                
                for key in self.target_followings.keys():                    
                    t.add_row([
                                    str(self.target_followings[key].pk),
                                    str(self.target_followings[key].username), 
                                    str(self.target_followings[key].full_name),
                              ])
                    
                    if self.is_json:
                        following_list.append(
                                            {
                                                'Following ID'           :       str(self.target_followers[key].pk),
                                                'Following UserName'     :       str(self.target_followers[key].username),
                                                'Following Name'         :       str(self.target_followers[key].full_name),
                                            }
                                         )

            json_data = {}
            
            if self.is_file is True:                
                file_name = self.output_dir.joinpath(self.target + "_followings.txt")
                if file_name.exists():
                    file_name.unlink() 
                file = open(file_name, "w")
                file.write(str(t))
                file.close()

            if self.is_json is True:
                json_data['followings'] = following_list
                json_file_name = self.output_dir.joinpath(self.target + "_followings.json")
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