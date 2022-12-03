# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable
from collections import Counter

#%% __getLikes__

class __getAllMediaCounts__(object):
    def __init__(self):
        super().__init__()
    def ___getAllMediaCounts___(self, length=0):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
            
            all_types = []
                        
            for count, m in enumerate(self.target_medias):
                if count == length and not length == 0:
                    break                
                
                if m.media_type == 1:
                    all_types.append("Photo")
                elif m.media_type == 2:
                    if m.product_type == "feed":
                        all_types.append("Video")
                    elif m.product_type == "igtv":
                        all_types.append("IGTV")
                    elif m.product_type == "clips":
                        all_types.append("Reel")
                elif m.media_type == 8:
                    all_types.append("Album")
                    
            all_media_counts = Counter(all_types)
                
            if len(all_media_counts) > 0:
                
                t = PrettyTable()
    
                t.field_names = ['Media Type', 'Counts']
                t.align["Media Type"] = "l"
                t.align["Counts"] = "l"
                self.___printout___("\nWoohoo! We found " + str(len(all_types)) + " medias\n", self.GREEN)
                
                hastags_list = []
                
                for key in all_media_counts.keys():
                    t.add_row([
                                str(key), 
                                str(all_media_counts[key]),
                             ])
                    
                    if self.is_json:
                        hastags_list.append(
                                                {
                                                    "Media Type"       :    str(key),
                                                    "Counts"     :    str(all_media_counts[key]),
                                                }
                                          )
                    
                json_data = {}            
                    
                if self.is_file is True:                
                    file_name = self.output_dir.joinpath(self.target + "_captions.txt")
                    if file_name.exists():
                        file_name.unlink() 
                    file = open(file_name, "w")
                    file.write(str(t))
                    file.close()
    
                if self.is_json is True:
                    json_data['media_counts'] = hastags_list
                    json_file_name = self.output_dir.joinpath(self.target + "_captions.json")
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