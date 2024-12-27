For Developers
==============

Welcome to the Developers page! This section provides resources and instructions for developers who want to contribute to PT3S. 

- **Contact**: For additional information regarding PT3S, this documentation, and contribution inquiries, please contact `jablonski@3sconsult.de <mailto:jablonski@3sconsult.de>`_. If you need feedback on a specific issue with PT3S, please include the PT3S version you are using and, if available, the Jupyter Notebook you are working with.

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

General GitHub Version Control Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These instructions lay out the different steps of the GitHub procedure around contributing to PT3S. Especially due to the GitHub repository currentley sitting on only one branch (master), following these basic rules is crucial. As soon as PT3S has a higher amount of frequent contributors, a more suitable system with multiple branches will be implemented.

.. note::
    Before following each step for the first time, read their instructions fully including notes like this one. If an unexpected problem occurs, you can search the :ref:`command-collection-label` for a solution.

Follow these steps every time you contribute to PT3S:

1. **Get the Latest Version from GitHub**: :ref:`get-latest-version-label`

2. **Edit PT3S**: Now you can edit the entire PT3S project locally. Please ensure, that nobody else is working on the project simultaneously in the same sourcefiles, because this could cause problems, when trying to commit.

3. **Commit Your Changes to the GitHub Repository**: :ref:`commit-changes-label`

.. _get-latest-version-label:

Get the Latest Version from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch the latest changes from the origin and merge them into your current branch, follow these steps:

1. **Navigate to project directory:** Use the ``cd`` command followed by the path to the directory of your project (This directory should contain an invisible .git folder).

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S"
      
2. **Pull the latest changes from the origin**: Use the ``git pull`` command. 

   .. code-block:: bash

      git pull origin master
        
   For a more detailed updating process, follow steps 2 and 3 instead.
        
2. **Fetch the latest changes from the origin:** Use the ``git fetch origin`` command.

   .. code-block:: bash

      git fetch origin

3. **Merge the fetched changes into your current branch:** Use the ``git merge origin/master`` command.

   .. code-block:: bash

      git merge origin/master

.. note::
    If you made local changes to files that were also edited by a remote commit, make a local copy of your project directory and use ``git reset --hard origin/master``. Afterwards you can paste you local changes back in. Just make sure that the remote changes to these files were not important or manually include them in your files.

.. code-block:: bash

   git reset --hard origin/master  

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

.. .. note::
    If you want to push multiple commits back to back, keep in mind that the PT3S GitHub repository uses :ref:`github-workflow-label` that might require you to fetch after committing to certain directories. Because workflows can automatically author commits, so fetching ensures you have the latest changes. Alternatively you can check the :ref:`current-workflow-label` utilised by the GitHub Repository and whether the might be triggered by your commit.

.. _command-collection-label:

Collection of Useful Git Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To discard all local changes and set your local HEAD to the master, use:

   .. code-block:: bash

      git reset --hard origin/master

To discard all remote changes and force push local HEAD to the master, use:

   .. code-block:: bash

      git push origin master --force
           
To uncommit commited but not yet pushed changes of the previous commit without changing local files (move HEAD pointer back by one commit), use:

   .. code-block:: bash

      git reset --soft HEAD~1

To revert all changes caused by a commit, use:

   .. code-block:: bash

      git revert commitID
      
To load a branch locally, use:

   .. code-block:: bash

      git checkout <branchname>

.. _github-workflow-label:

GitHub Workflows
~~~~~~~~~~~~~~~~

Our GitHub repository uses workflows to facilitate certain processes by automating tasks. Workflows are defined using YAML files and are stored in the `.github/workflows` directory of our repository.

.. _current-workflow-label:

Current Workflows
^^^^^^^^^^^^^^^^^

All of our workflows can be triggered using :ref:`manually-triggering-workflows-label`. 

We currently use the following workflows:

.. list-table:: 
   :header-rows: 1

   * - **Name**
     - **Triggers (Apart from manually triggering)**
     - **Tasks**
   * - Automatic Copying of HTML-Files
     - Push to `PT3S/sphinx_docs/_build/html/`
     - Copies HTML files from master `PT3S/sphinx_docs/_build/html` to gh-pages `PT3S/docs`
   * - Automatic Deletion of Example Data
     - 
     - Deletes example data in all `PT3S/Examples/WDExampleX/B1/V0/BZ1` except `.xml` and `.mx1`

.. _manually-triggering-workflows-label:

Manually Triggering Workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow these steps to manually trigger a workflow via GitHub:

1. Navigate to the **Actions** tab of the PT3S GitHub repository.

2. Select the workflow you want to trigger from the list on the left.

3. Click the **Run workflow** button.

