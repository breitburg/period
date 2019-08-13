def run_app():
    from minute.core.bindings import bindings
    from minute.core.draw import draw
    from minute.graphics.error import error

    try:
        bindings.get('on_start')()
        while True:
            draw.clear()
            bindings.get('on_tick')()
    except Exception as exception:
        draw.clear()
        error(exception)
