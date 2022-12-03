# Commands list and usage
```
- FILE=y/n              Enable/disable output in a '<target username>_<command>.txt' file'
- JSON=y/n              Enable/disable export in a '<target username>_<command>.json' file'
- quit                  Quit/exit the system
- exit                  Quit/exit the system
- locations             Get all registered addressed by target photos
- cache                 Clear cache of the system
- comments              Get a list of all the comments on the target's each posts
- likes                 Get a list of count of likes for target's each posts
- captions              Get a list of captions for target's each posts
- followers             Get a list of followers for target's each posts
- followings            Get a list of users followed by the target for target's each posts
- detailedfollowers		Get a list of followers' details for target's each posts
- detailedfollowings	Get a list of users' details followed by the target for target's each posts
- hashtags              Get a list of hashtags used by the target
- hastagscounts         Get a count of hashtags used by the target
- info                  Get user information of the target
- mediacounts           Get a count of the total media posts by the target (photos, videos or reels)
- mediastore            Store the total media detected from the target locally in the system
- commenters            Get a list of users who commented on the target's posts
- tagged                Get a list of users tagged in the target's posts
- newtarget             Change target user
- timeout               Set a timeout in seconds for commands to execute
```

### FILE
Can set preference to save commands output in output folder. It save output in `<target username>_<command>.txt` file.

With `FILE=y` you can enable saving in file.

With `FILE=n` you can disable saving in file.

### JSON
Can set preference to export commands output as JSON in output folder. It save output in `<target username>_<command>.JSON` file.

With `JSON=y` you can enable JSON exporting.

With `JSON=n` you can disable JSON exporting.

### exit/quit
Exit from InstAgent.

### locations
Return a list with address (GPS) tagged by target in his photos.
The list has post, address and date fields.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: locations
For how many recent posts? (default 10):
```

### cache
Clear cache of the system for the given credentials.

### comments
Get a list of all the comments on the target's each posts.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: comments
For how many recent posts? (default 10):
```

### likes
Get a list of count of likes for target's each posts.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: likes
For how many recent posts? (default 10):
```

### captions
Get a list of captions for target's each posts.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: captions
For how many recent posts? (default 10):
```

### followers
Get a list of followers for target's each posts.

### followings
Get a list of users followed by the target for target's each posts.

### detailedfollowers
Get a list of followers' details for target's each posts.

### detailedfollowings
Get a list of users' details followed by the target for target's each posts.

### hashtags
Get a list of hashtags used by the target.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: hashtags
For how many recent posts? (default 10):
```

### hastagscounts
Get a count of hashtags used by the target.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: hastagscounts
For how many recent posts? (default 10):
```

### info
Show target info like:
- id
- full name
- biography
- followed
- follow
- is business account?
- business category (if target has business account)
- is verified?
- business email (if available)
- HD profile picture url
- connected Facebook page (if available)
- Whats'App number (if available)
- City Name (if available)
- Address Street (if available)
- Contact phone number (if available)

### mediacounts
Get a count of the total media posts by the target (photos, videos or reels).

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: mediacounts
For how many recent posts? (default 10):
```

### mediastore
Store the total media detected from the target locally in the system.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: mediastore
For how many recent posts? (default 10):
```

### commenters
Get a list of users who commented on the target's posts.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: commenters
For how many recent posts? (default 10):
```

### tagged
Get a list of users tagged in the target's posts.

When you run the command, script ask you how many recent media to be analysed for the action. 
Type 0 for all available medias or any positive number for the number of recent medias. 
```
Run a command: tagged
For how many recent posts? (default 10):
```

### newtarget
Change target user.

### timeout
Set a timeout in seconds for to wait for user input before taking the default value (if requested).