4. Optionally, provide any required inputs and click **Run workflow** again to start the workflow.
                   
Working with PyPI
-----------------     
         
.. _version-control-label:    
          
Release a New Version
~~~~~~~~~~~~~~~~~~~~~

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
          
On the :doc:`releases` page you can view how this rst code is transformed into html.

2. **Change Release Number:** Change the release numbers in the files: PT3S/conf.py, PT3S/setup.py, PT3S/sphinx_docs/conf.py

3. **Run Doctests:** Follow the steps of :ref:`running-doctests-label`. And make sure they are executed successfully.

4. **Generate the Documentation:** Follow the steps in :ref:`generating-documentation-label`.
  
        
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

      python -m twine upload -u __token__ -p <YOUR TOKEN> dist/* --verbose
 
.. note::

   Make sure to keep your API token secure and do not hard-code it in your scripts or code. It's best to set it as an environment variable or store it in a secret configuration file.

7. **Test the Deployment:** Follow the steps in :ref:`test-the-deployment-label`

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

By installing PT3S in editable mode, a `PT3S.egg-link` file is created in the `C:\\Users\\User\\AppData\\Local\\anaconda3\\Lib\\site-packages` directory. This file is a link to your project directory and allows Python to import the package as if it were installed normally. If you no longer need the package to be in editable mode, you can simply reinstall PT3S using pip. You can also reinstall an older version this way to test it.

.. _generating-documentation-label:

Generating the Documentation
----------------------------

The PT3S documentation is edited in PT3S/sphinx_docs and files hosting the documentation are located in PT3S/docs.

If you want to edit the documentation yourself, you have to install sphinx related python packages.

   .. code-block:: bash

      pip install nbsphinx sphinx_copybutton sphinx-rtd-theme

Before generating the documentation for the first time, follow the steps of :ref:`install-editmode-label`.

To generate documentation, follow these steps:

1. **Edit the documentation:** Make your changes in the PT3S/sphinx_docs directory.

2. **Navigate to the PT3S/sphinx_docs directory:** Use the ``cd`` command.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S\sphinx_docs"

3. **Make an HTML build:** Use ``python3 -m sphinx.cmd.build -b html . /_build/html`` (for python env)  or ``.\make.bat html`` (for conda env).

   .. code-block:: bash

      python3 -m sphinx.cmd.build -b html . /_build/html
   
   .. code-block:: bash

      .\make.bat html

3. **Use Build File**: Alternatively, instead of using the ``.\make.bat html`` command, you can simply open the `PT3S/sphinx_docs/make_html_docs.py` file and run it to generate the documentation. This method will not print any Sphinx debugging output and will save time. This alternative is recommended when making many iterative improvements to the documentation.

4. **Commit the changes.** Commit all files from PT3S/sphinx_docs to GitHub (:ref:`commit-changes-label`).

.. 5. **Get the Latest Version**: You should :ref:`get-latest-version-label` before continuing to edit local.

The new documentation can be found at `https://aw3s.github.io/PT3S/index.html <https://aw3s.github.io/PT3S/index.html>`_

.. note::

   The created files in PT3S/sphinx/docs/_build/html on the master branch are moved to PT3S/docs on the gh-pages branch by one of our :ref:`github-workflow-label` and then hosted via GitHubPages. It might take a couple of minutes until the changes are visible on the website.
   
.. _test-the-deployment-label:

.. _running-doctests-label:

Running Doctests
----------------

Follow these tests to run all doctests included in this documentation:

1. **Navigate to sphinx_docs directory:** Open your terminal or command prompt and navigate to the directory sphinx_docs.

   .. code-block:: bash

      cd "C:\Users\User\3S\PT3S\sphinx_docs"

2. **Make a doctest build:** Use the ``.\make.bat doctest`` command.

   .. code-block:: bash

      .\make.bat doctest

You will get a console output and a output.txt file in the sphinx_docs\_build\doctest directory.

If you want the newly added or edited tests included into the hosted documentation follow the steps of :ref:`generating-documentation-label`. Running the tests beforehand is only necessary if the tests are inclueded outside of .rst files.

Testing the Deployment with Docker
----------------------------------

To ensure that the examples provided on the :doc:`examples` page run smoothly on devices of users not involved in the development process, we test them using nbval inside a Docker container. This container simulates a Windows environment, including SIR 3S, the latest release of PT3S with its dependencies, the example data, and the example notebooks.

.. _environment-versions-label:

Environment Versions
~~~~~~~~~~~~~~~~~~~~

This list provides information about the versions of various tools used throughout this project regarding development, creation of documentation, use of examples, etc. It is recommended to use the same versions of these tools, especially if you are contributing. These versions are used in the Docker testing.

.. list-table:: 
   :header-rows: 1

   * - **Tool**
     - **Version**
   * - Python
     - 3.11.8
   * - Anaconda (Not used in Docker)
     - 24.11.0 
   * - Sphinx-build
     - 5.0.2

Initial Test Setup Process
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    Not all files mentioned below are publicly available.

To set up all necessary files and programs to run tests on Notebooks, follow these steps:

1. **Setup Docker**: Download and install Docker Desktop. There might be some issues that need fixing in Windows settings. Help from the technical team is advised.

2. **Enable Windows Containers**: Right-click on the Docker Desktop icon in your taskbar and click "Switch to Windows Containers".

3. **Get Docker Files**: Copy `T:/interne_Projekte/PT3S/docker` and `T:/interne_Projekte/PT3S/dockerNotebooks` to `C:/Users/User/3S`.

4. **Copy SirCalc**: The `C:/Users/User/3S/docker/SIR 3S` directory is empty and needs a working copy of SirCalc. The easiest way to achieve this is to copy all files from your local `C:/3S/SIR 3S` to `C:/Users/User/3S/docker/SIR 3S` and then delete unnecessary files. This prevents them from being included in the container, which would make the build process even longer.

5. **Create v**: Create a folder at `C:/Users/User/3S/dockerNotebooks`. The `dockerNotebooks` folder on your local machine is used as a volume for the Docker container. Therefore, all changes made to the notebooks inside the container are applied to these files. You can also save additional notebooks to this folder to add them into the container for testing.

6. **Start Docker Engine:** Open Docker Desktop and start the engine.

7. **Navigate to Docker Folder:** Open your terminal or command prompt and navigate to the directory containing your Dockerfile.

   .. code-block:: bash

       cd C:/Users/User/3S/docker

8. **Build the Docker image**: Run the following command in a cmd with the name you want to give to your Docker image (e.g., `pt3stestpotsdam`). This process can take around half an hour. So make sure everything is set up properly.

   .. code-block:: bash

       docker build -t pt3stestpotsdam .

.. This is the Dockerfile that is being built:

.. .. literalinclude:: /../../docker/Dockerfile
..    :language: dockerfile
..    :caption: Dockerfile

Running Tests
~~~~~~~~~~~~~

These tests are run on :ref:`environment-versions-label`.

Follow these steps to run tests on the Example Notebooks currently hosted at :doc:`examples`:

1. **Start Docker Engine:** Open Docker Desktop and start the engine.

2. **Navigate to your project directory:** Open your terminal or command prompt and navigate to the directory containing your Dockerfile.

   .. code-block:: bash

      cd "C:/Users/User/3S/docker"

3. **Run the Docker container:** Run the following command with the name of your Docker image.

   .. note::
       The port must differ from a local JupyterLab you might be running.

   .. code-block:: bash

      docker run -it --rm -v C:\Users\User\3S\dockerNotebooks:C:\3S\notebooks -p 8889:8888 pt3stestpotsdam

   The container should now be running, downloading the Example Notebooks and upgrading PT3S to its newest version automatically. The `dockerNotebooks` folder on your local machine is used as a volume for the Docker container. Therefore, all changes made to the notebooks inside the container are applied to these files. You can also save additional notebooks to this folder to add them into the container for testing (rerun necessary).

   You now have access to a cmd running in the container environment. The `-it` option starts the container in interactive mode, and the `--rm` option removes the container after it exits.

4. **Start Tests:** Run the following command inside the container cmd. You should now be provided with the test results in the cmd.

   .. code-block:: bash

      pytest --nbval  

   With config  file (currentley not useful):

   .. code-block:: bash

      pytest --nbval --nbval-sanitize-with sanitize.cfg
             
5. **Open new Container CMD:** Run the following command in a local cmd. The container_id can be found on Docker Desktop.

   .. code-block:: bash

      docker exec -it container_id cmd

6. **Start JupyterLab:** Run the following command in the new container cmd.

   .. code-block:: bash

      python -m jupyter lab --ip=0.0.0.0 --allow-root

7. **Open in local Browser**: Due to there not being a browser installed inside the docker container, JupyterLab will not open automatically. Click on one of the links provided in the cmd output or click on the host of the running container under the container tab in Docker Desktop. You might need to enter a token. This can be found in the cmd output as well. Now you can edit the notebooks inside the docker container. Saved changes are applied to your local files in the dockerNotebooks folder. 

8. **Test manually**: To test one specific or all examples, run the following commands.

   .. code-block:: bash

      pytest --nbval ExampleX.ipynb

   .. code-block:: bash

      pytest --nbval