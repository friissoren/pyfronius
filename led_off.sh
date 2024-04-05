#!/bin/bash -e
sudo sh -c 'echo 0 > /sys/class/leds/ACT/brightness'
sudo sh -c 'echo 0 > /sys/class/leds/PWR/brightness'
