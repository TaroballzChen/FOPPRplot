# FOPPRplot
FOPPR data operate &amp; plot online by PyQt5,matplotlib,pandas programing with python3

# Download
`git clone https://github.com/curtis992250/FOPPRplot`

# Setup
```command
cd FOPPRplot
pip install -r requirement.txt
```

# Usage
`python main.py`

![view](https://i.imgur.com/lFvg9yG.png)

![movie](https://youtu.be/tBTep86xzbQ)


# pyinstaller 
Maybe you want to execute FOPPRplot program with only one execution file. You can use pyinstaller to pack all of .py file by the command as follow:
```command
pyinstaller main.py --paths=C:\...\FOPPRplot\module --paths=C:\...\FOPPRplot\core --paths=C:\...\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\PyQt5\Qt\bin --paths=C:\...\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\PyQt5\Qt\plugins --hidden-import scipy._lib.messagestream --paths=C:\...\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\scipy\extra-dll --hidden-import=pandas._libs.tslibs.timedeltas -F -w
```
*  replace `...` to your file path in real
*  my environment for packing:
> * OS : Windows 7 64bit
> * Python : 3.5.4 32bit
> * Pyinstaller : v3.3.1

# Update
* 2018.5.3 Add new function of removing selected point from graph
> * (notice: only removing point from graph but plot data still alive)

* 2018.5.9 Add new function of input Sample M.W. and caculating LOD(M) by Sample M.W. that you gave
* 2018.5.16 modify the name of y label

