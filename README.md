# Purpose
This repo contains measurements taken and their results for a practical lab concerning biodiversity monitoring solutions at the University of Osnabrück.

# Software used
## Server and client
Self-developed client/server software (https://github.com/biodiversity-monitoring-sose2024/networking/commit/8b2df6342e51d556d1700a5747960eeb81f42daa)
on the RPI Zero and nodes further up the infrastructure.

Self-developed ESP32 firmware for the ESP (https://github.com/biodiversity-monitoring-sose2024/esp32-audio-capture/commit/707777fa8513fa2036657a71bb55c77e0e998a3d)

[arecord](https://linux.die.net/man/1/arecord) on the RPI Zero to record audio.

## Evaluation
Generation of plots with matplotlib via [plot.py](tools/plot.py).  

Generation of power consumption markdown tables via [markdown-from-measurements.py](tools/markdown-from-measurements.py) and generation from upload time tables from device specific log files for the [esp32](esp/tools/markdown-from-log.py) and [Raspberry Pi Zero](raspberrypi-zero/tools/markdown-from-log.py).  

The images in the `pictures` folders were generated with ffmpeg and then OCR'd using [gImageReader](https://github.com/manisandro/gImageReader).

# Test files
All send tests were done using a constant set of 44 sound files, each 7.2MB in size.