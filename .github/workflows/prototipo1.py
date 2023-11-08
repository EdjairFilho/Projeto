pip install googletrans==4.0.0-rc1

from googletrans import Translator

trans = Translator()

trans.translate(input(), dest="pt").text

trans.translate(input(), dest="en").text
