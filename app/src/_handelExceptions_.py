# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:22:46 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

from instagrapi.exceptions import (
    BadPassword,
    ChallengeRequired,
    FeedbackRequired,
    LoginRequired,
    PleaseWaitFewMinutes,
    RecaptchaChallengeForm,
    ReloginAttemptExceeded,
    SelectContactPointRecoveryForm,
)

#%% __handelExceptions__

class __handelExceptions__(object):
    def __init__(self):
        super().__init__()
    
    def ___handelExceptions___(self, client, e):
        if isinstance(e, BadPassword):
            self.api.logger.exception(e)
            if self.api.relogin_attempt > 0:
                raise ReloginAttemptExceeded(e)
            self.___printout___("Please re-enter your account's username':\n", self.RED)
            self.username = self.___userInput___()
            self.api.username = self.username
            self.___printout___("Please re-enter your account's password':\n", self.RED)
            self.password = self.___userInput___()
            self.api.password = self.password
            self.___updateCredentials___()
            if not self.proxy is None:
                self.api.set_proxy(self.proxy)
            self.api.relogin()
            settings_file = self.main_dir.joinpath("config","{}.json".format(self.username))
            self.api.dump_settings(settings_file)
            
            return True
            
        elif isinstance(e, LoginRequired):
            self.api.logger.exception(e)
            self.api.relogin()
            settings_file = self.main_dir.joinpath("config","{}.json".format(self.username))
            self.api.dump_settings(settings_file)
            
            return True
            
        elif isinstance(e, ChallengeRequired):
            api_path = self.api.last_json.get("challenge", {}).get("api_path")
            if api_path == "/challenge/":
                if not self.proxy is None:
                    self.api.set_proxy(self.proxy)
                    self.api.relogin()
                    settings_file = self.main_dir.joinpath("config","{}.json".format(self.username))
                    self.api.dump_settings(settings_file)
            else:
                try:
                    self.api.challenge_resolve(self.api.last_json)
                    self.api.relogin()
                    settings_file = self.main_dir.joinpath("config","{}.json".format(self.username))
                    self.api.dump_settings(settings_file)
                except ChallengeRequired as e:
                    self.___printout___('\nManual Challenge Required\n', self.RED)
                    raise e
                except (ChallengeRequired, SelectContactPointRecoveryForm, RecaptchaChallengeForm) as e:
                    self.___printout___('Error: {}'.format(e), self.RED)
                    raise e
                    
            return True
        
        elif isinstance(e, FeedbackRequired):
            message = self.api.last_json["feedback_message"]
            if "This action was blocked. Please try again later" in message:
                self.___printout___('Feedback Required: {}'.format(message), self.RED)
                # client.settings = self.rebuild_client_settings()
                # return self.update_client_settings(client.get_settings())
            elif "We restrict certain activity to protect our community" in message:
                # 6 hours is not enough
                self.___printout___('Feedback Required: {}'.format(message), self.RED)
            elif "Your account has been temporarily blocked" in message:
                """
                Based on previous use of this feature, your account has been temporarily
                blocked from taking this action.
                This block will expire on 2020-03-27.
                """
                self.___printout___('Feedback Required: {}'.format(message), self.RED)
        elif isinstance(e, PleaseWaitFewMinutes):
            self.___printout___('Waiting: {}'.format(e), self.RED)
        raise e
        
#%% Standalone Run

if __name__ == "__main__":
    pass