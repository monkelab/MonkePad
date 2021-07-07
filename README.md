# monkepad
A simple Notepad-like editor written in Python

Since MonkePad is written in one file, all your customization can be done without much trouble, and you can transfer it easily. <br/>
**Note: MonkePad should be run with `python3` NOT `python` because of different module names between the versions.**


## Modification
MonkePad has multiple constants declared near the top of the file<br/>
![image](https://user-images.githubusercontent.com/80077386/124516274-1d386480-dd96-11eb-9d49-1b568cede2f1.png)

You can change these to fit your wants. For example:
<br/>
![image](https://user-images.githubusercontent.com/80077386/124516387-5d97e280-dd96-11eb-9ffd-daa94dc9d865.png)<br/>
![image](https://user-images.githubusercontent.com/80077386/124516359-4ce76c80-dd96-11eb-8d33-9a17ab8c6a30.png)

## Building
```shell
pip install pyinstaller
pyinstaller --onefile monkepad.py
```

[MonkePad color palette](https://lospec.com/palette-list/1bit-monitor-glow)
