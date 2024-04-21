@ECHO OFF

SET SCRIPT_DIR=%~dp0
SET "PATH1=%SCRIPT_DIR%source"
SET "PATH2=%SCRIPT_DIR%target"

python %SCRIPT_DIR%/webpconv.py %PATH1% %PATH2%
pause