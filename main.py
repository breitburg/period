import period

@period.on_start
def on_load():
  # Init code here...
  period.public.username = 'Debil'

@period.on_tick
def on_frame():
  period.graphics.alert(text=period.public.username)

if __name__ == '__main__':
  period.run_app()