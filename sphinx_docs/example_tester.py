# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:16:35 2024

@author: jablonski
"""
import subprocess

# Liste Ihrer Skripte
scripts = ['Example0.ipynb', 'Example1.ipynb', 'Example2.ipynb']

for script in scripts:
    try:
        # Führen Sie das Skript aus und überprüfen Sie den Rückgabestatus
        result = subprocess.run(['python', script], check=True)
        print(f'Das Skript {script} wurde erfolgreich ausgeführt.')
    except subprocess.CalledProcessError:
        print(f'Fehler beim Ausführen des Skripts {script}.')
