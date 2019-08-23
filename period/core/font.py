from PIL import ImageFont
from fontawesome import icons
from pathlib import Path

text_font = ImageFont.truetype(str(Path(__file__).resolve().parent.parent.joinpath('fonts').joinpath('text.ttf')), 9)
