import minute

@minute.on_start
def on_load():
  # Init code here...
  minute.public.username = 'Debil'

@minute.on_tick
def on_frame():
  minute.graphics.alert(text=minute.public.username)

if __name__ == '__main__':
  minute.run_app()