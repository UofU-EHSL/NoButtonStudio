# Setup #

## Requirements (This should all be done in a setup script in the very end) ##

1) Edit the docker-compose file to have your setups settings including USB device passthrough.
2) Run the following commands to get the enviorment all going.

| Syntax                                | Description                                               |
| ------------------------------------- | --------------------------------------------------------- |
| pip install -r requirements.txt       | Installs are of the requirements for python               |
| sudo apt-get install docker           | Installs docker so you can run compose                    |
| sudo apt-get install docker-compose   | Installs docker compose so you can use a default config   |
| docker-compose up                     | This will build the docker system for home assistant      |

## Home assistant ##

1) Make sure that the everything in your docker container is running by going to `localhost:8123`
2) Make a user and remember the login.
3) get your api key
    1) Go to your profile http://localhost:8123/profile
    2) Create a "Long-Lived Access Token"
    3) Paste that key into the key section of lights.py
4) Import the backup
5) Add all of your devices to zigbee
    1) Follow this link http://localhost:8123/config/integrations and add the zigbee integration.
6) Add all of the devices into scenes
    1) http://localhost:8123/config/scene/dashboard

## Run the no button studio code! ##

1) you can do `python3 record.py` and it will start everything up
2) you can add a start script we have yet to make into the boot of your machine so that if the power goes off everything comes back as normal

### To-Do ###
- [x] Lights system
- [x] Record on card swipe
- [x] Stop recording on second swipe
- [ ] Upload file when finished
- [ ] Share file with the right person
- [ ] Build setup.sh script so it's easy to install everything
- [ ] Automations based on movement or other things in the room
- [ ] Make start up at boot script
