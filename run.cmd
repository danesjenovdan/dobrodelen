@echo off

set CMDER_START=%~dp0
echo %CMDER_START%

cmd /k "%ConEmuDir%\..\init.bat & cd front & npm run dev" -new_console:n:t:"nuxt"

cmd /k "%ConEmuDir%\..\init.bat & cd back & venv\Scripts\activate.bat & python manage.py runserver" -new_console:s50V:n:t:"wagtail"

start /b code dobrodelen.code-workspace -new_console:bn
