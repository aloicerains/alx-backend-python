## Python-Async Comprehension
The learning objectives of this project includes:   
* How to write an asynchronous generator
* How to use async comprehensions
* How to type-annotate generators

### Resources   
* [PEP 530 - Asynchronous Comprehensions](https://peps.python.org/pep-0530/)  
* [What's New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)  
* [Type hinting generator in Python 3.6](https://stackoverflow.com/questions/42531143/type-hinting-generator-in-python-3-6)  

### Tasks  
* Task 0: A coroutine `async_generator` that takes no argument that loops 10 times each time asynchronously waiting for 1 second then yields random number between 0 and 10.    
* Task 1: Writing task 0 using async comprehesion
* Task 2: `measure_runtime` coroutine that executes async_comprehension four times in parallel using `asyncio.gather` and measures the total run time and return 
