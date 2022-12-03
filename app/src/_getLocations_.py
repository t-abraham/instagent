# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import json
from prettytable import PrettyTable
from collections import OrderedDict

#%% __getLocations__

class __getLocations__(object):
    def __init__(self):
        super().__init__()
    def ___getLocations___(self, length=0):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
            locations = {}
            for count, m in enumerate(self.target_medias):
                if count == length and not length == 0:
                    break
                if not m.location is None:
                    if not m.location.lat is None and not m.location.lng is None:
                        details = self.geolocator.reverse("{}, {}".format(m.location.lat, m.location.lng))
                        locations[details.address] = {
                                                        "time"          :       m.taken_at.strftime('%Y-%m-%d %H:%M:%S'),
                                                        "media_ID"      :       str(m.pk),
                                                        "location"       :       str(details.address)
                                                    }
                    
            # sort_addresses = sorted(address.items(), key=lambda p: p["time"], reverse=True)
            sort_locations = OrderedDict(sorted(locations.items(), key=lambda i: i[1]['time']))
            
            if len(sort_locations) > 0:
                t = PrettyTable()

                t.field_names = ['Post ID', 'Post Time', 'Address']
                t.align["Post ID"] = "l"
                t.align["Post Time"] = "l"
                t.align["Address"] = "l"
                self.___printout___("\nWoohoo! We found " + str(len(sort_locations)) + " addresses\n", self.GREEN)

                i = 1

                json_data = {}
                location_list = []

                for key in sort_locations.keys():
                    t.add_row([
                                    str(sort_locations[key]["media_ID"]),
                                    str(sort_locations[key]["time"]), 
                                    str(sort_locations[key]["address"]), 
                              ])

                    if self.is_json:
                        location_list.append(
                                                {
                                                    'Address': str(sort_locations[key]["address"]),
                                                    'Time': str(sort_locations[key]["time"]),
                                                    'Media ID': str(sort_locations[key]["media ID"])
                                                }
                                            )

                    i = i + 1

                if self.is_file is True:                
                    file_name = self.output_dir.joinpath(self.target + "_locations.txt")
                    if file_name.exists():
                        file_name.unlink() 
                    file = open(file_name, "w")
                    file.write(str(t))
                    file.close()

                if self.is_json is True:
                    json_data['locations'] = location_list
                    json_file_name = self.output_dir.joinpath(self.target + "_locations.json")
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