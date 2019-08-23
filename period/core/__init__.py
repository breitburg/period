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
            if False:
                bar_height = 9

                draw.rectangle(xy=(0, 0, 128, bar_height), fill=True)
                for corner in [((0, bar_height + 1), (1, bar_height + 1), (0, bar_height + 2)),
                           ((draw.device.size[0] - 2, bar_height + 1), (draw.device.size[0], bar_height + 1), (draw.device.size[0], bar_height + 3))]:
                    draw.polygon(xy=corner, fill=True)
                draw.icon(xy=(115, 1), icon=icons['battery-full'], size=8)

    except Exception as exception:
        draw.clear()
        error(exception)
