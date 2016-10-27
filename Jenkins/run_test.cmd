@echo on

rem  Run tests using nose and publish tests results, code coverage and
rem  pylint reports
rem 
rem  adapted from http://www.alexconrad.org/2011/10/jenkins-and-python.html

setlocal 



set WORKSPACE=%cd%
set PYENV_HOME=%WORKSPACE%\.pyenv

rem Delete previously built virtualenv
del /Q %PYENV_HOME%\



rem Create virtualenv and install necessary packages

echo "setup virtualenv"
virtualenv --no-site-packages %PYENV_HOME%
call %PYENV_HOME%\Scripts\activate.bat
pip install --quiet nosexcover
pip install --quiet pylint
rem pip install --quiet %WORKSPACE%\  # where your setup.py lives
pip install --quiet -r requirements.txt

rem reset test data for test\test_convert_eol.py
git config core.autocrlf false
git checkout test\data\

rem Run tests 
echo "nosetests"
nosetests --with-xcoverage --with-xunit --cover-erase --cover-tests

echo "pylint"

%PYENV_HOME%\Scripts\pylint.exe -f parseable lib\ test\   1> pylint.out
type pylint.out

exit 0
