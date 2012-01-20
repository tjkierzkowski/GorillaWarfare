from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.task import Task
########################################
##  Handles Mouse Input and Controls  ##
########################################
class BasicControls(ShowBase):
    def __init__(self):
        self.mouseChangeX = 0
        self.mouseChangeY = 0
        self.windowSizeX = base.win.getXSize()
        self.windowSizeY = base.win.getYSize()
        self.centerX = self.windowSizeX / 2
        self.centerY = self.windowSizeY / 2
        self.H = base.camera.getH()
        self.P = base.camera.getP()
        self.pos = base.camera.getPos()
        self.sensitivity = .5
        self.speed = .2
       
    def movement(self, task):
        mouse = base.win.getPointer(0)
        x = mouse.getX()
        y = mouse.getY()
        if base.win.movePointer(0, self.centerX, self.centerY):
            self.mouseChangeX = self.centerX - x
            self.mouseChangeY = self.centerY - y
            self.H += self.mouseChangeX * self.sensitivity
            self.P += self.mouseChangeY * self.sensitivity
            base.camera.setHpr(self.H , self.P, 0)
           
        #self.accept("w", self.walk)
        return Task.cont

    def startMovement(self):
        base.win.movePointer(0, self.centerX, self.centerY)
        taskMgr.add(self.movement, 'movement')
        taskMgr.add(self.walk, 'walk')

    def stopMovement(self):
        taskMgr.remove('movement')
        taskMgr.remove('walk')
       
    def walk(self, task):
        dir = base.camera.getNetTransform().getMat().getRow3(1)
        dir.setZ(0)
        dir.normalize()
        self.pos += dir * self.speed
        base.camera.setPos(self.pos)
        return Task.cont
       
