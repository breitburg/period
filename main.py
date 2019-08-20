import period

@period.on_start
def on_start():
  period.public.text = 'pressed' if period.button.up in period.button.get_pressed() else 'not pressed'

@period.on_tick
def on_tick():
  period.graphics.alert()

if __name__ == '__main__':
  period.run_app()