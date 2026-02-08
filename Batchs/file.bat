@echo off
:start_
echo started
title first program
set /P user=enter ur name:
if %user% ==storm (goto change_) else (goto idk_)

if not defined user goto exit_

:change_
move "C:\Users\Raze\Downloads\thumb-1920-350633.jpg" "C:\Users\Raze\Documents\"
echo %user%, welcome!
echo changed the file dir!

:idk_
set user = 
echo error404!
goto start_

:exit_
exit

pause
