python tools/plot.py esp/record/1/README.md esp/record/2/README.md esp/record/3/README.md \
        --y-column "Wattage [W]" \
        --table-index 0 \
        --output-file images/results/esp_record_watt.svg \
        --title "ESP32 power consumption while recording"
python tools/plot.py esp/send/1/README.md esp/send/2/README.md esp/send/3/README.md \
        --y-column "Wattage [W]" \
        --table-index 1 \
        --output-file images/results/esp_upload_watt.svg \
        --title "ESP32 power consumption while uploading"
python tools/plot.py esp/send/1/README.md esp/send/2/README.md esp/send/3/README.md \
        --y-column "Time [ms]" \
        --table-index 0 \
        --output-file images/results/esp_upload_times.svg \
        --title "ESP32 upload time"

python tools/plot.py raspberrypi-zero/record/1/README.md raspberrypi-zero/record/2/README.md raspberrypi-zero/record/3/README.md \
        --y-column "Wattage [W]" \
        --table-index 0 \
        --output-file images/results/rpi_record_watt.svg \
        --title "RPI Zero power consumption while recording"
python tools/plot.py raspberrypi-zero/send/1/README.md raspberrypi-zero/send/2/README.md raspberrypi-zero/send/3/README.md \
        --y-column "Wattage [W]" \
        --table-index 1 \
        --output-file images/results/rpi_upload_watt.svg \
        --title "RPI Zero power consumption while uploading"
python tools/plot.py raspberrypi-zero/send/1/README.md raspberrypi-zero/send/2/README.md raspberrypi-zero/send/3/README.md \
        --y-column "Time [ms]" \
        --table-index 0 \
        --output-file images/results/rpi_upload_times.svg \
        --title "RPI Zero upload time"