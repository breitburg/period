from tiny.bindings import bindings


# Функция, которая отвечает за запуск
def run_app() -> None:
    bindings.get('on_start')()
    while True:
        bindings.get('on_update')()
