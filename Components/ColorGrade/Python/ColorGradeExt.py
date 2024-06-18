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

class ColorGradeExt:
	"""
	ColorGradeExt description
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
		
	def ResetTMI(self):
		parent.colorGrade.par.Temperature = 0
		parent.colorGrade.par.Magenta = 0
		parent.colorGrade.par.Intensity = 0
		
	def ResetLGG(self):
		parent.colorGrade.parGroup.Liftcolor = 0
		parent.colorGrade.par.Liftlevel = 0
		
		parent.colorGrade.parGroup.Liftcolor = 0
		parent.colorGrade.par.Liftlevel = 0
		
		parent.colorGrade.parGroup.Gammacolor = 0
		parent.colorGrade.par.Gammalevel = 0
		
		parent.colorGrade.parGroup.Gaincolor = 0
		parent.colorGrade.par.Gainlevel = 0
		
		parent.colorGrade.parGroup.Offsetcolor = 0
		parent.colorGrade.par.Offsetlevel = 0
		
	def ResetSaturation(self):
		parent.colorGrade.par.Saturation = 1
	
	def ResetAll(self):
		parent.colorGrade.ResetTMI()
		parent.colorGrade.ResetLGG()
		parent.colorGrade.ResetSaturation()