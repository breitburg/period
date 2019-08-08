from .bindings import bindings


def run_app() -> None:
    bindings.get('on_start')()
    while True:
        bindings.get('on_update')()
