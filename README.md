# py_rest_api_tester
A simple data driven REST api test framework in python to verify http endpoint, it reads test data from CSV file and perform HTTP post request then asserts the response against predefined expected HTTP response.

project structure:

API_test/ project directory contains Python code for execution and sub-dir, run_api_test.py is the program entry script to execute test

API_test/test_input/ – test input data required for test execution, test case CSV files lives here

API_test/test_output/ – test output directory contains test_result_ouput.csv and test harness log file

How to setup your test exeution environment:

if on Windows, install Python version 2.7.6+ from https://www.python.org/downloads/windows/

if on Linux, it should have Python insatlled with OS, just check from console '$python --version'. If not installed try 'sudo apt-get install python2.7'

How execute test:

