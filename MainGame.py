import sys, os
from pandac.PandaModules import Filename
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

class MainGame(ShowBase):

	def __init__(self):
		ShowBase.__init__(self)
		
		#TODO - find a way to load local directory models
		#Get the location of MainGame.py
		projectdir = os.path.abspath(sys.path[0])
		#convert it to Panda's unix-style notation.
		projectdir = Filename.fromOsSpecific(projectdir).getFullpath()
		#Load the level/environment model
		self.environ = self.loader.loadModel(projectdir + "/models/ThePlayground")
		#self.environ = self.loader.loadModel("models/ThePlayground.egg")
		
		#Reparent the model to the root of the Scenegraph, render
		#this allows for the object to actually appear in the window
		self.environ.reparentTo(self.render)
		
		#Scale and position the level/environment model
		self.environ.setScale(0.25, 0.25, 0.25)
		self.environ.setPos(-8, 42, 0)
	
app = MainGame()
app.run()

