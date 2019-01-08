# Python Libraries/Modules

Python was designed with very few builtin features and functions. Most of its functionality comes from various libraries/modules. There are both standard libraries that come with Python and external libraries that need to be installed.

Examples of some useful standard libraries:
* glob - used to match filenames using wildcards
* pathlib - OS independent path utilities
* math - math utilities
* subprocess - used to run external programs from python
* threading, multiprocess - two libraries for parallel processing tasks
* sys - system utilities

A big part of Python's success can be attributed to the high quality of the libraries available through its easy to use package management system (pip). 

Examples of some common useful libraries:
 * [numpy](https://www.numpy.org/) - numerical python - arrays, math utilities, linear algebra
 * [matplotlib](https://matplotlib.org/)- plotting tools for displaying data, very similiar syntax to Matlab
 * [pandas](https://pandas.pydata.org/) - high performance data structures and tools for data analysis 

External libraries must be installed, either system wide or into your virtual environment.

To install a library run:

```
pip install <library name>
```

pip will connect to the Python Package Index ([PyPI](https://pypi.org/)) and retrieve the requested library, as well as any dependencies, and install them.

## Importing and using Libraries/Modules

There are several ways to import libaries. Each one has implications for namespacing. I'll demonstrate by example using the math library.

When you import a library/module, you are given access the many of the functions, classes and variables in those libraries. To prevent name collisions, the standard import method prepends the name of the library to the element you are calling:

## The Python Manifesto

Try:

```python
import this
```


```python
import math
math.sqrt(4)
```

If you have your own function called sqrt, the import of the math library will not override it. While this is more verbose, it is the safest way to proceed, and this is the method you should use most often.

It can be annoying to write out long library names all the time, especially when working interactively. The following demonstrates how you can shorten the namespace:

```python
import math as m
m.sqrt (4)
```

If you only need a single method (or a set of methods) from a library, and don't mind polluting your local namespace, you can use an alternate import method to only pull in the elements of the library you need.

```python
from math import sqrt, pi
sqrt(4)
pi
```

Finally, if you enjoy searching for bugs in your future code base, you can import everything. This is sometimes acceptable for interactive use, but not recommended for scripts of programs.

```python
from math import *
sqrt(4)
```

To see why this is a bad idea, let's try to calculate with some delicious pi.

```python
from math import *

# Bunch of code 

pi = "delicious"

# bunch more code
radius = 1.0
area = pi*radius**2
```

## Writing your own libraries

We'll cover this in more detail later, but it is possible to write your own modules in Python. In fact, you've already done it. At it's simplest, a Python module is just a python file with variables and methods in it.

Let's use the second example from the last section, hello_program.py. In you ipython window:

```
import hello_program
print hello_program.generate_greeting()
```

You've now used your program interactively and include it in other programs. Notice that "Hello World!" wasn't printed when the file was imported. This is due to the if \__name__=="\__main__" conditional statement returning false on import. The \__name__ variable is set by the interpreter when the program is first started. It is set to "\__main__" when the program is run as script, but given the module name when run as a module.

Next: Fun Exercise - [Hacking idle clicker games](IdleClicker.md)
