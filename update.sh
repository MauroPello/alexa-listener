#!/bin/bash

yes | cp listener.py ~/.local/share/alexa-listener/
killall flask
./alexa-listener &