Installation
================================

If you’re working in a Jupyter notebook or a similar environment, remember to place a ‘!’ before each command. This tells the environment to run the command as a shell command, not as a Python command.

How to install PT3S
-------------------

1. Download Anaconda from https://www.anaconda.com/download
2. Run the installer and follow the setup instructions
3. Open your terminal or command prompt
4. Run the following command to install PT3S: ``pip install PT3S``

Update to newest Version
------------------------

1. Open your terminal or command prompt
2. Run the following command to update PT3S: ``pip install PT3S -U --no-deps``

For Developers
--------------

Install and Configure Git on your Computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download Git from https://git-scm.com/downloads
2. Run the installer and follow the setup instructions
3. Configure your username: ``git config --global user.name "Your Name"``
4. Configure your email: ``git config --global user.email "your.email@example.com"``


Clone GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to your project folder: ``cd "path_to_your_project_folder"``
2. Clone the GitHub Repository to your local folder: ``git clone https://github.com/aw3s/PT3S``

Get latest Version from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fetch the latest changes from the origin: ``git fetch origin``
2. Merge the fetched changes into your current branch: ``git merge origin/master``

Commit Your Changes to the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Add files to the staging area: ``git add Dx.py`` (Use ``git add .`` to add all files)
2. Create a new commit with a descriptive message: ``git commit -m "commit_message"``
3. Push your commit to the GitHub Repository: ``git push origin master``

Current Method to Create Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Edit documentation in PT3S/sphinx_docs
2. Navigate to PT3S/sphinx_docs: ``cd /sphinx_docs``
3. Make html build: ``.\make.bat html``
4. After finishing all editing:
5. Copy all contents from PT3S/sphinx_docs/_build/html to PT3S/docs
6. Copy PT3S/sphinx_docs/_static to PT3S/docs
7. Commit changes

The new documentation can be found at https://aw3s.github.io/PT3S/index.html

Note: The copying process will be automated in the future

