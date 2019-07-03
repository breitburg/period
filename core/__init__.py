import logging
logging.basicConfig(level = logging.DEBUG)
logging.debug('Graphical core init...')

from .device import *
from .icons import icons, pictograms
from draw import Canvas
from draw.question import QuestionButton
