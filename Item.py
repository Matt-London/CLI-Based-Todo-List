class Item:
	## static stuff
	numItems = 0

	def __init__(self, title="Untitled", description="None", time="None", level="None"):
		self.title = title
		self.description = description
		self.time = time
		self.level = level

		Item.numItems += 1

	## The gets
	def getTitle(self):
		return self.title
	def getDescription(self):
		return self.description
	def getTime(self):
		return self.time
	def getLevel(self):
		return self.level

	## The sets
	def setTitle(self, t):
		self.title = t
	def setDescription(self, d):
		self.description = d
	def setTime(self, ti):
		self.time = ti
	def setLevel(self, l):
		self.level = l

	## others
	def __str__(self):
		if self.title == "Untitled":
			return ""
		toR = self.title
		if self.description != "None":
			toR += "\n    Description: " + str(self.description)
		if self.level != "None":
			toR += "\n    Level: " + str(self.level)
		if self.time != "None":
			toR += "\n    Time: " + str(self.time)
		return toR
