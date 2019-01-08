# How to Run Python

Unlike languages like C++ or Java, Python is an interpreted language. There is no need for the user to explicitely compile (transform semi human readable code into machine instructions). Python handles this at run time. 

This makes Python very flexible. It can be used to do anything. You can use it as a calculator, to do batch scripting jobs, to write full applications and even serve web sites. 

There are a number of ways for the user to interact with the Python interpreter (the program that reads your code and translates it to machine language). In this section, we will cover 3 common ones.

## Interactive Use (with iPython)

You can start Python in interactive mode by simply running the python command without any arguments:

```
python
```

You should see something like the following (this is from my home linux machine):

```
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The python interpreter is started and waiting for valid python code to execute.

Try typing 2+2 and pressing enter:

```
>>> 2+2
4
>>>
```

Great. You now have a calculator. This is an incredibly powerful calculator, however. You can type any valid Python code into this window and have it run that code. 

You can also feed it garbage:

```
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>>
```

In this case, Python didn't appreciate my attempts to be friendly and raised an error. We'll talk more about this in later sections, but what has happened here is that I've asked Python to print out the contents of the variable hello, which doesn't exist yet. 

In the python interpreter, statements that return a value or have a value that's not captured into a variable or another function call are printed to the screen. If we change the hello we typed to "hello" which Python recognizes as a string of characters and not a variable, it will print out the same value.

```
>>> "hello"
'hello'
>>>
```

Let's exit the python interpreter:

```
>>> quit()
```

The standard Python interpreter will run all valid Python passed to it, but it's not the best option for interactive use. For that, there is a program called iPython (interactive Python) that adds features that make interactive use easier.

First we'll install it (have you set up and activated a [virtual environment](VirtualEnvironments.md))

```
pip install ipython
```

We'll talk more about pip in the next section, but what we are doing here is fetching the latest version of ipython from the Python packages repository and installing it in our virtual environment (or system wide if you aren't in a virtual environment).

Now, let's run ipython:

```
ipython
```

You are now greated with a more colourful version of the python interpreter. It also has several other useful features.

* Tab completion
```
pri<TAB> -> print
```
* Syntax highlighting
* Docstring querying
```
print?
``` 
* magic functions (ie. %paste%)
* Interactive GUI's for data visualization
* Allows for web based notebooks (see below)

To exit ipython, type:

```
exit
```

## Scripted Use

Running scripts (lists of commands in a text file) is almost exactly the same as running a program in Python. In both cases, you run the script as an input parameter to the python interpreter:

```
python <name of script>.py
```

In this case, the interpreter will open the file, read in the text and attempt to execute it in the order it reads it in.

Let's write a script and run it. Copy the following into a text file and save it as hello_script.py:

```python
# this is a comment that's ignored by the python interpreter.
"""
There are also multi-line block comments, but these should 
only be used at the top of files and after function, method 
or class definitions because they are treated differently 
than regular comments.

In this script, you can see examples of variable assignment 
and a function call.
"""

hello_string = "Hello World!" 

print (hello_string)
```

Save this file and run it from the command line:

```
python hello_script.py
```

It should print out "Hello World!". 

It's also possible to run a script from within ipython. Start a new ipython session in the same directory as the hello_script.py and type:

```python
run hello_script.py
```

You should see "Hello World!" as output in the ipython interpreter. 

There is an additional advantage to running a script inside the ipython window. Anything you've defined in that script is now available in your session. This is great for debugging. For instance, you now have access to the variable you used to store the "Hello World!" string. In your ipython window, type hello_string. You should see the same text printed out.

Here's a slightly more advanced version demonstrating some other concepts:

```python
"""
This program uses a function to generate a welcome string.
"""

def generate_greeting():
    """
    Return a standard greeting.

    TODO: Support Internationalization
    """
    return "Hello World!"

def test_generate_greeting():
    """
    Tests for the greeting generator.
    """
    assert generate_greeting() == "Hello World!"

if __name__=="__main__":
    print (generate_greeting())
```

This code has the same behaviour, but it demonstrates some more advanced python concepts, including the use of functions, conditionals, testing (with pytest) and python builtin variables.

# Jupyter Notebooks

Another method of using python that's very powerful for data analysis and exploration is to use interactive Jupyter notebooks. 

Jupyter notebooks come set up with Anaconda already. If you are using it in a virtual environment or on another sytem, you can install from pip using:

```
pip install jupyter
```

To start the server run:

``` 
jupyter notebook
```

Here's an [example notebook](JupyterExample.ipynb).

Next: [Libraries](Libraries.md)