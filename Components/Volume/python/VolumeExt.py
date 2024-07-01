"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().

Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF

class Volume:
	"""
	Volume description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# properties
		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
						   readOnly=False)

		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

		# stored items (persistent across saves and re-initialization):
		storedItems = [
			# Only 'name' is required...
			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
			 						'property': True, 'dependable': True},
		]
		# Uncomment the line below to store StoredProperty. To clear stored
		# 	items, use the Storage section of the Component Editor
		
		# self.stored = StorageManager(self, ownerComp, storedItems)

	def Wireframe(self, state):
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.Wireframe(state)

	def Frustum(self, state):
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.Frustum(state)

	def TrackingMarkers(self, state):
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.TrackingMarkers(state)
	
	def Reinit(self):
		op('base_recreateScreens').par.Recreateallscreens.pulse()
		print('volume re-initialized')
		
	def SetScreenspacePriority(self, mode):
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.SetScreenspacePriority(mode)
			c.par.Screenspacepriority = mode
			print(c.name + ' screenspace priority set to ' + mode)
			
	def SetScreenspaceOpacity(self, opacity):
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.SetScreenspaceOpacity(opacity)

	def DebugOverlay(self, state):
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.DebugOverlay(state)

