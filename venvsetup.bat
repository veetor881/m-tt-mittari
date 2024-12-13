@echo off
REM Create the virtual environment
echo Creating virtual environment...
python -m venv mättö_env

REM Activate the virtual environment
echo Activating virtual environment...
call mättö_env\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Deactivate the virtual environment after setup
deactivate

echo Setup complete! Virtual environment is ready.
pause
freeze
