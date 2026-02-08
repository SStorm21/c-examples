@echo off 
title storm batchs
:start
cls
echo logoImage
echo 1)midnightCord 2) discordSpammer
set /p user= :
if not defined user goto start
if /i %user%==1 (goto midnight) else (goto vaild)
if /i %user%==2 (goto discordSpammer) else (goto vaild)

:midnight
echo midnightCordd
pause
cls
goto start

:discordSpammer
echo discordSpammer
pause
cls
goto start

:vaild
echo uknown option!
set /p user=
pause
cls
goto start



