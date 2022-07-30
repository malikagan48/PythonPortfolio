# PythonPortfolioExe
### What did I?
 I created an exe file that goes to the portfolio url I created using the webbrowser module. When using the web browser module, I specified the url part with the open cursor.

<p>
  
 First of all we need python.  After completing the Python installation, we integrate our code into the system and check if it works.

</p>
<p>
 import webbrowser as web

web.open('https://malikagan48.github.io/Portfolio/')



<img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/16.PNG" width="auto">


  
## How has this project created?

- first, an empty file named PythonPortfolio was created on the desktop or C: drive and  was created inside.
- Init.py and main.py files, where the actual codes are written.
- A file with the extension setup.py was created by moving to a higher folder. In this file, there are explanations about the package, information about the name and functionality of the package.
- The file directory created by opening the windows command system was accessed.
- "run pip install setuptools" command to start installation.
- then package creation is started using the command " python setup.py sdist bdist_wheel ".
- To upload the created files to PyPI, firstly, the twine installation was done by running the " pip3 install twine" command.
- Then an account was opened by going to the pypi.org page.
- "twine upload dist /* " command is used to upload content outside of dist.
- After the command was run, the user and password created in PyPI were entered.
- The package creation and installation is complete.
  
 ## Application images
<img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/11.PNG" width="auto">
  <img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/12.PNG" width="auto">
  <img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/13.PNG" width="auto">
  <img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/14.PNG" width="auto">
  <img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/15.PNG" width="auto">
  <img src="https://github.com/malikagan48/PythonPortfolio/blob/main/Images/17.PNG" width="auto">

## How can i download project

To download the package created, it will be enough to use the "pip3 install KaganKucukPortfolio" command.
Or you can run it by downloading the exe file.<a href="https://github.com/malikagan48/PythonPortfolio/blob/main/KaganKucukPortfolioExe.exe" target="_blank">You can also access the exe file from here.</a>  
