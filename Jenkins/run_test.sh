#!/bin/bash

## Run tests using nose and publish tests results, code coverage and
## pylint reports
##
## adapted from http://www.alexconrad.org/2011/10/jenkins-and-python.html

set -e
set -o pipefail


if [[ -z "$WORKSPACE" ]]; then
    WORKSPACE=$PWD
fi

PYENV_HOME=$WORKSPACE/.pyenv/

## Delete previously built virtualenv
if [[ -d "$PYENV_HOME" ]]; then
    rm -rf $PYENV_HOME
fi


## Create virtualenv and install necessary packages

echo "setup virtualenv"
if hash virtualenv 2>/dev/null; then
  virtualenv --no-site-packages $PYENV_HOME --python=$py
else
  $py -m venv $PYENV_HOME
fi

. $PYENV_HOME/bin/activate
pip install --quiet nosexcover
pip install --quiet pylint
#pip install --quiet $WORKSPACE/  # where your setup.py lives
pip install --quiet -r requirements.txt

echo "nosetests"
nosetests --with-xcoverage --with-xunit --cover-erase --cover-tests

echo "pylint"

pylint -f parseable *.py lib test | tee pylint.out

