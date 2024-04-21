@ECHO OFF

SET SCRIPT_DIR=%~dp0
SET "PATH_NAME=%SCRIPT_DIR%rgbslide"

call python %SCRIPT_DIR%/changebackground.py %PATH_NAME%