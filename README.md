# Clock Counter 1.2.0

## Requirements
- Raspberry Pi
- Digital Sensor, (Active Low), For example a break-light switch or hall effect sensor
- Python 3
- Node.js

## Dependencies
- python3
- node
- npm
- express
- csv2json
- internet
- GNU screen

## Setup
1. on a pc, launch a terminal, the rest of the instructions will be assuming you are using an Ubuntu installation.

2. Set the network connection to "shared to other computers"

3. connect the Pi to the pc via an ethernet cable, power the pi on.

4. run `ifconfig` to obtain the pc ip address

5. run `nmap <first, second & third part of pc ip>.0/24`

6. ssh into to pi using the command `ssh pi@<pi ip>`

the rest of the instructions will be ran on the Pi via ssh on the PC

1. Install Python3 `sudo apt install python3`

2. Install node `sudo apt install node`

3. install npm `sudo apt install npm`

4. Download the Zip file containing the source files using `wget https://raw.githubusercontent.com/Gvenn666/Church-Clock-Counter/master/Install_X.X.X.zip`

5. Extract the zip file using unzip `unzip <file>`

6. install GNU screen to allow for multitasking through the command line 
`sudo apt install screen`

7. run GNU screen using the command `screen`

8. run the python script from the current screen and then press ctrl-A and ctrl-D in succession to detach from the current screen

9. run server.js using the command `sudo node server.js`




