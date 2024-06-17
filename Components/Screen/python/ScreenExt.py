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

class Screen:
	"""
	Screen description
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

	def myFunction(self, v):
		debug(v)

	def DebugOverlay(self, v):
		
		op('base_debugOverlay').par.Enable = v
		
		#debug(v)
		
	def TrackingMarkers(self, v):
		
		op('level_markerOpacity').par.opacity = v
		
		#debug(v)
  
	def BoundingBox(self, v):

		op('null_boundsPoint0').display = v
		op('null_boundsPoint1').display = v
		op('null_boundsPoint2').display = v
		op('null_boundsPoint3').display = v
		op('null_boundsPoint4').display = v
		op('null_boundsPoint5').display = v
		op('null_boundsPoint6').display = v
		op('null_boundsPoint7').display = v

		op('null_boundingBox').display = v

		#debug(v)
  
	def UpdateProjMatrix(self):

		m = tdu.Matrix()

		# default projection matrix parameters
		cam = op('cam_outer')
		render = op('render_outerPerspective')
		fovX = cam.par.fov
		aspectX = render.par.resolutionw
		aspectY = render.par.resolutionh
		near = cam.par.near
		far = cam.par.far
		
		# crop values
		cropLeft = op('null_crop')['left']
		cropRight = op('null_crop')['right']
		cropBottom =op('null_crop')['bottom']
		cropTop = op('null_crop')['top']
		
		# re-scale factor calc
		scaleX = 1 / (cropRight - cropLeft)
		scaleY = 1 / (cropTop - cropBottom)
		
		# convert original matrix to projection matrix with default pars
		m.projectionFovX(fovX, aspectX, aspectY, near, far)
		
		# crop to bounding box
			
		m.scale(0.5,0.5,1.0)
			
		m.translate(0.5,0.5,0.0)
			
		m.translate((cropLeft * -1),(cropBottom * -1),0)
			
		m.scale( scaleX , scaleY, 1 )
			
		m.translate(-0.5,-0.5,0.0)
			
		m.scale(2.0,2.0,1.0)
			
		m.fillTable(op('table_projMat'))
		
		#debug(v)
		
	def SetColor(self, r, g, b, a):
		
		#work in progress
		
		num = parent.Screen.digits
		
		r = op.Colors.par.Color
		
		print(row)

		#debug()