#!/usr/bin/env python3

from src.instagent import instagent
import argparse
import sys
import signal
import os
from pathlib import Path 
from prettytable import PrettyTable

def cmdlist():
    global api
    
    t = PrettyTable()
    
    t.field_names = ['Command', 'Action']
    t.align["Command"] = "l"
    t.align["Action"] = "l"
    
    printcmdlist = {
        "FILE=y/n"              :   "Enable/disable output in a '<target username>_<command>.txt' file'",
        "JSON=y/n"              :   "Enable/disable export in a '<target username>_<command>.json' file'",
        "quit"                  :   "Quit/exit the system",
        "exit"                  :   "Quit/exit the system",
        "locations"             :   "Get all registered addressed by target photos",
        "cache"                 :   "Clear cache of the system",
        "comments"              :   "Get a list of all the comments on the target's each posts",
        "likes"                 :   "Get a list of count of likes for target's each posts",
        "captions"              :   "Get a list of captions for target's each posts",
        'followers'             :   "Get a list of followers for target's each posts",
        'followings'            :   "Get a list of users followed by the target for target's each posts",        
        'detailedfollowers'     :   "Get a list of followers' details for target's each posts",
        'detailedfollowings'    :   "Get a list of users' details followed by the target for target's each posts" ,
        'hastags'               :   "Get a list of hashtags used by the target" ,
        'hastagscounts'         :   "Get a count of hashtags used by the target",
        'info'                  :   "Get user information of the target", 
        'mediacounts'           :   "Get a count of the total media posts by the target (photos, videos or reels)",
        'mediastore'            :   "Store the total media detected from the target locally in the system",
        'commenters'            :   "Get a list of users who commented on the target's posts",
        'tagged'                :   "Get a list of users tagged in the target's posts",
        'newtarget'             :   "Change target user",
        'timeout'               :   "Set a timeout in seconds for to wait for user input before taking the default value",
    }
    
    
    for key in printcmdlist.keys():
        t.add_row([
                    key, 
                    printcmdlist[key], 
                 ])
        
    print (t)

def signal_handler(sig, frame):
    global api
    
    api.___printout___("\nGoodbye!\n", api.RED)
    sys.exit(0)


def completer(text, state):
    global commands
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def _quit():
    global api
    
    api.___printout___("Goodbye!\n", api.RED)
    sys.exit(0)

def api_process(parms, readliner):
    global commands    
    global api

    api.initialize( parms.identity, 
                    parms.defaultcount,
                    parms.defaultmedia,
                    parms.proxy,
                    parms.cookies,
                    parms.file, 
                    parms.json, 
                    parms.command, 
                    parms.output, 
                    parms.timeout,
                    Path(__file__).parent.resolve()
                  )

    commands = {
        'list'                  :   cmdlist,
        'help'                  :   cmdlist,
        'quit'                  :   _quit,
        'exit'                  :   _quit,
        'locations'             :   api.get_locations,
        'cache'                 :   api.clear_cache,
        'comments'              :   api.get_comments,
        'likes'                 :   api.get_likes,
        'captions'              :   api.get_captions,
        'followers'             :   api.get_followers,
        'followings'            :   api.get_followings,        
        'detailedfollowers'     :   api.get_followers_detailed,
        'detailedfollowings'    :   api.get_followings_detailed,
        'hastags'               :   api.get_hashtags,
        'hastagscounts'         :   api.get_hashtags_counts,        
        'info'                  :   api.get_user_info,
        'mediacounts'           :   api.get_all_media_counts,
        'mediastore'            :   api.store_media,
        'commenters'            :   api.get_people_who_commented,
        'tagged'                :   api.get_people_who_tagged,
        'newtarget'             :   api.change_target,
        'timeout'               :   api.set_timeout,
    }


    signal.signal(signal.SIGINT, signal_handler)
    readliner.parse_and_bind("tab: complete")
    readliner.set_completer(completer)

    if not parms.command:
        api.printlogo()

    while True:
        if parms.command:
            cmd = parms.command
            _cmd = commands.get(parms.command)
        else:
            signal.signal(signal.SIGINT, signal_handler)
            readliner.parse_and_bind("tab: complete")
            readliner.set_completer(completer)
            api.___printout___("Run a command: ", api.YELLOW)
            cmd = api.___userInput___(
                                        answers=commands.keys(),
                                        timeout=-1
                                      )

            _cmd = commands.get(cmd)
        
        if _cmd:
            _cmd()
        elif cmd == "FILE=y":
            api.set_is_file(True)
        elif cmd == "FILE=n":
            api.set_is_file(False)
        elif cmd == "JSON=y":
            api.set_is_json(True)
        elif cmd == "JSON=n":
            api.set_is_json(False)
        elif cmd == "":
            print("")
        else:
            api.___printout___("Unknown command\n", api.RED)

        if parms.command:
            break

