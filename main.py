from core import *
device = Device()

while True:
    with Canvas(device) as draw:
        draw.alert(text='Обновление завершено!')
