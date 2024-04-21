@ECHO OFF

SET SCRIPT_DIR=%~dp0
SET "PATH1=C:\Users\miro9\Desktop\python_tools\webpconv\source"
SET "PATH2=C:\Users\miro9\Desktop\python_tools\webpconv\target"

python %SCRIPT_DIR%/webpconv.py %PATH1% %PATH2%
pause