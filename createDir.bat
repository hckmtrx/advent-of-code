@echo off
set day=%DATE:~0,2%
set month=%DATE:~3,2%
set year=%DATE:~6,4%
set directory=%CD%

if %month% == 12 (
    if not exist %directory%\%year%\ (
        md %directory%\%year%\
        echo %directory%\%year%\ was created
    )

    if not exist %directory%\%year%\day%day%\ (
        md %directory%\%year%\day%day%\
        copy %directory%\template.py %directory%\%year%\day%day%\main.py >NUL
        echo %directory%\%year%\day%day%\ was created
        pause
    )
)