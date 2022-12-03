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

class __getTags__(object):
    def __init__(self):
        super().__init__()
    def ___getTags___(self, length=0, tag_type="#", counts=False):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
            
            if tag_type == "#":
                tag_key = "hastags"
            elif tag_type == "@":
                tag_key = "usertags"
            else:
                tag_key = "tags"
            
            alltags = {}
            for count, m in enumerate(self.target_medias):
                if count == length and not length == 0:
                    break                
                tag = [tag for tag in str(m.caption_text).split() if tag.startswith(tag_type)]
                
                if len(tag) > 0:
                    alltags[m.pk] = {
                                        "time"         :       m.taken_at.strftime('%Y-%m-%d %H:%M:%S'),
                                        "media_ID"     :       str(m.pk),
                                        tag_key        :       tag
                                    }
                
            if len(alltags) > 0:
                
                if counts is True:
                    
                    json_key = "{}_counts".format(tag_key)
                    all_hashtags = []
                    for key in alltags.keys():
                        all_hashtags = all_hashtags + alltags[key][tag_key]
                    
                    all_hashtags_counts = Counter(all_hashtags)
                    
                    t = PrettyTable()
    
                    t.field_names = [tag_key.capitalize(), 'Counts']
                    t.align[tag_key.capitalize()] = "l"
                    t.align["Counts"] = "l"
                    self.___printout___("\nWoohoo! We found {} {} \n".format(len(all_hashtags), tag_key), self.GREEN)
                    
                    tags_list = []
                    
                    for key in all_hashtags_counts.keys():
                        t.add_row([
                                    str(key), 
                                    str(all_hashtags_counts[key]),
                                 ])
                        
                        if self.is_json:
                            tags_list.append(
                                                    {
                                                        tag_key.capitalize()    :    str(key),
                                                        "Counts"                :    str(all_hashtags_counts[key]),
                                                    }
                                              )
                    
                else:
                    
                    json_key = "{}".format(tag_key)
                    t = PrettyTable()
    
                    t.field_names = ['Post ID', 'Post Time', tag_key.capitalize()]
                    t.align["Post ID"] = "l"
                    t.align["Post Time"] = "l"
                    t.align[tag_key.capitalize()] = "l"
                    self.___printout___("\nWoohoo! We found {} posts with {} \n".format(len(alltags), tag_key), self.GREEN)
                    
                    tags_list = []
                    
                    for key in alltags.keys():
                        t.add_row([
                                    str(alltags[key]["media_ID"]), 
                                    str(alltags[key]["time"]), 
                                    str(alltags[key][tag_key]),
                                 ])
                        
                        if self.is_json:
                            tags_list.append(
                                                    {
                                                        "Post ID"               :    str(alltags[key]["media_ID"]),
                                                        "Post Time"             :    str(alltags[key]["time"]),
                                                        tag_key.capitalize()    :    str(alltags[key][tag_key]),
                                                    }
                                              )
                
                json_data = {}            
                
                if self.is_file is True:                
                    file_name = self.output_dir.joinpath(self.target + "_{}.txt".format(json_key))
                    if file_name.exists():
                        file_name.unlink() 
                    file = open(file_name, "w")
                    file.write(str(t))
                    file.close()

                if self.is_json is True:
                    json_data[json_key] = tags_list
                    json_file_name = self.output_dir.joinpath(self.target + "_{}.json".format(json_key))
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