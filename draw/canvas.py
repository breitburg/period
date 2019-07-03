from luma.core.render import canvas
from .advanced import AdvancedDraw


class Canvas(canvas):
    def __init__(self, device):
        super(Canvas, self).__init__(device=device)

    def __enter__(self):
        self.draw = AdvancedDraw(self.image, self.device)
        return self.draw
