from minute.core.bindings import bindings
from minute.core.draw import draw


# Функция, которая отвечает за запуск
def run_app() -> None:
    bindings.get('on_start')()
    while True:
        draw.cleanup()
        bindings.get('on_update')()
