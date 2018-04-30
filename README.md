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

![view][image-1]

# pyinstaller 
Maybe you want to execute FOPPRplot program with only one execution file. You can use pyinstaller to pack all of .py file by the command as follow:
```command
pyinstaller main.py --paths=C:\...\FOPPRplot\module --paths=C:\...\FOPPRplot\core --paths=C:\...\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\PyQt5\Qt\bin --paths=C:\...\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\PyQt5\Qt\plugins --hidden-import scipy._lib.messagestream --paths=C:\...\AppData\Local\Programs\Python\Python35-32\Lib\site-packages\scipy\extra-dll --hidden-import=pandas._libs.tslibs.timedeltas -F -w 
 `
*  replace `...` to your file path in real
*  my environment of packing:
> * OS : Windows 7 64bit
> * Python : 3.5.4 32bit
> * Pyinstaller : v3.3.1

[image-1]:	https://i.imgur.com/lFvg9yG.png