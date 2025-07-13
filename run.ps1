[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "run main_app.py..."
.\.venv\Scripts\python.exe main_app.py

Write-Host "done!"
Read-Host "press enter to exit..."