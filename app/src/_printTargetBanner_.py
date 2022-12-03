# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:48:17 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory


#%% __printTargetBanner__

class __printTargetBanner__(object):
    def __init__(self):
        super().__init__()
    def ___printTargetBanner___(self):
        self.___printout___("\nLogged as ", self.GREEN)
        self.___printout___(self.api.username, self.CYAN)
        self.___printout___(". Target: ", self.GREEN)
        self.___printout___(str(self.target), self.CYAN)
        self.___printout___(" [" + str(self.target_id) + "]")
        if self.target_is_private:
            self.___printout___(" [PRIVATE PROFILE]", self.BLUE)
        if self.my_following:
            self.___printout___(" [FOLLOWING]", self.GREEN)
        else:
            self.___printout___(" [NOT FOLLOWING]", self.RED)
    
        print('\n')

#%% Standalone Run    
if __name__ == "__main__":
    pass