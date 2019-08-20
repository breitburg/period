# period ![](https://img.shields.io/github/languages/code-size/breitburg/period) ![](https://wdp9fww0r9.execute-api.us-west-2.amazonaws.com/production/badge/breitburg/period)

Library for writing applications for watches with a 1-bit 128x64 display and [PiSugar](https://github.com/PiSugar/PiSugar) battery.

```python
import period

@period.on_start
def on_start():
    period.public.name = 'Alex'
    period.graphics.alert(text=f'Welcome, {period.public.name}!')

@period.on_tick
def on_frame():
    period.draw.rectangle(xy=(0, 0, 10, 10), fill=255)

if __name__ == '__main__':
    period.run_app()
```

## Hardware

| Name                | Price  | Source     |
|---------------------|--------|------------|
| OLED Display Hat    | $11.66 | AliExpress |
| Raspberry Pi Zero W | $18.89 | Amazon     |
| PiSugar Battery     | $32.99 | Amazon     |
| QI Wireless Charger |  $3.68 | AliExpress |

## Requirements

All requirements are defined in `requirements.txt`:

- luma.core (1.9.0)
- luma.emulator (1.1.0)
- luma.oled (3.2.1)
- pillow (6.0.0)
- pygame (1.9.6)
- pyserial (3.4)
