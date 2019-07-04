# Documentation
## Dependencies
- Raspberry Pi or compatible-SBC
- Ubuntu or compatible Linux Distro
- Python3
- Node
- NPM
- Express
- csv2json

## Tools Used
- Nano
- Vim.Tiny
- IDLE
- Git

# Source.py
- Uses 2 libaries, Time and RPi.GPIO
- Uses a .conf file to adjust settings
- Debug Mode
- Writes to a .txt file for semi-persistant output
- 1 Tick is 1 Period in seconds, eg, 4s period has a 4 second tick
- BlockSizeMins is equal to the minutes in a block x ticks in 1 minute
- The file on disk is written to every minute block, so if BlockSizeMins was 5, every 5 minutes the file would by updated
- BlockSizeHours is equal to the hours in a block x ticks in 1 hour
- BlockSizeDays is equal to the days in a block x ticks in 1 day

# Server.js
- Built Using Node.js
- Uses Express To Host Webpages
- Has Two api inputs, api/csv and api/json
- api/json serves a CSV file converted Into A JSON file
- api/csv serves a CSV file as a txt file

# .conf File Format

- Period Of Swing
- Minute Block Size
- Hour Block Size
- Day Block Count
- Debug Value [0/1]
- Debounce

# GPIO Pinout
- +5v =>  VCC, 10Kohm Resistor
- GND =>  GND
- PIN2 => DOUT
- 10KO => DOUT


