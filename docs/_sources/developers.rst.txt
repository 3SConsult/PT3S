For Developers
==============

This section provides resources and instructions for developers who want to contribute to PT3S or use it in their own projects. 

- **GitHub Repository:** You can find the source code and contribute to the project on our `GitHub page <https://github.com/aw3s/PT3S>`_.

- **PyPI Project:** The PT3S package is also available on `PyPI <https://pypi.org/project/PT3S>`_.

.. note::

   If you are working with a Spyder Console or in a similar environment, remember to place a '!' before each command. This tells the environment to run the command as a shell command, not as a Python command.

Setting Up Git on Your Computer
-------------------------------

Follow these steps to install and configure Git:

1. **Download Git:** Visit the official Git website at `https://git-scm.com/downloads <https://git-scm.com/downloads>`_ and download the version that is compatible with your operating system.

2. **Install Git:** Launch the downloaded installer and follow the setup wizard to complete the installation.

3. **Configure Your GitHub Username:** Open your terminal or command prompt and enter the following command, replacing "Your Name" with your actual GitHub username:

   .. code-block:: bash

      git config --global user.name "Your Name"

4. **Configure Your GitHub Email:** Similarly, set your GitHub email using the following command, replacing "your.email@example.com" with your actual email:

   .. code-block:: bash

      git config --global user.email "your.email@example.com"

.. note::

   If you're pushing your first commit to GitHub, you might be prompted to authenticate your GitHub account. This usually involves entering your GitHub account credentials in a browser dialogue window that pops up. This is a standard security measure to ensure you have the necessary permissions to push to the repository.

Working with GitHub
-------------------

Clone GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~

To clone a GitHub repository to your local folder, follow these steps:

1. **Navigating to the Parent Directory of Your Project:** Use the ``cd`` command followed by the path to the parent directory of your project (This is the directory that contains your project folder).

   .. code-block:: bash

      cd "path_to_your_parent_project_directory"

2. **Clone the GitHub Repository:** Use the ``git clone`` command followed by the URL of the repository.

   .. code-block:: bash

      git clone https://github.com/aw3s/PT3S

Get Latest Version from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch the latest changes from the origin and merge them into your current branch, follow these steps:

1. **Fetch the latest changes from the origin:** Use the ``git fetch origin`` command.

   .. code-block:: bash

      git fetch origin

2. **Merge the fetched changes into your current branch:** Use the ``git merge origin/master`` command.

   .. code-block:: bash

      git merge origin/master

.. _commit-changes-label:

Commit Your Changes to the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To commit your changes to the GitHub repository, follow these steps:

1. **Add files to the staging area:** Use the ``git add`` command followed by the name of the file. Use ``git add .`` to add all files.

   .. code-block:: bash

      git add Dx.py
      # or
      git add .

2. **Create a new commit with a descriptive message:** Use the ``git commit -m "commit_message"`` command.

   .. code-block:: bash

      git commit -m "commit_message"

3. **Push your commit to the GitHub Repository:** Use the ``git push origin master`` command.

   .. code-block:: bash

      git push origin master
     
Working with PyPI
-----------------     
        
Upload a New Version to PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to upload a new version of your project to PyPI:

1. **Navigate to Your Project Directory:** Use the ``cd`` command followed by the path to your project directory.

   .. code-block:: bash

      cd project

2. **Delete Old Distributions:** Remove all old distributions in your ``dist`` directory.

3. **Create a New Source Distribution:** Use the ``python setup.py sdist`` command to create a new source distribution of your package.

   .. code-block:: bash

      python setup.py sdist

4. **Generate an API Token on PyPI:** Log into your PyPI account and navigate to your Account Settings. Select "API Tokens" and then "Add API Token". Provide a token name and select the scopes this token should have access to. Click "Create Token" and make sure to copy your new token.

5. **(Optional) Set Your PyPI API Token as an Environment Variable:** You can do this by running the following command in your console, replacing ``your_token`` with your actual token.

   .. code-block:: bash

      export TWINE_USERNAME=__token__
      export TWINE_PASSWORD=your_token

6. **Upload the Distribution with Twine:** Use the ``python -m twine upload dist/*`` command to upload the distribution.

   .. code-block:: bash

      python -m twine upload dist/*

7. **(Alternative to Step 5) Enter API Token When Prompted:** If you didn't set your PyPI API token as an environment variable in step 5, you will be prompted to enter it after running the command in step 6. Simply enter your API token when asked.

 
.. note::

   Make sure to keep your API token secure and do not hard-code it in your scripts or code. It's best to set it as an environment variable or store it in a secret configuration file.

Creating Documentation
----------------------

To create documentation, follow these steps:

1. **Edit the documentation:** Make your changes in the PT3S/sphinx_docs directory.

2. **Navigate to the PT3S/sphinx_docs directory:** Use the ``cd`` command.

   .. code-block:: bash

      cd .../sphinx_docs

3. **Make an HTML build:** Use the ``.\make.bat html`` command.

   .. code-block:: bash

      .\make.bat html

4. **Commit the changes.** Commit alle files from PT3S/sphinx_docs to GitHub (:ref:`commit-changes-label`).

The new documentation can be found at `https://aw3s.github.io/PT3S/index.html <https://aw3s.github.io/PT3S/index.html>`_.

.. note::

   The created files in PT3S/sphinx/docs/_build/html are moved to PT3S/docs by a GitHub workflow and then hosted via GitHubPages. It might take a couple of minutes until the changes are visible on the website.