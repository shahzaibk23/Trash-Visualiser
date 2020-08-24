## TRASH VISUALISER <sup>v1.0</sup>
This is GUI-based Python Desktop Application, that will show all your deleted items inside the Recycle-bin in a better visual representation. You'll be able to open those folders/ files in the GUI, as well as delete and restore them from the GUI, in an effective manner.

### PREQUISITIES
**winshell** library should be installed in your system, before using this program. if not
Run this command
```ruby
pip install winshell
```

## HOW TO USE
start by cloning this repository 
```ruby
$ git clone https://github.com/shahzaibk23/Trash-Visualiser
```
After cloning is successful
```ruby
cd Trash-Visualiser
Trash-Visualiser> python launcher.py
```
#### [CAUTION]⚠️
It may happen that the windows will ask you to create some folders that doesn't exist, these will be the folders that you'd have deleted once. <br />
Simply Click <b>YES</b>, this way the folders you once had deleted will be created again temporarily, so no need to Panic on that, let it happen. <br />
![2](https://github.com/shahzaibk23/Trash-Visualiser/blob/master/Sceenshots/2.PNG "img 2") <br />

After a few seconds of processing, Trash-Visualiser Main Window will be opened
![1](https://github.com/shahzaibk23/Trash-Visualiser/blob/master/Sceenshots/1.PNG "img 1")
This Window will show all the deleted files/folders in your recycle bin.
Files and Folders are visualised seperately.

### FEAUTURES
<ul>
<li> Upon Single CLick on any File/Folder the details(properties) of it will be shown in the down right box. </li>
<li> Upon Double Click on any File: </li>
<ul>
<li> If the Clicked File is .txt OR .py OR any other kind of sorce file that contains any kind of text in it, will be opened directly in the Window, so as you can view it. </li>
<li> Any other file other than text files( Source Code Files included ), won;t be able to be opened, the program will show a message box saying that it can't be opened. </li>
</ul>
<li> Upon Double CLick on a Folder, the Folder will be opened </li>
<ul>
<li> You'll be able to open further files and folders inside that folder, and so on.</li>
</ul>
<li> GO Back Button is found once you're inside any File or Folder, through which you can get back to the main window.</li>
<li> In Order to Restore or Delete a File/Folder Single click on it from the main window, you'll see its properties being shown, then <b>CLick on RESTORE or DELETE button</b> </li>
<ul>
<li>RESTORE: The selected file/folder will be restores to its original location.</li>
<li>DELETE: The selected file/folder will be permanently deleted from the recycle-bin as well.</li>
</ul>
</ul>

![3](https://github.com/shahzaibk23/Trash-Visualiser/blob/master/Sceenshots/3.gif "img 3")

### Using CLI-version
After cloning is successful, cd into the repository folder.
```ruby
cd Trash-Visualiser
```
After that 
```ruby
Trash-Visualiser> cd src/CLI/
Trash-Visualiser> python main.py
```
The exact same operations will be performed but in Command Line Interface.<br />
![4](https://github.com/shahzaibk23/Trash-Visualiser/blob/master/Sceenshots/4.png" img 4") 
