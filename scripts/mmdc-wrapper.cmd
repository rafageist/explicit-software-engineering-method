@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
mmdc -p "%SCRIPT_DIR%puppeteer.json" %*
