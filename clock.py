import os
import time
from display import Display

displayWidth = 400
displayHeight = 300


def main():
    try:
        d = Display()

        while(True):
            time = getReadableTime()
            startingPos = calulateCenteredPosition(time, displayWidth, 0)
            d.text((startingPos, 100), getReadableTime())
            date = getReadableDate()
            startingPos = calulateCenteredPosition(date, displayWidth, 0)
            d.text((startingPos, 130), getReadableDate())
            d.draw()
            time.sleep(30)
            d.clear()
    except IOError as e:
        print(e)


def getReadableTime():
    return time.strftime('%l:%M%p %z')


def getReadableDate():
    return time.strftime('%b %d, %Y')


def calulateCenteredPosition(string, width, startingPos):
    characterWidth = 36
    strLength = len(string)
    strWidth = characterWidth * strLength
    padding = (width - strWidth) / 2
    return startingPos + padding


if __name__ == "__main__":
    main()
