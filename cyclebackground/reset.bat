@ECHO OFF

tasklist /fi "ImageName eq pythonw.exe" /fo csv 2>NUL | find /I "pythonw.exe">NUL
if "%ERRORLEVEL%"=="0" TASKKILL /F /IM pythonw.exe

tasklist /fi "ImageName eq python.exe" /fo csv 2>NUL | find /I "python.exe">NUL
if "%ERRORLEVEL%"=="0" TASKKILL /F /IM python.exe

SET SCRIPT_DIR=%~dp0

call %SCRIPT_DIR%resetbackground.pyw