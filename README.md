### COMP0035 Content to support the testing activities

If you are using a different IDE to PyCharm you may need to use its documentation to complete the following steps.

#### Step 1: Clone this repository
Clone the repository and open it in your preferred IDE.

If you are working in an online code editor you may need to download as zip and upload to the online IDE.

#### Step 2: Create a virtual environment (venv) in PyCharm
Either: 

a) Use the Preferences https://www.jetbrains.com/help/pycharm-edu/creating-virtual-environment.html 

or,

b) Open terminal in PyCharm project and use the command line:

```python
#creates the venv in the project structure in a folder called venv
python3 -m venv venv
```

#### Step 3: Add the testing packages
There are a number of popular test packages for Python.
Both pytest and unittest are included in PyCharm. This example uses pytest.
If you are using an IDE orther than PyCharm then you may need to install the dependencies listed in requirements.txt:
```python
pip install -r requirements.txt
```
Otherwise in PyCharm open requirements.txt and you should be able to install the dependencies from there.

####  Step 4: Change the Pycharm test runner preferences/settings to Pytest 
See [https://www.jetbrains.com/help/pycharm/pytest.html](https://www.jetbrains.com/help/pycharm/pytest.html)

