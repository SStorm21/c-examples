@echo off
title storm bash.bat
:point1
cls
set  /p name=enter ur name: 
set /p age=enter ur age: 
set /p gender=enter ur gender: 

echo hello there %name% you are %age% old, and ur a %gender%
pause
goto point1
