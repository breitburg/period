# period ![](https://img.shields.io/github/languages/code-size/breitburg/period) ![](https://wdp9fww0r9.execute-api.us-west-2.amazonaws.com/production/badge/breitburg/period)

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

## Installation

Use `pip` to install the latest version of `period` package:

```console
pip install git+https://github.com/breitburg/period
```

To upgrade package version add `--upgrade` argument:

```console
pip install git+https://github.com/breitburg/period --upgrade
```

## Using

After installing library you need to use `period` command line utility. This command will generate sample project in your current path:

```console
$ period create (name)
```

To run your project you need to be in the project path, use `run` argument to run.

```console
$ period run
```

## Requirements

To automaticly install all requirements use `pip` terminal util:

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

**Release 0.0.8** (26-08-2019)
- Refactored CLI utility
- Refactored status bar
- Added FPS counter
- Added display dim

**Release 0.0.7** (25-08-2019)
- Fixed buttons at hardware

**Release 0.0.6** (23-08-2019)
- Added version checking option to comamnd line tool
- Added help to command line tool

**Release 0.0.5** (23-08-2019)
- Renamed `new-project` option to `create`
- Added resources API

**Release 0.0.4** (23-08-2019)
- Fixed bug with icons font
- Fixed bug with running app function

**Release 0.0.3** (23-08-2019)
- Added command line utility
- New package architecture

**Release 0.0.2** (23-08-2019)
- Added new alerts
- Added font awesome icons

**Release 0.0.1** (21-08-2019)
- Initial release
