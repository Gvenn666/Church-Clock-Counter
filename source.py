import RPi.GPIO as gpio
import time

settings = open("./.conf")

period = float(settings.readline())

mins = float(settings.readline())
hours = float(settings.readline())
days = float(settings.readline())

debug = int(settings.readline())

debounce = float(settings.readline())

hallSensor = 2
led = 3

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)
gpio.setup(hallSensor, gpio.IN)
gpio.setup(led, gpio.OUT)

ticksInSecond = 1 / period
ticksInMinute = 60 * ticksInSecond
ticksInHour = 60 * ticksInMinute
ticksInDay = 24 * ticksInHour

secsInMin = 60
secsInHour = 60 * secsInMin
secsInDay = secsInHour * 24

filename = "./public/data.txt"
with open(filename, "w+") as csv:
    csv.write("Date,Tick," + str(mins) + " Min(s)," + str(hours) + " Hour(s)," + str(days) + " Day(s)\n")

timeStampsMin = [0,0]
timeStampsHour = [0,0]
timeStampsDay = [0,0]

i, j, k = 0, 0, 0
diffMin, diffHour, diffDay = 0, 0, 0
tick = 0
begin = time.time()

while True:
    while gpio.input(hallSensor) == 1:
        continue

    tick += 1
    timeStamp = time.time();

    gpio.output(led, 1)
    time.sleep(debounce)
    gpio.output(led, 0)

    if debug == 1:
        print("Tick #" + str(tick) + "!")
        print("time (System): " + time.ctime(timeStamp))
        print("time (Pendulum): " + time.ctime(tick * period + begin))

    blockTypeTicks = ticksInMinute
    blockTypeSecs = secsInMin
    blockSize = mins
    if debug == 1:
        print("Checking for tick modulo " + str(blockTypeTicks * blockSize))
    if (tick % (blockTypeTicks * blockSize)) == 0:
        timeStampsMin[i] = timeStamp
        diffMin = abs(timeStampsMin[i] - timeStampsMin[(i - 1) % 2]) - blockTypeSecs * blockSize
        print(str(blockSize) + " Minute Diff: %2.3fs " % diffMin)
        i += 1
        i %= 2
        with open(filename, "a") as csv:
            csv.write(time.ctime(timeStamp) + ",")
            csv.write(str(tick) + ",")
            if diffMin == 0 or diffMin > 999:
                csv.write("-,")
            else:
                csv.write("%3.3f," % diffMin)
            if diffHour == 0 or diffHour > 999:
                csv.write("-,")
            else:
                csv.write("%3.3f," % diffHour)
            if diffDay == 0 or diffDay > 999:
                csv.write("-,")
            else:
                csv.write("%3.3f," % diffDay)
            csv.write("\n")

    blockTypeTicks = ticksInHour
    blockTypeSecs = secsInHour
    blockSize = hours
    if (tick % (blockTypeTicks * blockSize)) == 0:
        timeStampsHour[j] = timeStamp
        diffHour = abs(timeStampsHour[j] - timeStampsHour[(j - 1) % 2]) - blockTypeSecs * blockSize
        print(str(blockSize) + " Hour Diff: %2.3fs " % diffHour)
        j += 1
        j %= 2

    blockTypeTicks = ticksInDay
    blockTypeSecs = secsInDay
    blockSize = days
    if(tick % (blockTypeTicks * blockSize)) == 0:
        timeStampsDay[k] = timeStamp
        diffDay = abs(timeStampsDay[k] - timeStampsDay[(k - 1) % 2]) - blockTypeSecs * blockSize
        print(str(blockSize) + " Day Diff: %2.3fs " % diffDay)
        k += 1
        k %= 2


