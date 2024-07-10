# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:16:35 2024

@author: jablonski
"""

import os
import subprocess
import venv
import pytest
import nbformat
import logging
import re
from nbconvert.preprocessors import ExecutePreprocessor

# Erstellen Sie einen Logger
logging.basicConfig(filename='notebook_tests.log', level=logging.DEBUG)

# Erstellen Sie eine virtuelle Umgebung
venv_dir = "C:\\Users\\jablonski\\3S\\venv"
venv.create(venv_dir, with_pip=True)
logging.info('Virtuelle Umgebung erstellt.')

# Pfad zu den Python- und Pip-Executables in der virtuellen Umgebung
python_exe = os.path.join(venv_dir, 'Scripts', 'python')
pip_exe = os.path.join(venv_dir, 'Scripts', 'pip')

# Pfad zur setup.py-Datei
setup_py_path = os.path.join('..', 'setup.py')

# Öffnen Sie die setup.py-Datei und lesen Sie den Inhalt
with open(setup_py_path, 'r') as f:
    setup_py_content = f.read()

# Finden Sie die install_requires-Liste mit einem regulären Ausdruck
match = re.search(r'install_requires\s*=\s*\[([^\]]+)\]', setup_py_content)

if match:
    # Extrahieren Sie die Liste der Anforderungen
    install_requires = eval('[' + match.group(1) + ']')

    # Installieren Sie jedes Paket in install_requires
    for requirement in install_requires:
        logging.info(f'Installiere Paket: {requirement}')
        subprocess.check_call([pip_exe, 'install', requirement])

logging.info('Anforderungen aus setup.py installiert.')

# Liste Ihrer Skripte
scripts = ['Example0.ipynb', 'Example1.ipynb', 'Example2.ipynb']

for script in scripts:
    try:
        # Führen Sie das Skript aus und überprüfen Sie den Rückgabestatus
        result = subprocess.run([python_exe, script], check=True)
        logging.info(f'Das Skript {script} wurde erfolgreich ausgeführt.')
    except subprocess.CalledProcessError:
        logging.error(f'Fehler beim Ausführen des Skripts {script}.')

def test_notebook(path):
    # Notebook öffnen
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)
    logging.info(f'Notebook {path} geöffnet.')

    # Prozessor erstellen, der das Notebook ausführt
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    # Notebook ausführen
    try:
        ep.preprocess(nb)
        logging.info(f'Notebook {path} erfolgreich ausgeführt.')
    except Exception as e:
        logging.error(f'Fehler beim Ausführen von {path}: {str(e)}')
        pytest.fail(f"Fehler beim Ausführen von {path}: {str(e)}", pytrace=False)

def test_notebooks():
    # Liste Ihrer Notebooks
    notebooks = ['Example1.ipynb']

    for notebook in notebooks:
        test_notebook(notebook)

if __name__ == "__main__":
    test_notebooks()


