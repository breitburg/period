# tiny

Refactored library:

```python
import tiny  # Importing tiny library

# Calling on application start
@tiny.on_start
def on_start():
    tiny.alert(text='Hello, world!')

# Calling on frame update
@tiny.on_update
def on_frame():
    tiny.draw.rectangle(xy=(0, 0, 10, 10), fill=255)

# Entry-point
if __name__ == '__main__':
    tiny.run_app()  # Creating main loop
```

## Requirements

All requirements are defined in `requirements.txt`:

- luma.core (1.9.0)
- luma.emulator (1.1.0)
- luma.oled (3.2.1)
- pillow (6.0.0)
- pygame (1.9.6)
- pyserial (3.4)