def run_app():
    from time import time
    from period.core.binding import bindings
    from period.graphics.statusbar import status_bar
    from period.core.config import __configuration
    from period.core.draw import draw
    from period.core.device import is_emulator
    from period.graphics.error import error
    from period.core.button import get_pressed

    on_start = bindings.get('on_start')
    on_tick = bindings.get('on_tick')

    try:
        on_start()
        while True:
            start_time = time()
            draw.clear()
            on_tick()

            # Drawing status bar
            if __configuration.get('show_status_bar'): status_bar()
    except Exception as exception:
        draw.clear()
        error(exception)
        raise exception
