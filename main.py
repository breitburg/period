import period

@period.on_start
def on_load():
    period.public.position = [0, 0]

@period.on_tick
def on_tick():
    speed = 1
    if period.buttons.first in period.buttons.get_pressed(): speed = 2
    elif period.buttons.second in period.buttons.get_pressed(): speed = 3
    elif period.buttons.third in period.buttons.get_pressed(): speed = 4
    elif period.buttons.center in period.buttons.get_pressed(): period.draw.rectangle(xy=(0, 0, 10, 10), fill=True)
    if period.buttons.up in period.buttons.get_pressed(): period.public.position[1] -= speed
    elif period.buttons.down in period.buttons.get_pressed(): period.public.position[1] += speed
    elif period.buttons.left in period.buttons.get_pressed(): period.public.position[0] -= speed
    elif period.buttons.right in period.buttons.get_pressed(): period.public.position[0] += speed
    period.draw.point(xy=period.public.position, fill=True)

if __name__ == '__main__':
    period.run_app()