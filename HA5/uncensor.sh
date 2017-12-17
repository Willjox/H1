#!/bin/bash
python3 uncensor.py
openssl enc -in secret -out bin -d -a;
openssl rsautl -decrypt -inkey uncens.pem -in bin -out klartext
