# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 10:31:57 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

import sys

#%% __storeMedias__

class __storeMedias__(object):
    def __init__(self):
        super().__init__()
    def ___storeMedias___(self, length=0, dwld_media_type="all"):
        if self.my_following or not self.target_is_private:
            if self.target_medias is None or (not length == 0 and not len(self.target_medias) == length):
                self.___getMedias___(length)
            
            if len(self.target_medias) > 0:
                specific_count = 0
                media_count = 0
                
                if dwld_media_type == "all":
                    media_count = len(self.target_medias)
                else:
                    for count, m in enumerate(self.target_medias):
                        if specific_count == length and not length == 0:
                            break
                                
                        if dwld_media_type.lower() == "photos":                        
                            if m.media_type == 1:
                                # Photo
                                media_count += 1
                                specific_count += 1
                                
                        elif dwld_media_type.lower() == "videos": 
                            if m.media_type == 2 and m.product_type == 'feed':
                                # Video
                                media_count += 1
                                specific_count += 1
                                
                        elif dwld_media_type.lower() == "igtvs": 
                            if m.media_type == 2 and m.product_type == 'igtv':
                                # IGTV
                                media_count += 1
                                specific_count += 1                        
                                
                        elif dwld_media_type.lower() == "reels":
                            if m.media_type == 2 and m.product_type == 'clips':
                                # Reels
                                media_count += 1
                                specific_count += 1                        
                                
                        elif dwld_media_type.lower() == "albums":    
                            if m.media_type == 8:
                                # Album
                                media_count += 1
                                specific_count += 1

                specific_count = 0
                self.___printout___("\nWoohoo! We found " + str(media_count) + " medias\n", self.GREEN)
                for count, m in enumerate(self.target_medias):
                    if specific_count == length and not length == 0:
                        break
                    
                    if dwld_media_type.lower() == "all":
                        if m.media_type == 1:
                            # Photo
                            self.api.photo_download(m.pk, self.output_dir)
                            specific_count += 1
                        elif m.media_type == 2 and m.product_type == 'feed':
                            # Video
                            self.api.video_download(m.pk, self.output_dir)
                            specific_count += 1
                        elif m.media_type == 2 and m.product_type == 'igtv':
                            # IGTV
                            self.api.video_download(m.pk, self.output_dir)
                            specific_count += 1
                        elif m.media_type == 2 and m.product_type == 'clips':
                            # Reels
                            self.api.video_download(m.pk, self.output_dir)
                            specific_count += 1
                        elif m.media_type == 8:
                            # Album
                            self.api.album_download(m.pk, self.output_dir)
                            specific_count += 1
                            
                    elif dwld_media_type.lower() == "photos":                        
                        if m.media_type == 1:
                            # Photo
                            self.api.photo_download(m.pk, self.output_dir)
                            specific_count += 1
                            
                    elif dwld_media_type.lower() == "videos": 
                        if m.media_type == 2 and m.product_type == 'feed':
                            # Video
                            self.api.video_download(m.pk, self.output_dir)
                            specific_count += 1
                            
                    elif dwld_media_type.lower() == "igtvs": 
                        if m.media_type == 2 and m.product_type == 'igtv':
                            # IGTV
                            self.api.video_download(m.pk, self.output_dir)
                            specific_count += 1                        
                            
                    elif dwld_media_type.lower() == "reels":
                        if m.media_type == 2 and m.product_type == 'clips':
                            # Reels
                            self.api.video_download(m.pk, self.output_dir)
                            specific_count += 1                        
                            
                    elif dwld_media_type.lower() == "albums":    
                        if m.media_type == 8:
                            # Album
                            self.api.album_download(m.pk, self.output_dir)
                            specific_count += 1
                            
                    sys.stdout.write("\rDownloaded {} of {}".format(specific_count, media_count))
                    sys.stdout.flush()
            else:
                self.___printout___("Sorry! No results found :-(\n", self.RED)
                

#%% Standalone Run

if __name__ == "__main__":
    pass