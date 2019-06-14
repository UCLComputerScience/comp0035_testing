### comp0035_testing
COMP0035 Content to support the testing lecture.

The lecture materials contain guidance for using PyCharm, if you are using a different IDE you may need to use its documentation to complete the following steps.



#### Step 1: Clone this repository in PyCharm 

#### Step 2: Create a virtual environment (venv) in PyCharm
Either: 

a) Use the Preferences https://www.jetbrains.com/help/pycharm-edu/creating-virtual-environment.html 

or,

b) Open terminal in PyCharm project and use the command line:

```python
#creates the venv in the project structure in a folder called venv
python3 -m venv venv
```

#### Step 3: Create the tests
There are a number of popular test packages for Python.
Both pytest and unittest are included in PyCharm. This example uses pytest.
If you are using an IDE orther than PyCharm then you may need to install the following dependencies:
```python
pip install pytest pytest-cov
```

Otherwise in PyCharm change the preferences to use Pytest https://www.jetbrains.com/help/pycharm/pytest.html 

It is typical to add tests to a directory called ‘test’.

It is also standard naming convention to name the test files the same as the python code files that they test with test_ as a prefix.

Open the tests folder (directory) called ‘test’

#### Step 4: Run the tests
To run the tests, either use the command prompt in the terminal: 
python3 -m pytest -v --cov

Or right click on the file the PyCharm project structure and select Run ‘test_calculator’ with Coverage
 

####Step 4: Create a requirements.txt to list the packages that are dependencies for your project.

From a command line go to the project folder
Enter
```python
pip freeze > requirements.txt
```




