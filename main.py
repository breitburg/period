import minute
import time

@minute.on_tick
def on_update():
    minute.graphics.alert()
    time.sleep(1)

minute.run_app()