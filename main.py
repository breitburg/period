from core import *
device = Device()

while True:
    with Canvas(device) as draw:
        from random import randint
        from time import sleep

        for progress in range(0, 101):
            draw.progress_bar(text=f'Обновление... {progress}%', value=progress)
            sleep(randint(0, 10) / 50)

        draw.alert(text='Обновление завершено!')
