@echo off
SET OSGEO4W_ROOT=C:\Program Files\QGIS 3.32.1
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat
call "%OSGEO4W_ROOT%"\apps\grass\grass83\etc\env.bat
@echo off
path %PATH%;%OSGEO4W_ROOT%\apps\qgis-dev\bin
path %PATH%;%OSGEO4W_ROOT%\apps\grass\grass83\lib
path %PATH%;%OSGEO4W_ROOT%\apps\Qt5\bin
path %PATH%;%OSGEO4W_ROOT%\apps\Python39\Scripts

set PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis-dev\python
set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python39

set PATH=C:\Program Files\Git\bin;%PATH%

cmd.exe