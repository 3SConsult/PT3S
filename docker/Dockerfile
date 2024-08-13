# Verwenden Sie ein offizielles Python-Runtime-Image als Eltern-Image
# FROM python:3.8-slim-buster

# Use the Microsoft Windows Server Core image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /3S

# Kopieren Sie die aktuellen Verzeichnisinhalte in das Arbeitsverzeichnis im Container
COPY "\Users\jablonski\3S\PT3S\docker" /3S

# Kopieren Sie das gesamte SirCalc-Verzeichnis in das Docker-Image
COPY "\3S\SIR 3S\SirCalc-90-14-02-10_Potsdam" /3S

# Installieren Sie alle benötigten Pakete
# RUN apt-get update && apt-get install -y unixodbc-dev #not nec
# RUN powershell.exe -Command \
    # New-Item -ItemType Directory -Force -Path C:\temp ; \
    # Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe -OutFile C:\temp\python-3.8.0-amd64.exe ; \
    # Start-Process C:\temp\python-3.8.0-amd64.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait ; \
    # Remove-Item -Force -Recurse C:\temp
# RUN python -m pip install --upgrade pip setuptools wheel
# RUN pip install --no-cache-dir -r requirements.txt


#docker build -f C:\Users\jablonski\3S\PT3S\docker\Dockerfile -t pt3stest C:\
