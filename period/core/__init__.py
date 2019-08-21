def run_app():
    from period.core.binding import bindings
    from period.core.font import icons
    from period.core.draw import draw
    from period.graphics.error import error

    on_start = bindings.get('on_start')
    on_tick = bindings.get('on_tick')

    try:
        on_start()
        while True:
            draw.clear()
            on_tick()

            # Drawing status bar
            draw.rectangle(xy=(0, 0, 128, 10), fill=True)
            draw.icon(xy=(115, 1), icon=icons['battery-full'])
            draw.icon(xy=(98, 1), icon=icons['usb'])

    except Exception as exception:
        draw.clear()
        error(exception)
