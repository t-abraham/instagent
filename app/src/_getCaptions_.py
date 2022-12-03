# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable

#%% __getLikes__

class __getCaptions__(object):
    def __init__(self):
        super().__init__()
    def ___getCaptions___(self, length=0):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
            
            captions = {}
            for count, m in enumerate(self.target_medias):
                if count == length and not length == 0:
                    break
                
                if not m.caption_text is None:
                    captions[m.pk] = {
                                        "time"         :       m.taken_at.strftime('%Y-%m-%d %H:%M:%S'),
                                        "media_ID"     :       str(m.pk),
                                        "caption"      :       str(m.caption_text)
                                    }
                
            if len(captions) > 0:
                t = PrettyTable()

                t.field_names = ['Post ID', 'Post Time', 'Caption']
                t.align["Post ID"] = "l"
                t.align["Post Time"] = "l"
                t.align["Caption"] = "l"
                self.___printout___("\nWoohoo! We found " + str(len(captions)) + " posts with captions\n", self.GREEN)
                
                json_data = {}
                captions_list = []
                
                for key in captions.keys():
                    t.add_row([
                                str(captions[key]["media_ID"]), 
                                str(captions[key]["time"]), 
                                str(captions[key]["caption"]),
                             ])
                    
                    if self.is_json:
                        captions_list.append(
                                                {
                                                    "Post ID"       :    str(captions[key]["media_ID"]),
                                                    "Post Time"     :    str(captions[key]["time"]),
                                                    "Like Counts"   :    str(captions[key]["caption"]),
                                                }
                                          )
                if self.is_file is True:                
                    file_name = self.output_dir.joinpath(self.target + "_captions.txt")
                    if file_name.exists():
                        file_name.unlink() 
                    file = open(file_name, "w")
                    file.write(str(t))
                    file.close()

                if self.is_json is True:
                    json_data['captions'] = captions_list
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