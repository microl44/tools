@ECHO OFF

SET SCRIPT_DIR=%~dp0

ECHO "ENTER THE PATH OF THE FOLDER YOU WANT TO ANALYZE
set /p path_name="Empty string to default to appdata/local folder:"

python %SCRIPT_DIR%/list_folder_size.py %path_name%
pause