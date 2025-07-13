[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "create venv..."
.\uv.exe venv .venv

Write-Host "run venv..."
.venv\Scripts\activate.ps1

Write-Host "install dependencies..."
.\uv.exe pip install selenium Pillow natsort python-pptx

Write-Host "done!"
Read-Host "press enter to exit..."
