# Sublime Text - Open Python file in external Windows command prompt

Sublime Text can build a Python file by default and run it in the built-in command panel but this doesn't allow interactivity (i.e. user keyboard input). These steps will create a custom build system to run a Python program in a Windows command prompt and therefore allow interactivity.

1. Select Tools -> Build System -> New Build System...
2. Replace the text with the following lines:

 ```json
 {
    "selector": "source.python",
    "windows": {
        "shell_cmd": "start \"$file_name\" cmd /c \"python $file_name & pause\"",
    }
 }
 ```
3. Save the file in the default location with a meaningful name, like `Python3.sublime-build`
4. Select the new build system through Tools -> Build System -> Python3
5. With your Python file open, build it (run) with `Ctrl + B` or Tools -> Build.

Your Python file should now open in a Windows command prompt. 

*Note*: These instructions are for Python 3 and assumes that the Python executable folder (default: `C:\Program Files\python36\`) is added to your system PATH. If you can run the `python` command from a prompt window, you're good to go. More information here: https://docs.python.org/3/using/windows.html#configuring-python