import tiny
import time
import random

@tiny.on_start
def on_start():
    tiny.alert()

@tiny.on_update
def on_frame():
    tiny.draw.rectangle(xy=(random.randint(0, 128), random.randint(0, 64), random.randint(0, 128), random.randint(0, 64)), fill=255)

if __name__ == '__main__':
    tiny.run_app()
