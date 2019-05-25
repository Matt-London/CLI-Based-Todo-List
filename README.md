# CLI-Based-Todo-List
A basic command line todo list that can store tasks and repeat them back later.

Run the installer to install the program. Make sure you enter actual paths or you might mess up the install. I recommend entering nothing for the launcher path and sticking with the default of "\usr\bin"

To uninstall simply delete the folder: toDo which lives in the path that you specified first. Then delete the launcher, if not in usr/bin then wherever you specified the second path.

IF THE INSTALLER DOESN'T WORK:
I first recommend placing the following files in a safe place in the same folder: Main.py, Item.py, save.task.
After this you should note the path to the files mentioned above and insert the path within the file named toDo right before the pound symbol that reads "# Insert full path to files here". Finally place the file named toDo somewhere that your $PATH environment variable reaches to and type "chmod +x toDo". This way you can launch the program anywhere in the filesystem.

Note: Uninstaller coming soon

Also note: I am aware that the ascii art that reads "toDo" is a little sloppy. I used an ascii art generator to make it and then I wasn't careful with a replace all command. I like how it looks, so I left it alone.

Enjoy!
