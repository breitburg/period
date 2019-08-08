import tiny  # Importing tiny library

@tiny.on_start
def on_start():
    tiny.alert(text='Starting application')

@tiny.on_update
def on_frame():
    tiny.alert(text='Frame!')

if __name__ == '__main__':
    tiny.run_app()
