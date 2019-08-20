import period


@period.on_start
def on_load():
  # Init code here...
  period.public.username = 'Вам новое сообщение!'

@period.on_tick
def on_frame():
  period.draw.rectangle(xy=(0, 0, 10, 10), fill=True)
  period.graphics.alert(text=period.public.username)

if __name__ == '__main__':
  period.run_app()