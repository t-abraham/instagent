# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable

#%% __getLikes__

class __getLikes__(object):
    def __init__(self):
        super().__init__()
    def ___getLikes___(self, length=0):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
            
            likes = {}
            for count, m in enumerate(self.target_medias):
                if count == length and not length == 0:
                    break
                likes[m.pk] = {
                                    "time"          :       m.taken_at.strftime('%Y-%m-%d %H:%M:%S'),
                                    "media_ID"      :       str(m.pk),
                                    "likes_counts"       :       str(m.like_count)
                                }
                
            if len(likes) > 0:
                t = PrettyTable()

                t.field_names = ['Post ID', 'Post Time', 'Like Counts']
                t.align["Post ID"] = "l"
                t.align["Post Time"] = "l"
                t.align["Like Counts"] = "l"
                self.___printout___("\nWoohoo! We found " + str(likes) + " posts with likes\n", self.GREEN)
                
                json_data = {}
                likes_list = []
                
                for key in likes.keys():
                    t.add_row([
                                str(likes[key]["media_ID"]), 
                                str(likes[key]["time"]), 
                                str(likes[key]["likes_counts"]),
                             ])
                    
                    if self.is_json:
                        likes_list.append(
                                                {
                                                    "Post ID"       :    str(likes[key]["media_ID"]),
                                                    "Post Time"     :    str(likes[key]["time"]),
                                                    "Like Counts"   :    str(likes[key]["likes_counts"]),
                                                }
                                          )
                if self.is_file is True:                
                    file_name = self.output_dir.joinpath(self.target + "_comments.txt")
                    if file_name.exists():
                        file_name.unlink() 
                    file = open(file_name, "w")
                    file.write(str(t))
                    file.close()

                if self.is_json is True:
                    json_data['likes_counts'] = likes_list
                    json_file_name = self.output_dir.joinpath(self.target + "_comments.json")
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