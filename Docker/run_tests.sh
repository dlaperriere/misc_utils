#!/bin/env bash

cd /src

#echo Test install requirements
#pip install -r requirements.txt
#pip3 install -r requirements.txt
echo -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

echo Test Python 2
bash Jenkins/run_test.sh python2

echo -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

echo Test Python 3
bash Jenkins/run_test.sh python3

echo -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

echo -30-

