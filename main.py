import tiny

@tiny.on_start
def on_start():
    tiny.alert(text='Hello, world!')

@tiny.on_update
def on_frame():
    tiny.draw.rectangle(xy=(0, 0, 10, 10), fill=255)

if __name__ == '__main__':
    tiny.run_app()
