# Fun Exercise: Hacking Idle Clickers

Today we will play [Universal Paperclips](http://www.decisionproblem.com/paperclips/). Your goal is to make as many paperclips as possible. To do this, we will use Python to take over the mouse and generate many clicks quickly to save our fingers and mice from wear and tear.

I'd recommend installing pyautogui.

```
pip install pyautogui
```

Open ipython:

```
ipython
```

Import the library:

```python
import pyautogui
```

Explore the functions available in the library. Look for ones that might allow you to read the cursor position and generate clicks at a particular position.

<details><summary>## My solution:</summary>

Mouse over the button, and then run:

```python
x, y = pyautogui.position()
pyautogui.click(x, y, 100)
```

</details>
