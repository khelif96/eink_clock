import os
import time
from lib.waveshare_epd import epd4in2bc
from PIL import Image, ImageDraw, ImageFont
resdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'resources')
roboto = os.path.join(resdir, 'Roboto-Regular.ttf')

def main():
	try:
	# Display init, clear
		display = epd4in2bc.EPD()
		display.init()
		display.Clear() # 0: Black, 255: White
		w = display.height
		h = display.width
		print("Fetching font")
		font = ImageFont.truetype(roboto, 24)
		print('width:', w)
		print('height:', h)
	    ### ... IMAGE CODE ... ###
	except IOError as e:
    		print(e)

if __name__ == "__main__":
    main()
