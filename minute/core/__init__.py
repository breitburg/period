from minute.core.bindings import bindings
from minute.core.draw import draw
from minute.graphics.error import error


# Функция, которая отвечает за запуск
def run_app():
    try:
        bindings.get('on_start')()
        while True:
            draw.clear()
            bindings.get('on_update')()
    except Exception as exception: error(exception)