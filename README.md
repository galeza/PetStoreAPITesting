# PetStoreAPITesting

This is REST API Python and Behave testing framework for Swagger Petstore: http://petstore.swagger.io/


# Getting Started
Download project from github. Project can be run in eclipse or in console using following commands: 

1. run a runner file:
python Pet_Store_API_Testing_Runner.py
2. run a concrete feature scenario:
python Pet_Store_API_Testing_Runner.py ./features/feature_pet/
3. run tests with specific tags:
python Pet_Store_API_Testing_Runner.py ./features/feature_pet/  --tags=@smoke
4. run without runner (In this case report is not generated):
behave features/feature_pet/Pet_Store_API_Testing.feature
5. run specific scenario (In this case report is not generated):
behave features/feature_pet/Pet_Store_API_Testing.feature -n 'GET pet request using pet ID' 


# Project structure
Test cases are designed using behave python module. They have given-when-then structure.

1. Structure

![Alt text](./project_structure.png?raw=true "Project Structure")


2. Test case example with given-when-then structure:

Scenario: GET pet request using pet ID

  Given "POST" api pet request endpoint is set as "pet"
  When HEADER params for request and response are specified
	And Pet details are specified as "Rex" and "/workspace/PetStoreAPITesting1 " and "pending"
	And Request BODY form parameters are set using pet details  
	And "POST" HTTP request is raised
    And Valid HTTP response is received 
	And Response http code is 200 
    And "GET" api pet request endpoint is set as "pet"
    And HEADER params for request and response are specified
	And "GET" HTTP request is raised
  Then Valid HTTP response is received
	And Response http code is 200 


# Prerequisites

## Built With:
Python 3.6
Module requests version 2.19
Module behave version 1.2.6
Module hamcrest version 1.9
Eclipse + SonarLint + Pydev

### install also allure_behave using command:
-sudo pip install allure_behave

### install Pyhamcrest using commands:
-sudo pip install PyHamcrest -> python2
which pip3 python3
-sudo pip3 install PyHamcrest -> python3

# How to use eclipse with Python behave


## unsused import from behave in steps.py
-behave should be added to the 'Forced Builtin'
Window>Preferences>PyDev>Interperters>Python Interperter>Forced Builtins>New

## duplicated signature: step_impl error
-to turn it off, Window>Preferences>PyDev>Editor>Code Analysis>Others>Duplicated Signature>Ignore

## run from eclipse
-setup the built in run. 
Run>Run Configurations>Python Run
Create a new run. In Main>Project set project. For the Main Module choose version of "/home/xx/bin/behave" Inside the Arguments tab set the Working Directory where .feature file exists. 

# Tags

You can enable/skip tests using tags:

select/enable	  | --tags=@smoke	        |Only items with this tag.
not (tilde/minus) |	--tags=~@smoke	        |Only items without this tag.
logical-or	      | --tags=@one,@two	    |If @one or @two is present.
logical-and	      | --tags=@one --tags=@two	|If both @one and @two are present.

example run only smoke test cases:
python Pet_Store_API_Testing_Runner.py ./features/feature_pet/  --tags=@smoke

# Reports

Test reports are generated in the reporting/results directory.
Each test case can have a following status: passed, failed, skipped.

Report example:
![Alt text](./report_example.png?raw=true "Report Example")

# Versioning
Version 1.0

# Author
Agnieszka Galeza

# License


# Acknowledgments

