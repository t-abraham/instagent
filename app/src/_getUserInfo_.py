# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

from prettytable import PrettyTable

#%% __getUserInfo__

class __getUserInfo__(object):
    def __init__(self):
        super().__init__()
    def ___getUserInfo___(self):
        if self.target_user_info is None or self.target_id is None:
            self.___setTarget___()
        t = PrettyTable()

        t.field_names = [
            'Target ID', 
            'Target UserName', 
            'Target Name',
            'Target Private Profile',
            'Target Verified', 
            'Target Media Count', 
            'Target Follower Count',
            'Target Following Count',            
            'Target Biography',            
            'Target Email',            
            'Target Phone'
            ]
        t.align["Target ID"] = "l"
        t.align["Target UserName"] = "l"
        t.align["Target Name"] = "l"
        t.align["Target Private Profile"] = "l"
        t.align["Target Verified"] = "l"
        t.align["Target Media Count"] = "l"
        t.align["Target Follower Count"] = "l"
        t.align["Target Following Count"] = "l"
        t.align["Target Biography"] = "l"
        t.align["Target Email"] = "l"
        t.align["Target Phone"] = "l"
        
        self.___printout___("\nWoohoo! We found User information for: " + str(len(self.target)) + "\n", self.GREEN)
        
        t.add_row([
                        str(self.target_user_info.pk),
                        str(self.target_user_info.username),
                        str(self.target_user_info.full_name),
                        str(self.target_user_info.is_private),
                        str(self.target_user_info.is_verified),
                        str(self.target_user_info.media_count),
                        str(self.target_user_info.follower_count),
                        str(self.target_user_info.following_count),
                        str(self.target_user_info.biography),
                        str(self.target_user_info.public_email),
                        str(self.target_user_info.contact_phone_number),
                  ])
        print (t)
        
#%% Standalone Run

if __name__ == "__main__":
    pass