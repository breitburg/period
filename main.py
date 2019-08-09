import minute

@minute.on_tick
def on_frame():
    pass

if __name__ == '__main__':
    minute.run_app()
