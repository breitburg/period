import minute
import time

@minute.on_tick
def on_frame():
    minute.draw.rectangle(xy=(0, 0, 10, 10), fill=True)
    asdf

minute.run_app()
