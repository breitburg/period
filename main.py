import period

@period.on_start
def on_load():
    pass

@period.on_tick
def on_tick():
    print(period.buttons.right in period.buttons.get_pressed())

if __name__ == '__main__':
    period.run_app()