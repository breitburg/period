import tiny

@tiny.on_update
def on_frame():
    tiny.alert(text='Здарова!')

tiny.run_app()
