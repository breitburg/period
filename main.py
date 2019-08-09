import minute

@minute.on_update
def on_frame():
    minute.alert(text='Здарова!')

minute.run_app()
