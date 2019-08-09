import minute
import time

@minute.on_update
def on_frame():
    minute.alert(text='Вам новое сообщение!')
    time.sleep(1)
    
minute.run_app()
