#!/usr/bin/env bash
virtualenv python=/usr/bin/python3.6 venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
