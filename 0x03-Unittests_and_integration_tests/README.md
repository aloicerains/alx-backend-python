## Unittests and Integration Tests 
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.     
The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?    
Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.     
Integration tests will test interactions between every part of your code.   

## Objectives
* The difference between unit and integration tests
* Common testing patterns such as mocking, parametrization and fixtures    

## Resources   
* [unnitest - Unit testing framework](https://docs.python.org/3/library/unittest.html)  
* [unittest.mock - mock object library](https://docs.python.org/3/library/unittest.mock.html)  
* [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
* [parameterized](https://pypi.org/project/parameterized/)  
* [Memoization](https://en.wikipedia.org/wiki/Memoization)  
* [Real Python - Python mock library](https://realpython.com/python-mock-library/)  
* [Understanding parameterized](https://www.codestudyblog.com/cnb2001/0123221843.html) 
* [Parameterized Python tests](https://kracekumar.com/post/618264170735009792/parameterize-python-tests/)   
* [Class and Module Fixtures](https://docs.python.org/2/library/unittest.html#class-and-module-fixtures)  

## Tasks
* Create `TestAccssNestedMap` class that inherits from `unittest.TestCase`.     Implement `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.
