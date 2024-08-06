# Verwenden Sie ein offizielles Python-Runtime-Image als Eltern-Image
# FROM python:3.8-slim-buster

# Use the Microsoft Windows Server Core image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die aktuellen Verzeichnisinhalte in das Arbeitsverzeichnis im Container
COPY . /app

# Kopieren Sie das gesamte SirCalc-Verzeichnis in das Docker-Image
# COPY C:/3S/SIR 3S/Sir3S-90-13-02-06_Nordpol.fix5/SirCalc-90-13-02-16_Nordpol.upd2_x64 /app/SirCalc

# Installieren Sie alle benötigten Pakete
# RUN apt-get update && apt-get install -y unixodbc-dev
RUN powershell.exe -Command \
    New-Item -ItemType Directory -Force -Path C:\temp ; \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe -OutFile C:\temp\python-3.8.0-amd64.exe ; \
    Start-Process C:\temp\python-3.8.0-amd64.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait ; \
    Remove-Item -Force -Recurse C:\temp
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt


