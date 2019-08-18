# minute ![](https://img.shields.io/github/languages/code-size/breitburg/minute) ![](https://wdp9fww0r9.execute-api.us-west-2.amazonaws.com/production/badge/breitburg/minute)

Library for writing applications for watches with a 1-bit 128x64 display and [PiSugar](https://github.com/PiSugar/PiSugar) battery.

```python
import minute

@minute.on_start
def on_start():
    minute.public.name = 'Alex'
    minute.graphics.alert(text=f'Welcome, {minute.public.name}!')

@minute.on_tick
def on_frame():
    minute.draw.rectangle(xy=(0, 0, 10, 10), fill=255)

if __name__ == '__main__':
    minute.run_app()
```

## Requirements

All requirements are defined in `requirements.txt`:

- luma.core (1.9.0)
- luma.emulator (1.1.0)
- luma.oled (3.2.1)
- pillow (6.0.0)
- pygame (1.9.6)
- pyserial (3.4)
