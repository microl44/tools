@ECHO OFF

SET SCRIPT_DIR=%~dp0
SET "PATH_NAME=C:\Users\%USERNAME%\Desktop\rgbslide\mrinc"

call python %SCRIPT_DIR%/changebackground.py %PATH_NAME%
pause