# minute

Refactored library:

```python
import minute

@minute.on_start
def on_start():
    minute.alert(text='Hello, world!')

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