Getting Started
===============

Why Python and PT3S are valuable when Working with SIR 3S
----------------------------------------------------------

In progress...

.. note::

    If you have already installed Anaconda (Jupyterlab) and PT3S and you are familiar with their general usage, you can visit the :doc:`developers` page for more technical information, such as how to contribute to PT3S.

Getting Started with Anaconda
-----------------------------

Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing. It is designed for data science, machine learning applications, large-scale data processing, predictive analytics, and more. It simplifies package management and deployment and includes several useful programs, such as JupyterLab and Spyder.

Currently, 3S Consult utilizes JupyterLab for editing and displaying both imported and exported data from SIR 3S, and Spyder for coding PT3S. More details on PT3S Contribution can be found at :doc:`developers`.

For more detailed information, visit the `official Anaconda documentation website <https://docs.anaconda.com/>`_.

How to Install Anaconda
~~~~~~~~~~~~~~~~~~~~~~~

To install Anaconda, follow these steps:

1. **Download Anaconda:** Visit the `official Anaconda download website <https://www.anaconda.com/download>`_ and skip the registration process. Download the version that is compatible with your operating system.

.. image:: 1_anaconda_skip_registration.png
   :alt: anaconda_skip_registration
   :width: 100%
   :align: center 
|
   
2. **Install Anaconda:** Launch the downloaded installer and follow the setup wizard to complete the installation. Under "All" in the Windows start menu, you should now find an Anaconda3 folder.

.. _anaconda_folder:

.. image:: 2_anaconda_folder.png
   :alt: anaconda_folder
   :width: 100%
   :align: center 
|
   
Working with JupyterLab
~~~~~~~~~~~~~~~~~~~~~~~

.. _startandopennotebooks:

How to Start JupyterLab and Open Notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, 3S Consult utilizes JupyterLab to author Notebooks, that are saved as ipynb files. 

To open JupyterLab and have certain Notebooks at hand, follow these steps:

1. **Locate Notebook directory:** Find the parent directory of the Notebook or multiple Notebooks, you want to open, and copy the path  (This directory can also contain non-ipynb files).


2. **Open Anaconda Powershell Prompt:** This is located in your `Anaconda3 folder <anaconda_folder_>`_.

3. **Navigate to the notebook directory:** Use the ``cd`` command followed by the copied path to the Notebook directory.


       .. code-block:: bash

          cd "path_to_your_notebook_directory"
         
4. **Start JupyterLab:** Enter the following command.

       .. code-block:: bash

          python -m jupyterlab

A JupyterLab browser tab should now open.

5. **Open Notebooks:** Each Notebook in the Notebook directory can now be opened individually on the far left side of the tab.

    .. image:: 6_jupyterlab_open_notebook.png
       :alt: jupyterlab_open_notebook
       :width: 100%
       :align: center 

.. _workwithnotebooks:

How to Work with Notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^^

In progress...

Getting Started with PT3S
-------------------------

How to Install PT3S
~~~~~~~~~~~~~~~~~~~

To install PT3S to the newest version, follow these steps (Two Possibilities give):

1. **Possibility: Install via Terminal:**

    1. **Open Terminal or Command Prompt:** You can do this by searching for "terminal" or "command prompt" in your computer's search bar.

    2. **Install PT3S:** Run the following command to install PT3S:

       .. code-block:: bash

          pip install PT3S

2. **Possibility: Install via Example0:**

    1. **Download Example0:** Download Example0.ipynb from :ref:`ex0`.
    
    2. **Open Example0.ipynb via JupyterLab:** Instructions on how to open ipnyb files are explained in detail at :ref:`startandopennotebooks`.
    
    3. **Run 2nd cell:** Instructions on how to work with Notebooks are explained in detail at :ref:`workwithnotebooks`.

    .. image:: 3_pt3s_install_example0.png
       :alt: pt3s_install_example0
       :width: 100%
       :align: center 
|
            
How to Update to the Newest PT3S Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update PT3S to the newest version, follow these steps (Two Possibilities give):

1. **Possibility: Update via Terminal:**

    1. **Open Terminal or Command Prompt:** You can do this by searching for "terminal" or "command prompt" in your computer's search bar.
    
    2. **Update PT3S:** Run the following command to update PT3S:
    
       .. code-block:: bash
    
          pip install PT3S -U --no-deps
          
2. **Possibility: Update via Example0:**

    1. **Download Example0:** Download Example0.ipynb from :ref:`ex0`.
    
    2. **Open Example0.ipynb via JupyterLab:** Instructions on how to open ipnyb files are explained in detail at :ref:`startandopennotebooks`.
    
    3. **Run 4th cell:** Instructions on how to work with Notebooks are explained in detail at :ref:`workwithnotebooks`.

    .. image:: 4_pt3s_update_example0.png
       :alt: pt3s_update_example0
       :width: 100%
       :align: center 
|

How to Import PT3S into Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To import PT3S into your Notebook, use the following commands.

   .. code-block:: bash

    try:
        from PT3S import dxAndMxHelperFcts
    except:
        import dxAndMxHelperFcts

To try this inside an Example Notebook, follow these steps:

    1. **Download Example0:** Download Example0.ipynb from :ref:`ex0`.
    
    2. **Open Example0.ipynb via JupyterLab:** Instructions on how to open ipnyb files are explained in detail at :ref:`startandopennotebooks`.
    
    3. **Run 6th cell:** Instructions on how to work with Notebooks are explained in detail at :ref:`workwithnotebooks`.
    
    .. image:: 5_pt3s_import_example0.png
       :alt: pt3s_update_example0
       :width: 100%
       :align: center 
|