class parameters():
    identity = None
    cookies = None
    json = None
    file = None
    command = None
    output = None
    multi = None
    timeout = None
    defaultcount = None
    defaultmedia = None
    proxy = None

if __name__ == "__main__":
    api = instagent()       
 
    parms = parameters()
    parser = argparse.ArgumentParser(description='Osintgram is a OSINT tool on Instagram. It offers an interactive shell '
                                                 'to perform analysis on Instagram account of any users by its nickname ')
    parser.add_argument('identity', type=str, nargs='?', help='username')
    parser.add_argument('-C','--cookies', help='clear\'s previous cookies', action="store_true")
    parser.add_argument('-j', '--json', help='save commands output as JSON file', action='store_true')
    parser.add_argument('-f', '--file', help='save output in a file', action='store_true')
    parser.add_argument('-c', '--command', help='run in single command mode & execute provided command', action='store')
    parser.add_argument('-o', '--output', help='where to store photos', action='store')
    parser.add_argument('-m', '--multi', help='multi targets', action='store_true')
    parser.add_argument('-t', '--timeout', help='input timeout in seconds', action='store')
    parser.add_argument('-dc', '--defaultcount', help='defualt media counts for commands', action='store')
    parser.add_argument('-dm', '--defaultmedia', help='defualt media type for commands', action='store')
    parser.add_argument('-p', '--proxy', help='proxy for the app (example: http://username:password@147.123123.123:412345)', action='store')
    
    args = parser.parse_args()
    
    parms.identity = os.environ.get("INSTAGENT_IDENTITY", args.identity)
    parms.cookies = os.environ.get("INSTAGENT_COOKIES", args.cookies)
    parms.json = os.environ.get("INSTAGENT_JSON", args.json)
    parms.file = os.environ.get("INSTAGENT_FILE", args.file)
    parms.command = os.environ.get("INSTAGENT_COMMAND", args.command)
    parms.output = os.environ.get("INSTAGENT_OUTPUT", args.output)
    parms.multi = os.environ.get("INSTAGENT_MULTI", args.multi)
    parms.timeout = os.environ.get("INSTAGENT_TIMEOUT", args.timeout)
    parms.defaultcount = os.environ.get("INSTAGENT_DEFAULTCOUNT", args.defaultcount)
    parms.defaultmedia = os.environ.get("INSTAGENT_DEFAULTMEDIA", args.defaultmedia)
    parms.proxy = os.environ.get("INSTAGENT_PROXY", args.proxy)
    
    if os.name == 'nt':
        from pyreadline3 import Readline
        readliner = Readline()
        api.___printout___("Windows Detected!\n", api.RED)
    else:
        import gnureadline
        readliner = gnureadline    
        api.___printout___("Linux Detected!\n", api.RED)
    
    if parms.multi:
        if parms.command:
            try:
                targets_dir = Path(__file__).parent.resolve().joinpath("config")
                targets = targets_dir.joinpath("targets.ini")
                data = [line.strip() for line in open(targets, 'r') if not line.strip()[0] == "#"]
                data = sorted(list(set(data)))
                targets.unlink()
                targets_dir.mkdir(parents=True, exist_ok=True)
                with open(targets, 'w') as file:
                    file.write("\n".join(str(item) for item in data))
                
            except FileNotFoundError:
                api.___printout___('Error: file "config/targets.ini" not found!\n', api.RED)
                sys.exit(0)
            except Exception as e:
                api.___printout___("Error: {}\n".format(e), api.RED)
                sys.exit(0)
                
            for target in data:
                api.___printout___("*************************************************************************\n", api.GREEN)            
                api.___printout___("Target: {}\n".format(target), api.GREEN)            
                api.___printout___("*************************************************************************\n", api.GREEN)
                parms.identity = target
                api_process(parms, readliner)
            api.___printout___("All targets completed!\n", api.RED)    
            api.___printout___("Goodbye!\n", api.RED)
        else:
            api.___printout___('Error: To use Multi Target (-m), a fixed Command (-c) needs to be passed too!\n', api.RED)
            sys.exit(0)
    else:
        api_process(parms, readliner)
