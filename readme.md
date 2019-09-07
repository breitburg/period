# period ![](https://img.shields.io/github/languages/code-size/getperiod/framework) ![](https://img.shields.io/github/v/release/getperiod/framework?include_prereleases)

![](https://imgur.com/download/Nf7iy9A/)

Library for writing applications for watches with a 1-bit 128x64 display and [PiSugar](https://github.com/PiSugar/PiSugar) battery.

```python
import period

@period.on_start
def on_start():
    period.graphics.alert(text='Hello, world')

@period.on_tick
def on_frame():
    period.draw.rectangle(xy=(0, 0, 10, 10), fill=True)
```

## Features

- Pixel font with cyrillic and latin
- Graphical interface elements ready-to-use
- Clear and simple project structure
- Unified portable package structure
- Supports the most popular display modules
- Easy-to-use documentation
- Simulator included

## Requirements

To automatically install all requirements use `pip` terminal util:

```console
pip install -r requirements.txt
```

All requirements are defined in `requirements.txt`:

- luma.core (1.9.0)
- luma.emulator (1.1.0)
- luma.oled (3.2.1)
- pillow (6.0.0)
- pygame (1.9.6)
- pyserial (3.4)
- fontawesome (5.10.1.post1)

## Changelog

**Release 0.1.2** (04-09-2019)
- Removed display dim
- Added optimal frame rate counter
- Added exit buttons combination
- Fixed menu buttons pressing issues
- CLI tool library moved to submodule

**Pre-Release 0.1.1** (30-08-2019)
- Implemented menu

**Release 0.1.0** (28-08-2019)
- Added project building option
- Added status bar dynamic height elements offsets calculation
- Added status bar height as config option

**Pre-Release 0.0.9** (27-08-2019)
- Added support for Windows

**Pre-Release 0.0.8** (26-08-2019)
- Refactored CLI utility
- Refactored status bar
- Added FPS counter
- Added display dim

**Pre-Release 0.0.7** (25-08-2019)
- Fixed buttons at hardware

**Pre-Release 0.0.6** (23-08-2019)
- Added version checking option to comamnd line tool
- Added help to command line tool

**Pre-Release 0.0.5** (23-08-2019)
- Renamed `new-project` option to `create`
- Added resources API

**Pre-Release 0.0.4** (23-08-2019)
- Fixed bug with icons font
- Fixed bug with running app function

**Pre-Release 0.0.3** (23-08-2019)
- Added command line utility
- New package architecture

**Pre-Release 0.0.2** (23-08-2019)
- Added new alerts
- Added font awesome icons

**Pre-Release 0.0.1** (21-08-2019)
- Initial release
