import period

@period.on_start
def on_load():
    pass

@period.on_tick
def on_frame():
    for btn in period.button.get_pressed():
        if btn == period.button.right:
            period.draw.text(xy=(0, 0), text='Нажато', fill=True)

if __name__ == '__main__':
    period.run_app()
