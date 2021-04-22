# GimmeThat

For our case we are using pipenv as a package manager instead of Anaconda,
the command below installs pipenv in your system for managing our venv :: 

    pip install pipenv

Now make a project directory ::

    mkdir RecSys && cd RecSys && mkdir .venv

Now we will initialise our virtual environment by selecting the Python version,
that we will use, in my case Python version that i have used is Python 3.8.7 :: 

    pipenv --python 3.8.7


Install LensKit
---------------

use ``pipenv`` to install LensKit in our stock Python virtual environment,
using our Pipfile to install all the dependencies ::

    pipenv install 

now to make use of the virtual enviroment in Jupyter we activate our virtual 
environment by ::

    pipenv shell

and select the python path for the Jupyter Notebook from .venv folder of the directory


--------------
BOOM TOASTED !
--------------
