import minute
import time

@minute.on_tick
def On_Update():
    minute.alert()
    time.sleep(1)

minute.run_app()