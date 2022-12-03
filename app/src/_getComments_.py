# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable
from collections import Counter

#%% __getLocations__

class __getComments__(object):
    def __init__(self):
        super().__init__()
    def ___getComments___(self, length=0, users=False):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
                
            if self.target_comments is None or (not length == 0 and not len(self.target_comments) == length):
                self.target_comments = {}
                
            for count, m in enumerate(self.target_medias):
                if count == length and not length == 0:
                    break
                self.target_comments[m.pk] = []
                cmnts = self.api.media_comments(m.pk)
                for cmnt in cmnts:
                    
                    self.target_comments[m.pk].append(
                            {
                                "text"      :       cmnt.text,
                                "user"      :       cmnt.user.username,
                                "name"      :       cmnt.user.full_name,
                                "time"      :       cmnt.created_at_utc.strftime('%Y-%m-%d %H:%M:%S'),
                                "post_time" :       m.taken_at.strftime('%Y-%m-%d %H:%M:%S')
                            }
                        )
                self.target_comments[m.pk] = sorted(self.target_comments[m.pk], key=lambda p: p["time"], reverse=True)
                 
            if len(self.target_comments) > 0:
                
                if users is True:
                    json_key = "comments_users"
                    
                    all_users = [(cmnt["user"],cmnt["name"]) for pk in self.target_comments.keys() for cmnt in self.target_comments[pk]]
                    all_users = list(set(all_users))
                    cmnt_users = {}
                    
                    for pk in self.target_comments.keys():
                        cmnt_users[pk] = []
                        for cmnt in self.target_comments[pk]:                            
                            cmnt_users[pk].append(all_users[[x for x, y in enumerate(all_users) if y[0] == cmnt["user"]][0]])
                        cmnt_users[pk] = Counter(cmnt_users[pk])
                    
                    t = PrettyTable()
    
                    t.field_names = ['Post ID', 'Commented User ID', 'Commented User Name', 'Comment Counts']
                    t.align["Post ID"] = "l"
                    t.align["Commented User ID"] = "l"
                    t.align["Commented User Name"] = "l"
                    t.align["Comment Counts"] = "l"
                    self.___printout___("\nWoohoo! We found " + str(len(all_users)) + " commented users\n", self.GREEN)
    
                    comments_list = []
                    
                    for pk in cmnt_users.keys():
                        for user_id, user_name in cmnt_users[pk]:
                            t.add_row([
                                            str(pk), 
                                            user_id, 
                                            user_name, 
                                            cmnt_users[pk][(user_id, user_name)],
                                      ])
                            
                            if self.is_json:
                                comments_list.append(
                                                        {
                                                            "Post ID": str(pk),
                                                            "Commented User ID": user_id,
                                                            "Commented User Name": user_name,
                                                            "Comment Counts": cmnt_users[pk][(user_id, user_name)],
                                                        }
                                                    )
                else:
                    json_key = "comments"
                    total_comments = sum(len(all_comments) for all_comments in self.target_comments.values())
                    t = PrettyTable()
    
                    t.field_names = ['Post ID', 'Post Time', 'Comment', 'User', 'Full Name', 'time']
                    t.align["Post ID"] = "l"
                    t.align["Post Time"] = "l"
                    t.align["Comment"] = "l"
                    t.align["User"] = "l"
                    t.align["Full Name"] = "l"
                    t.align["Time"] = "l"
                    self.___printout___("\nWoohoo! We found " + str(total_comments) + " comments\n", self.GREEN)
    
                    comments_list = []
    
                    for pk in self.target_comments.keys():
                        for cmnt in self.target_comments[pk]:                    
                            t.add_row([
                                            str(pk), 
                                            cmnt["post_time"], 
                                            cmnt["text"], 
                                            cmnt["user"], 
                                            cmnt["name"], 
                                            cmnt["time"],
                                      ])
    
                        if self.is_json:
                            comments_list.append(
                                                    {
                                                        "Post ID": str(pk),
                                                        "Post Time": cmnt["post_time"],
                                                        "Comment": cmnt["text"],
                                                        "User": cmnt["user"],
                                                        "Full Name": cmnt["name"],
                                                        "Time": cmnt["time"],
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
                    json_data[json_key] = comments_list
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