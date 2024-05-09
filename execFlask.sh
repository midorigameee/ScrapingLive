#!/bin/sh

python3 -m venv python12_venv
. ./python12_venv/bin/activate
cd WebScapingAPI
pip install -r requirements.txt
python liveCalendar.py 5001