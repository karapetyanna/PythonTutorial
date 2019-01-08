# Virtual Environment

While you can run a single copy of Python on your computer and never have any problems, if you work with it long enough you are likely to run into problems with different Python version and library version incompatibilities. The virtual environments were introduced to prevent version conflicts between Python libraries (because libraries are stored in the same directory, regardless of version) and it's also guarantees you are using the library version you expect for the project you are working on.

At this point in your Python learning, you aren't going to run into any problems, but it is worth learning this best practice now so it becomes ingrained. 


## Set up a virtual environment

If you are using Python3, the virtual environment is part of the standard libary (it's built in). So, to start a new virtual environment for a project, run the followig from the root directory:

Windows
```
python -m venv venv
```

Linux
```
python3 -m venv venv
```

These commands create a directory called venv (you can call it whatever you want, just change the last venv in the command). This directory effectively has a standalone Python environment inside it. This command only needs to be run once when the project is set up.

## Activate the virtual environment

Now that your virtual environment directory is created you can activate it. This needs to be done every time you want to run the project. From the project directory containing the venv/ directory run:

Windows
```
venv/Scripts/activate.bat
```

Linux
```
source venv/bin/activate
```

You now have a clean python distribution to work with and add new libraries to. You can tell you are running in a virtual environment because your prompt will have the work (venv) prepended to it.


### VSCode Aside:

If you already have a virtual environment set up in your active project directory, VSCode will automatically find it, but you have to tell it to switch interpreters.

When you open a project with an existing environment, type Ctrl-Shift-P and find the Python: Select Interpreter command. Select you local environment and any programs you run will be run in this environment.

## Turning off the virtual environment

The fastest way to shut down a virtual environment is to close the terminal window you are working with, but you can also deactivate it manually using the following commands.

```
deactivate
```

Next: [How to Run](HowToRun.md)



