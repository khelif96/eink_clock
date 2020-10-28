import os
import time
from display import Display


def main():
    try:
        d = Display()

        while(True):
            d.text((50, 100), getReadableTime())
            d.text((50, 130), getReadableDate())
            time.sleep(30)
            d.clear()
    except IOError as e:
        print(e)


def getReadableTime():
    return time.strftime('%l:%M%p %z')


def getReadableDate():
    return time.strftime('%b %d, %Y')


if __name__ == "__main__":
    main()
