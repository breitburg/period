from tiny.core.bindings import bindings
from tiny.core.draw import draw


# Функция, которая отвечает за запуск
def run_app() -> None:
    bindings.get('on_start')()
    while True:
        draw.update()
        bindings.get('on_update')()
