class Camera:
	"""
	TDVPCamInner description
	"""

	def __init__(self, ownerComp):
	# The component to which this extension is attached
		self.ownerComp = ownerComp

	def Label(self, state):
		op('label').bypass = not state

	def Border(self, state):
		op('border').bypass = not state

	def KeyingScreen(self, state):
		op('chroma_screen').bypass = not state

	def Frustum(self, state):
		op('FrustumVisualizer').display = state

	def EnableDoF(self):
		op('Swaggy_Bokeh_v1_0').allowCooking = True
		op('switch_DoF').par.index = 1
		print('depth of field enabled')

	def DisableDoF(self):
		op('Swaggy_Bokeh_v1_0').allowCooking = False
		op('switch_DoF').par.index = 0
		print('depth of field disabled')

	def Bloom(self, state):
		op('bloom_camera').bypass = not state

	def FOVtoThrow(self, fov):
		#incomplete
		import math

		distance = parent.Camera.par.Focaldepth

		angle = 180 - ( ( fov / 2 ) + 90 )
		print('angle = ' + str(angle))

		hypot = ( distance / math.sin( angle ) * 2 )
		print('hypot = ' + str(hypot))

		width = math.sqrt( pow(hypot,2) - pow(distance,2) ) * 2
		print('width = ' + str(width))

		throw = distance / width
		print('throw = ' + str(throw))

		return throw

	def ThrowToFOV(self, throw):
		import math

		fov = math.degrees( math.atan( 0.5 * ( 1 / throw ) ) * 2 )

		return fov
