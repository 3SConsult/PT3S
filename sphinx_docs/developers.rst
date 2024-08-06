For Developers
==============

Welcome to the Developers page! This section provides resources and instructions for developers who want to contribute to PT3S or use it in their own projects. 

- **GitHub Repository:** You can find the source code and contribute to the project on our `GitHub page <https://github.com/aw3s/PT3S>`_.

- **PyPI Project:** The PT3S package is also available on `PyPI <https://pypi.org/project/PT3S>`_.

.. note::

   If you are working with a Spyder Console or in a similar environment, remember to place a '!' before each command. This tells the environment to run the command as a shell command, not as a Python command. For instance, write ``!git clone`` instead of ``git clone``.

Setting Up Git on Your Computer
-------------------------------

Follow these steps to install and configure Git:

1. **Download Git:** Visit the `official Git website <https://git-scm.com/downloads>`_ and download the version that is compatible with your operating system.

2. **Install Git:** Launch the downloaded installer and follow the setup wizard to complete the installation.

3. **Configure Your GitHub Username:** Open your terminal or command prompt and enter the following command, replacing "Your Name" with your actual GitHub username:

   .. code-block:: bash

      git config --global user.name "Your Name"

4. **Configure Your GitHub Email:** Similarly, set your GitHub email using the following command, replacing ``your.email@example.com`` with your actual email:

   .. code-block:: bash

      git config --global user.email "your.email@example.com"

.. note::

   If you're pushing your first commit to GitHub, you might be prompted to authenticate your GitHub account. This usually involves entering your GitHub account credentials in a browser dialogue window that pops up. This is a standard security measure to ensure you have the necessary permissions to push to the repository.

Working with GitHub
-------------------

.. _cloning-github-label: 

Cloning the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To clone a GitHub repository to your local folder, follow these steps:

1. **Navigate to the Parent Directory of Your Project:** Use the ``cd`` command followed by the path to the parent directory of your project (This is the directory that should contain your project folder).

   .. code-block:: bash

      cd "C:\Users\User\3S"

2. **Clone the GitHub Repository:** Use the ``git clone`` command followed by the URL of the repository.

   .. code-block:: bash

      git clone https://github.com/aw3s/PT3S

Now, you are advised to following the steps of :ref:`install-editmode-label`.

Get Latest Version from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch the latest changes from the origin and merge them into your current branch, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S"
      
2. **Fetch the latest changes from the origin:** Use the ``git fetch origin`` command.

   .. code-block:: bash

      git fetch origin

3. **Merge the fetched changes into your current branch:** Use the ``git merge origin/master`` command.

   .. code-block:: bash

      git merge origin/master

.. _commit-changes-label:

Commit Your Changes to the GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To commit your changes to the GitHub repository, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S"

2. **Add files to the staging area:** Use the ``git add`` command followed by the name of the file. Use ``git add .`` to add all files.

   .. code-block:: bash

      git add .

3. **Create a new commit with a descriptive message:** Use the ``git commit -m "commit_message"`` command.

   .. code-block:: bash

      git commit -m "commit_message"

4. **Push your commit to the GitHub Repository:** Use the ``git push origin master`` command.

   .. code-block:: bash

      git push origin master

Collection of Useful Git Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To discard all local changes and set your local HEAD to the master use:

   .. code-block:: bash

      git reset --hard origin/master

To discard all remote changes and force push local HEAD to the master use:

   .. code-block:: bash

      git push origin master --force


Working with PyPI
-----------------     
         
.. _version-control-label:    
          
Version Control
~~~~~~~~~~~~~~~

Before uploading a new release to PyPI, follow these steps:

1. **Document the Release:** Describe new additions or fixes, that are included in this release, to the PT3S/sphinx_docs/releases.rst file.

   .. code-block:: rst
   
      90.14.20.0.dev1
      ---------------
      - readDxAndMx:
          **Fix:**
              - m is constructed (instead of reading m-pickle) if SIR 3S' dbFile is newer than m-pickle; in previous releases m-pickle was read even if dbFile is newer
          **New:**
              - INFO: if SIR 3S' dbFile is newer than SIR 3S' mxFile; in this case the results are maybe dated or (worse) incompatible to the model 
        
      90.14.19.0.dev1
      ---------------
      **New:**

      - SIR 3S db3 and mx files used in Examples are now included in the package.
          
For further examples on how to document your additions and fixes, visit the :doc:`releases` page.

2. **Change Release Number:** Change the release numbers in the files: PT3S/conf.py, PT3S/setup.py, PT3S/sphinx_docs/conf.py

3. **Generate the Documentation:** Follow the steps of :ref:`generating-documentation-label`.
  
        
Upload a New Version to PyPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to upload a new version of your project to PyPI:

1. **Version Control:** Make sure you have documented your changes and changed the release number in all necessary files according to :ref:`version-control-label`.

2. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S"

3. **Delete Old Distributions:** Remove all old distributions in your ``dist`` directory.

4. **Create a New Source Distribution:** Use the ``python setup.py sdist`` command to create a new source distribution of your package.

   .. code-block:: bash

      python setup.py sdist

5. **Generate an API Token on PyPI:** Log into your PyPI account and navigate to your Account Settings. Find "API Tokens" and then "Add API Token". Provide a token name and select the scopes this token should have access to (include PT3S). Click "Create Token" and make sure to copy your new token. This token can be used for all your future PT3S Uploads.

6. **Upload the Distribution with Twine:** Use the ``python -m twine upload dist/*`` command to upload the distribution.

   .. code-block:: bash

      python -m twine upload dist/*

7. **Enter API Token when Prompted:** You will be prompted to enter your API Token after running the command in step 6. Simply enter your API token when asked.
 
.. note::

   Make sure to keep your API token secure and do not hard-code it in your scripts or code. It's best to set it as an environment variable or store it in a secret configuration file.

.. _install-editmode-label:

Installing PT3S in Editable Mode
--------------------------------

After :ref:`cloning-github-label`, you can install the package in editable mode. Here are the steps:

1. **Navigate to the Directory of the Cloned Repository:** Use the ``cd`` command followed by the path to the directory of your project.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S"

2. **Install the Package in Editable Mode:** Use the ``pip install -e .`` command to install the package in editable mode. 

   .. code-block:: bash

      pip install -e .

Now, your package is installed in editable mode. This means that you can make changes to the source code of the package and those changes will take effect immediately without needing to reinstall the package.

By installing PT3S in editable mode, a `PT3S.egg-link` file is created in the `C:\\Users\\User\\AppData\\Local\\anaconda3\\Lib\\site-packages` directory. This file is a link to the project directory and allows Python to import the package as if it were installed normally. If you no longer need the package to be in editable mode, you can simply delete this `PT3S.egg-link` file. Delete also the PT3S-line in easy-install.pth.

PT3S's Documentation
--------------------

The PT3S documentation is edited in PT3S/sphinx_docs and files hosting the documentation are located in PT3S/docs.

.. _generating-documentation-label:

Generating the Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate documentation, follow these steps:

1. **Edit the documentation:** Make your changes in the PT3S/sphinx_docs directory.

2. **Navigate to the PT3S/sphinx_docs directory:** Use the ``cd`` command.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S\sphinx_docs"

3. **Make an HTML build:** Use the ``.\make.bat html`` command.

   .. code-block:: bash

      .\make.bat html

4. **Commit the changes.** Commit alle files from PT3S/sphinx_docs to GitHub (:ref:`commit-changes-label`).

The new documentation can be found at `https://aw3s.github.io/PT3S/index.html <https://aw3s.github.io/PT3S/index.html>`_

.. note::

   The created files in PT3S/sphinx/docs/_build/html are moved to PT3S/docs by a GitHub workflow and then hosted via GitHubPages. It might take a couple of minutes until the changes are visible on the website.
   
Testing Example Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~
      
.. note::
    This part of the Documentation is still in the works.    
   
Building a Docker Image
"""""""""""""""""""""""

Follow these steps to build a Docker image:

1. **Navigate to your project directory:** Open your terminal or command prompt and navigate to the directory containing your Dockerfile.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S\app"

2. **Build the Docker image:** Run the following command, replacing `pt3stest` with the name you want to give to your Docker image:

   .. code-block:: bash

      docker build -t pt3stest .

Running a Docker Container
""""""""""""""""""""""""""

Follow these steps to run a Docker container:

1. **Start Docker Engine**: Open Docker Desktop and start the engine.

2. **Navigate to your project directory:** Open your terminal or command prompt and navigate to the directory containing your Dockerfile.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S\app"
    
3. **Run the Docker container:** Run the following command with the name of your Docker image. 

   .. note:: 
       The port must differ from a local JupyterLab you might be running (use 8889:8888 instead).

   .. code-block:: bash

      docker run -it --rm -p 8889:8888 pt3stest cmd

You now have access to a cmd running in the container environment. The `-it` option starts the container in interactive mode, and the `--rm` option removes the container after it exits.

Testing Examples
""""""""""""""""

Follow these steps to test Example Notebooks:

1. **Start JupyterLab**: Type the following command into the cmd of the container.

   .. code-block:: bash
   
       python -m jupyter lab --ip=0.0.0.0 --allow-root
       
Alternative:
       
1. **Open Docker Desktop**: This is not preinstalled on 3sconsult devices. It needs to be installed.       

2. **Open JupyterLab**: Under the container tab in Docker Desktop, click on the host of the running container.

3. **Enter Token**: When asked to enter a token, copy and paster the token you can find in the anaconda powershell, that should be running. It is part of the links provided.
