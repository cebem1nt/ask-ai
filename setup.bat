@echo off
SET "SCRIPT_DIR=%~dp0"

ECHO installing requirements ... 
python -m pip install -r requirements.txt

SET /P API_KEY=Enter your API key: 
ECHO API_KEY="%API_KEY%" > "%SCRIPT_DIR%key.py"

SET "NEW_PATH=%~dp0;%PATH%"
REG ADD "HKCU\Environment" /v PATH /t REG_EXPAND_SZ /d "%NEW_PATH%"

ECHO Setup complete. You can now use the 'askai' command.
