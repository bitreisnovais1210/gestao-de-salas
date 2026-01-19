# PowerShell setup script for Windows
$ErrorActionPreference = "Stop"

# Create venv
python -m venv venv

# Activate venv
& .\venv\Scripts\Activate.ps1

# Update pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

Write-Host "Setup completed successfully!" -ForegroundColor Green
