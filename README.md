# Halloween Torch based on RP2040

Based on [Adafruit Neopixel Flame Torch](https://learn.adafruit.com/neopixel-flame-torch/). Adapted to work on a [WaveShare RP2040-Zero](https://www.waveshare.com/wiki/RP2040-Zero)

## Prerequisites

### Prepare development environment
To benefit from the pre-configuration of this repository, ensure the following is installed:
* VSCode
* Docker Desktop

Load this repository in VSCode using devcontainers, and afterwards accept all extensions to be installed.

### Install MicroPython on Pico
* Plugin the device into the computer while holding the bootsel button.
* [Download](https://micropython.org/download/) the latest version for the Pico or Pico W
* Drag the UF2 file onto your Pico once it is done downloading. *It should show up on your Desktop as RP1-RP2.
* Once it is done, the RP1-RP2 will disappear.
* Unplug and replug the Pico (without holding the bootsel). You need to do this so VSCode can find the device.

## Usage

* Connect the MCU to a workstation using USB
* Install `code.py` and the `lib` folder to the MCU by dragging it to the mounted MCU drive
* The code should execute directly

_Note:_ In case of a runtime failure, the onboard MCU led will flash


