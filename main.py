import minute

@minute.on_start
def on_start():
    minute.globals.a = 3
    pass

@minute.on_tick
def on_frame():
    print(minute.globals.a)

if __name__ == '__main__':
    minute.run_app()
