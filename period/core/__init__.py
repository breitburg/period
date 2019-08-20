def run_app():
    from period.core.binding import bindings
    from period.core.draw import draw
    from period.graphics.error import error

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
