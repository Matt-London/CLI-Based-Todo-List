#!/usr/bin/python3
from Item import Item
import time
import sys

taskList = []
file = "./save.task"

## Read the file *oof*
try:
	f = open(file, "r+")
except:
	print("Error opening saved file at: \n" + file)
	sys.exit(1)
lines = f.readlines()
f.close()
for x in lines:
	x = x.split("`|")
	tmp = Item()
	if x[0] != "~|~":
		tmp.setTitle(x[0])
	if x[1] != "~|~":
		tmp.setDescription(x[1])
	if x[2] != "~|~":
		tmp.setTime(x[2])
	if x[3] != "~|~":
		tmp.setLevel(x[3])
	taskList.append(tmp)

if len(sys.argv) > 1 and sys.argv[1] == "Term":
	if len(taskList) > 0:
		for x in range(0, len(taskList)):
			print(str(x + 1) + ". " + str(taskList[x]) + "\n")
		sys.exit(0)
	else:
		sys.exit(0)

print("     ,----,     ")
print("       ,/   .`|     ")
print("     ,`   .'  :     ,---,        ")
print("  ;     ;      /       .'  .' `\      ")
print(".'___,/     ,'  ,---.       ,---.'      \     ,---.   ")
print("|     :      |  '   ,'\      |   |  .`\  |  '   ,'\  ")
print(";     |.';  ; /   /   |     :   : |  '  | /   /   | ")
print("`----'  |  |.   ; ,. :     |   ' '  ;  :.   ; ,. : ")
print("     '   :  ;'   | |: :     '   | ;  .  |'   | |: : ")
print("     |   |  ''   | .; :     |   | :  |  ''   | .; : ")
print("     '   :  ||   :     |     '   : | /  ; |   :     | ")
print("     ;   |.'  \   \  /      |   | '` ,/   \   \  /  ")
print("     '---'      `----'       ;   :  .'       `----'   ")
print("       |   ,.'      ")
print("       '---'        \n")
choice = 0
while True:
	print("Select from the following options:")
	print("1. List tasks")
	print("2. Add task")
	print("3. Delete task")
	print("4. Exit")
	start = 1;end = 4
	try:
		choice = int(input())
	except KeyboardInterrupt:
		sys.exit(1)
	except:
		choice = end + 1
	if choice >= start and choice <= end:
		break
	else:
		print("\n---Invalid choice---\n")
		continue

if choice == 1:
	if len(taskList) > 0:
		print("Here are your existing tasks:\n")
		for x in range(0, len(taskList)):
			print(str(x + 1) + ". " + str(taskList[x]) + "\n")
		sys.exit(0)
	else:
		print("\n---No existing tasks---\n")
		sys.exit(0)

elif choice == 2:
	tmpTitle = ""
	tmpDescription = ""
	tmpLevel = ""
	tmpTime = ""

	print("Add Task:\n")
	tmpTitle = input("Title: ")
	tmpDescription = input("Description: ")
	tmpLevel = input("Level: ")
	tmpTime = input("Time: ")

	taskList.append(Item(tmpTitle, tmpDescription, tmpTime, tmpLevel))
	if len(tmpTitle) == 0:
		tmpTitle = "~|~"
	if len(tmpDescription) == 0:
		tmpDescription = "~|~"
	if len(str(tmpLevel)) == 0:
		tmpLevel = "~|~"
	if len(tmpTime) == 0:
		tmpTime = "~|~"
	try:
		f = open(file, "a+")
		f.write(tmpTitle + "`|" + tmpDescription + "`|" + tmpTime + "`|" + tmpLevel + "`|\n")
		f.close()
	except:
		print("Error writing to file:")
		print("Shutting down...")
		sys.exit(1)
	print("\n===Successfully added task===\n")
	sys.exit(0)

elif choice == 3:
	print("Please enter the number of a task to delete:\n")
	for x in range(0, len(taskList)):
			print(str(x + 1) + ". " + str(taskList[x]) + "\n")
	while True:
		try:
			toDelete = int(input())
			if toDelete < 1 or toDelete > len(taskList):
				toDelete = int("error")
		except:
			print("Please enter a valid number:")
			continue
		break
	toDelete -= 1
	print("Are you sure you want to delete the following task: (y/n)")
	while True:
		print(taskList[toDelete])
		confirm = input()
		if confirm != "y" and confirm != "n":
			print("Enter either 'y' or 'n'")
			continue
		break
	toDelete += 1
	try:
		f = open(file, "r")
		contents = f.readlines()
		f.close()
		f = open(file, "w")
		count = 0
		for line in contents:
			count += 1
			if count == toDelete:
				continue
			else:
				f.write(line)
		f.close()
	except:
		print("Error deleting task:")
		print("Shutting down...")
		sys.exit(1)
	print("\n===Successfully deleted task===\n")
	sys.exit(0)

elif choice == 4:
	print("\n===Goodbye===\n")
	sys.exit(0)
