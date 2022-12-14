# InstAgent 🔎📸

InstAgent is a tool on Instagram to collect, analyze, and run reconnaissance. 

The original idea is from [Datalux](https://github.com/Datalux).

Since the [original version](https://github.com/Datalux/Osintgram) is more or less inactive, I took the initiative to continue with the developments.

<p align="center">
<img align="center" src=".img/carbon.png" width="900">
</p>

Disclaimer: **FOR EDUCATIONAL PURPOSE ONLY! The contributors do not assume any responsibility for the use of this tool.**

Warning: It is advisable to **not** use your own/primary account when using this tool.

## Tools and Commands 🧰

InstAgent offers an interactive shell to perform analysis on Instagram account of any users by its nickname. You can get:

<p align="center">
<img align="center" src=".img/commands.png" width="900">
</p>


You can find detailed commands usage [here](doc/COMMANDS.md).

[Commands](doc/COMMANDS.md) |
[CHANGELOG](doc/CHANGELOG.md)

## FAQ
1. **Can I access the contents of a private profile?** No, you cannot get information on private profiles. You can only get information from a public profile or a profile you follow. The tools that claim to be successful are scams!
2. **What is and how I can bypass the `challenge_required` error?** The `challenge_required` error means that Instagram notice a suspicious behavior on your profile, so needs to check if you are a real person or a bot. To avoid this you should follow the suggested link and complete the required operation (insert a code, confirm email, etc)


## Installation ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/t-abraham/instagent.git`

2. Navigate to the directory

    `cd instagent`

3. Create a virtual environment for this project

    `python3 -m venv venv`

4. Load the virtual environment
   - On Windows Powershell: `.\venv\Scripts\activate.ps1`
   - On Linux and Git Bash: `source ./venv/bin/activate`
  
5. Run 
   - On Windows Powershell: `pip install -r .\app\requirements.txt`
   - On Linux and Git Bash: `pip install -r ./app/requirements.txt`

6. Setting up the application
    * Main user credentials (please do not use your original Account)
       - Open the `credentials.ini` file in the `app -> config` folder and write your account username and password in the corresponding fields
    * (If you wish to do reconnaissance on multiple targets)
       - Open the `targets.ini` file in the `app -> config` folder and write your target accounts' usernames per line.
       <p align="center">
           <img align="center" src=".img/multi_targets.png" width="900">
       </p>

7. Run the main.py script in one of two ways

    * As an interactive prompt
       - On Windows Powershell: `python3 .\app\main.py <target username>`
       - On Linux and Git Bash: `python3 ./app/main.py <target username>`
    * Or execute your command straight away
       - On Windows Powershell: `python3 .\app\main.py <target username> --command <command>`
       - On Linux and Git Bash: `python3 ./app/main.py <target username> --command <command>`
       
8. Possible running aruguments (multiple arguments can be executed with a space " " inbetween):
    *  On Windows Powershell:
       - Target User: `python3 .\app\main.py <target username>`
       - Login with new cookies: `python3 .\app\main.py -C`
       - Enable auto JSON file saving: `python3 .\app\main.py -j`
       - Enable auto TXT file saving: `python3 .\app\main.py -f`
       - Auto Perform Command: `python3 .\app\main.py -c <command>`
       - Custom Output Directory: `python3 .\app\main.py -o <output path>`
       - Use of Multiple Targets: `python3 .\app\main.py -m`
       - User Input timeout before taking default value: `python3 .\app\main.py -t <time in seconds>`   
       - Default media counts for any commands: `python3 .\app\main.py -dc <number>`
       - Default media types for any commands: `python3 .\app\main.py -dm <number>`
       - Proxy settings: `python3 .\app\main.py -p <proxy url (http://username:password@147.123123.123:412345)>`
    *  On Linux and Git Bash:
       - Target User: `python3 ./app/main.py <target username>`
       - Login with new cookies: `python3 ./app/main.py -C`
       - Enable auto JSON file saving: `python3 ./app/main.py -j`
       - Enable auto TXT file saving: `python3 ./app/main.py -f`
       - Auto Perform Command: `python3 ./app/main.py -c <command>`
       - Custom Output Directory: `python3 ./app/main.py -o <output path>`
       - Use of Multiple Targets: `python3 ./app/main.py -m`
       - User Input timeout before taking default value: `python3 ./app/main.py -t <time in seconds>` 
       - Default media counts for any commands: `python3 ./app/main.py -dc <number>`
       - Default media types for any commands: `python3 ./app/main.py -dm <number>`
       - Proxy settings: `python3 ./app/main.py -p <proxy url (http://username:password@147.123123.123:412345)>`

## Docker Quick Start 🐳

This section will explain how you can quickly use this image with `Docker` or `Docker-compose`.

### Coming Soon
<!---
### Prerequisites

Before you can use either `Docker` or `Docker-compose`, please ensure you do have the following prerequisites met.

1. **Docker** installed - [link](https://docs.docker.com/get-docker/)
2. **Docker-composed** installed (if using Docker-compose) - [link](https://docs.docker.com/compose/install/)
3. **Credentials** configured - This can be done manually or by running the `make setup` command from the root of this repo

**Important**: Your container will fail if you do not do step #3 and configure your credentials

### Docker

If docker is installed you can build an image and run this as a container.

Build:

```bash
docker build -t instagent .
```

Run:

```bash
docker run --rm -it -v "./output:/home/app/output" InstAgent <target>
```

- The `<target>` is the Instagram account you wish to use as your target for recon.
- The required `-i` flag enables an interactive terminal to use commands within the container. [docs](https://docs.docker.com/engine/reference/commandline/run/#assign-name-and-allocate-pseudo-tty---name--it)
- The required `-v` flag mounts a volume between your local filesystem and the container to save to the `./output/` folder. [docs](https://docs.docker.com/engine/reference/commandline/run/#mount-volume--v---read-only)
- The optional `--rm` flag removes the container filesystem on completion to prevent cruft build-up. [docs](https://docs.docker.com/engine/reference/run/#clean-up---rm)
- The optional `-t` flag allocates a pseudo-TTY which allows colored output. [docs](https://docs.docker.com/engine/reference/run/#foreground)

### Using `docker-compose`

You can use the `docker-compose.yml` file this single command:

```bash
docker-compose run instagent <target>
```

Where `target` is the Instagram target for recon.

Alternatively you may run `docker-compose` with the `Makefile`:

`make run` - Builds and Runs with compose. Prompts for a `target` before running.

### Makefile (easy mode)

For ease of use with Docker-compose, a `Makefile` has been provided.

Here is a sample work flow to spin up a container and run `instagent` with just two commands!

1. `make setup`   - Sets up your Instagram credentials
2. `make run`     - Builds and Runs a InstAgent container and prompts for a target

Sample workflow for development:

1. `make setup`                 - Sets up your Instagram credentials
2. `make build-run-testing`     - Builds an Runs a container without invoking the `app/main.py` script. Useful for an `it` Docker session for development
3. `make cleanup-testing`       - Cleans up the testing container created from `build-run-testing`

## Development version 💻

To use the development version with the latest feature and fixes just switch to `development` branch using Git:

`git checkout development`

and update to last version using:

`git pull origin development`
--->

## Updating ⬇️

To update InstAgent with the stable release just pull the latest commit using Git.

1. Make sure you are in the master branch running: `git checkout main`
2. Download the latest version: `git pull origin main`


## Contributing 💡

You can propose a feature request opening an issue or a pull request.

## External library 🔗

[instagrapi](https://github.com/adw0rd/instagrapi)
