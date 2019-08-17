def run_app():
    from minute.core.bindings import bindings
    from minute.core.draw import draw
    from minute.graphics.error import error

    on_start = bindings.get('on_start')
    on_tick = bindings.get('on_tick')

    try:
        on_start()
        while True:
            draw.clear()
            on_tick()
    except Exception as exception:
        draw.clear()
        error(exception)
