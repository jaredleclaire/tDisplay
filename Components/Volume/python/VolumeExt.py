from TDStoreTools import StorageManager
import TDFunctions as TDF

class Volume:
	"""
	Volume description
	"""	
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.screens = parent.Volume.findChildren(name='Screen*',depth=1)

	def Wireframe(self, state):
		for screen in self.screens:
			screen.Wireframe(state)

	def Frustum(self, state):
		for screen in self.screens:
			screen.Frustum(state)

	def TrackingMarkers(self, state):
		for screen in self.screens:
			screen.TrackingMarkers(state)
	
	def Reinit(self):
		op('base_recreateScreens').par.Recreateallscreens.pulse()
		#op.Screen_Template.allowCooking = False
		print('volume re-initialized')
		
	def SetScreenspacePriority(self, mode):
		for screen in self.screens:
			screen.par.Screenspacepriority = mode
			
	def SetScreenspaceOpacity(self, opacity):
		for screen in self.screens:
			screen.SetScreenspaceOpacity(opacity)

	def DebugOverlay(self, state):
		for screen in self.screens:
			screen.DebugOverlay(state)
		
	def Mode(self, mode):
		for screen in self.screens:
			screen.Mode(mode)
	
	def SetCanvas(self):
		for screen in self.screens:
			screen.SetCanvas()
			
	def SetEnvResolution(self, width, height):
		for screen in self.screens:
			screen.par.Environmentresolutionw = width
			screen.par.Environmentresolutionh = height
