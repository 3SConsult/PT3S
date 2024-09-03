# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:42:47 2024

@author: jablonski
"""

import subprocess

def make_html_docs():
    # Run the make.bat file
    subprocess.run(["cmd", "/c", ".\\make.bat html"])

    print("docs built")
6
make_html_docs()
