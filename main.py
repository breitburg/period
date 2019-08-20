import period

@period.on_start
def on_load():
    period.public.position = [0, 0]

@period.on_tick
def on_tick():
    speed = 1
    if period.button.first in period.button.get_pressed(): speed = 2
    elif period.button.second in period.button.get_pressed(): speed = 3
    elif period.button.third in period.button.get_pressed(): speed = 4
    elif period.button.center in period.button.get_pressed(): period.draw.rectangle(xy=(0, 0, 10, 10), fill=True)
    if period.button.up in period.button.get_pressed(): period.public.position[1] -= speed
    elif period.button.down in period.button.get_pressed(): period.public.position[1] += speed
    elif period.button.left in period.button.get_pressed(): period.public.position[0] -= speed
    elif period.button.right in period.button.get_pressed(): period.public.position[0] += speed
    period.draw.point(xy=period.public.position, fill=True)

if __name__ == '__main__':
    period.run_app()