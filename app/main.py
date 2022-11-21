#!/usr/bin/env python3

from src.instagent import instagent
import argparse
from src import printcolors as pc
from src import artwork
import sys
import signal
import os
from pathlib import Path 

def printlogo():
    pc.printout(artwork.ascii_art, pc.YELLOW)
    pc.printout("\nVersion 1.0 - Developed by Tahasanul Abraham\n\n", pc.YELLOW)
    pc.printout("Type 'list' to show all allowed commands\n")
    pc.printout("Type 'FILE=y' to save results to files like '<target username>_<command>.txt (default is disabled)'\n")
    pc.printout("Type 'FILE=n' to disable saving to files'\n")
    pc.printout("Type 'JSON=y' to export results to a JSON files like '<target username>_<command>.json (default is "
                "disabled)'\n")
    pc.printout("Type 'JSON=n' to disable exporting to files'\n")


def cmdlist():
    pc.printout("FILE=y/n\t")
    print("Enable/disable output in a '<target username>_<command>.txt' file'")
    pc.printout("JSON=y/n\t")
    print("Enable/disable export in a '<target username>_<command>.json' file'")
    pc.printout("addrs\t\t")
    print("Get all registered addressed by target photos")
    pc.printout("cache\t\t")
    print("Clear cache of the tool")
    pc.printout("captions\t")
    print("Get target's photos captions")
    pc.printout("commentdata\t")
    print("Get a list of all the comments on the target's posts")
    pc.printout("comments\t")
    print("Get total comments of target's posts")
    pc.printout("followers\t")
    print("Get target followers")
    pc.printout("followings\t")
    print("Get users followed by target")
    pc.printout("fwersemail\t")
    print("Get email of target followers")
    pc.printout("fwingsemail\t")
    print("Get email of users followed by target")
    pc.printout("fwersnumber\t")
    print("Get phone number of target followers")
    pc.printout("fwingsnumber\t")
    print("Get phone number of users followed by target")    
    pc.printout("hashtags\t")
    print("Get hashtags used by target")
    pc.printout("info\t\t")
    print("Get target info")
    pc.printout("likes\t\t")
    print("Get total likes of target's posts")
    pc.printout("mediatype\t")
    print("Get target's posts type (photo or video)")
    pc.printout("photodes\t")
    print("Get description of target's photos")
    pc.printout("photos\t\t")
    print("Download target's photos in output folder")
    pc.printout("propic\t\t")
    print("Download target's profile picture")
    pc.printout("stories\t\t")
    print("Download target's stories")
    pc.printout("tagged\t\t")
    print("Get list of users tagged by target")
    pc.printout("target\t\t")
    print("Set new target")
    pc.printout("wcommented\t")
    print("Get a list of user who commented target's photos")
    pc.printout("wtagged\t\t")
    print("Get a list of user who tagged target")
    pc.printout("timeout\t\t")
    print("Set input timeout in seconds")


def signal_handler(sig, frame):
    pc.printout("\nGoodbye!\n", pc.RED)
    sys.exit(0)


def completer(text, state):
    global commands
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def _quit():
    pc.printout("Goodbye!\n", pc.RED)
    sys.exit(0)

def api_process(parms):
    global commands
    
    if os.name == 'nt':
        from pyreadline3 import Readline
        readliner = Readline()
        pc.printout("Windows Detected!\n", pc.RED)
    else:
        import gnureadline
        readliner = gnureadline    
        pc.printout("Linux Detected!\n", pc.RED)
    
    api = instagent(parms.identity, 
                    parms.file, 
                    parms.json, 
                    parms.command, 
                    parms.output, 
                    parms.cookies, 
                    parms.timeout,
                    Path(__file__).parent.resolve()
                    )

    commands = {
        'list':             cmdlist,
        'help':             cmdlist,
        'quit':             _quit,
        'exit':             _quit,
        'addrs':            api.get_addrs,
        'cache':            api.clear_cache,
        'captions':         api.get_captions,
        "commentdata":      api.get_comment_data,
        'comments':         api.get_total_comments,
        'followers':        api.get_followers,
        'followings':       api.get_followings,
        'fwersemail':       api.get_fwersemail,
        'fwingsemail':      api.get_fwingsemail,
        'fwersnumber':      api.get_fwersnumber,
        'fwingsnumber':     api.get_fwingsnumber,
        'hashtags':         api.get_hashtags,
        'info':             api.get_user_info,
        'likes':            api.get_total_likes,
        'mediatype':        api.get_media_type,
        'photodes':         api.get_photo_description,
        'photos':           api.get_user_photo,
        'propic':           api.get_user_propic,
        'stories':          api.get_user_stories,
        'tagged':           api.get_people_tagged_by_user,
        'target':           api.change_target,
        'wcommented':       api.get_people_who_commented,
        'wtagged':          api.get_people_who_tagged,
        'timeout':          api.set_timeout,
    }


    signal.signal(signal.SIGINT, signal_handler)
    readliner.parse_and_bind("tab: complete")
    readliner.set_completer(completer)
    

    if not parms.command:
        printlogo()

    while True:
        if parms.command:
            cmd = parms.command
            _cmd = commands.get(parms.command)
        else:
            signal.signal(signal.SIGINT, signal_handler)
            readliner.parse_and_bind("tab: complete")
            readliner.set_completer(completer)
            pc.printout("Run a command: ", pc.YELLOW)
            cmd = input()

            _cmd = commands.get(cmd)

        if _cmd:
            _cmd()
        elif cmd == "FILE=y":
            api.set_write_file(True)
        elif cmd == "FILE=n":
            api.set_write_file(False)
        elif cmd == "JSON=y":
            api.set_json_dump(True)
        elif cmd == "JSON=n":
            api.set_json_dump(False)
        elif cmd == "":
            print("")
        else:
            pc.printout("Unknown command\n", pc.RED)

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

if __name__ == "__main__":       
 
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
    
    args = parser.parse_args()
    
    parms.identity = os.environ.get("INSTAGENT_IDENTITY", args.identity)
    parms.cookies = os.environ.get("INSTAGENT_COOKIES", args.cookies)
    parms.json = os.environ.get("INSTAGENT_JSON", args.json)
    parms.file = os.environ.get("INSTAGENT_FILE", args.file)
    parms.command = os.environ.get("INSTAGENT_COMMAND", args.command)
    parms.output = os.environ.get("INSTAGENT_OUTPUT", args.output)
    parms.multi = os.environ.get("INSTAGENT_MULTI", args.multi)
    parms.timeout = os.environ.get("INSTAGENT_TIMEOUT", args.timeout)
    
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
                pc.printout('Error: file "config/targets.ini" not found!\n', pc.RED)
                sys.exit(0)
            except Exception as e:
                pc.printout("Error: {}\n".format(e), pc.RED)
                sys.exit(0)
                
            for target in data:
                pc.printout("*************************************************************************\n", pc.GREEN)            
                pc.printout("Target: {}\n".format(target), pc.GREEN)            
                pc.printout("*************************************************************************\n", pc.GREEN)
                parms.identity = target
                api_process(parms)
            pc.printout("All targets completed!\n", pc.RED)    
            pc.printout("Goodbye!\n", pc.RED)
        else:
            pc.printout('Error: To use Multi Target (-m), a fixed Command (-c) needs to be passed too!\n', pc.RED)
            sys.exit(0)
    else:
        api_process(parms)
