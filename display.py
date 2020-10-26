from lib.waveshare_epd import epd4in2
from PIL import Image,ImageDraw,ImageFont
import time
import os

# resourcedir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'resources')

class Display:
	epd = None
	HBlackimage = None
	drawblack = None
	robotoFont = ImageFont.truetype(os.path.join('resources', 'roboto.ttf'), 24)
	selectedFont = robotoFont
	def __init__(self):
		try:
			self.epd = epd4in2.EPD()
			self.epd.init()
			self.epd.Clear()
			self.HBlackimage = Image.new('1', (self.epd.width, self.epd.height), 255)
			self.drawblack = ImageDraw.Draw(self.HBlackimage)
		except IOError as e:
			print(e)
	def text(self,coord, str):
		
		self.drawblack.text(coord, str, font = self.robotoFont)
	def draw(self):
		self.epd.display(self.epd.getbuffer(self.HBlackimage))
		time.sleep(2)
	def clear(self):
		self.epd.Clear()

