import sys, os
from pandac.PandaModules import Filename
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from BasicControls import BasicControls

class MainGame(ShowBase):

	def __init__(self):
		ShowBase.__init__(self)
		
		#Disable standard mouse camera movement
		#base.disableMouse()
		#Exit app on escape key
		base.accept("escape", sys.exit)
		
		#Get the location of MainGame.py
		projectdir = os.path.abspath(sys.path[0])
		#convert it to Panda's unix-style notation.
		projectdir = Filename.fromOsSpecific(projectdir).getFullpath()
		
		#TODO - Load the level model here
		#base.wireframeOn()
		#self.environ = self.loader.loadModel(projectdir + "/models/levels/ThePlayground")
		#Load the default environment model from the panda Tutorial
		self.environ = self.loader.loadModel(projectdir + "/models/levels/environment")
		
		#Reparent the model to the root of the Scenegraph, aka the "render" node
		#this allows for the object to actually appear on screen
		self.environ.reparentTo(self.render)
		
		#Scale and position the level/environment model
		self.environ.setScale(0.25, 0.25, 0.25)
		self.environ.setPos(-8, 42, 0)
		
		#TODO add camera controls to a function that can be added to the taskMgr
		#Handle camera controls here
		controls = BasicControls()
		#controls.startMovement()
		self.taskMgr.add(controls.movement, 'movement')
		self.taskMgr.add(controls.walk, 'walk')
		
	
app = MainGame()
app.run()

