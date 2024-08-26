from TDStoreTools import StorageManager
import TDFunctions as TDF

class Screen:
	"""
	Screen description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def DebugOverlay(self, state):		
		op('base_debugOverlay').par.Enable = state
		# debug(state)

	def TrackingMarkers(self, state):
		op('level_markerOpacity').par.opacity = state
		# debug(state)

	def BoundingBox(self, state):

		op('null_boundsPoint0').display = state
		op('null_boundsPoint1').display = state
		op('null_boundsPoint2').display = state
		op('null_boundsPoint3').display = state
		op('null_boundsPoint4').display = state
		op('null_boundsPoint5').display = state
		op('null_boundsPoint6').display = state
		op('null_boundsPoint7').display = state

		op('null_boundingBox').display = state

		#debug(state)

	def UpdateProjMatrix(self):
		m = tdu.Matrix()

		#default projection matrix parameters
		cam = op('cam_outer_reference')
		render = op('render_outerPerspective')
		fovX = cam.par.fov
		aspectX = render.par.resolutionw
		aspectY = render.par.resolutionh
		near = cam.par.near
		far = cam.par.far
		
		#crop values
		'''
		cropLeft = op('null_crop')['left']
		cropRight = op('null_crop')['right']
		cropBottom =op('null_crop')['bottom']
		cropTop = op('null_crop')['top']
		'''
		cropLeft = op('geo_dynamicFrustum').par.Minimumsx
		cropRight = op('geo_dynamicFrustum').par.Maximumsx
		cropBottom = op('geo_dynamicFrustum').par.Minimumsy
		cropTop = op('geo_dynamicFrustum').par.Maximumsy
		
		#re-scale factor calc
		scaleX = 1 / (cropRight - cropLeft)
		scaleY = 1 / (cropTop - cropBottom)
		
		#convert original matrix to projection matrix with default pars
		m.projectionFovX(fovX, aspectX, aspectY, near, far)
		
		#crop to bounding box
			
		m.scale(0.5,0.5,1.0)
			
		m.translate(0.5,0.5,0.0)
			
		m.translate((cropLeft * -1),(cropBottom * -1),0)
			
		m.scale( scaleX , scaleY, 1 )
			
		m.translate(-0.5,-0.5,0.0)
			
		m.scale(2.0,2.0,1.0)
			
		m.fillTable(op('table_projMat'))
		
		#debug(v)
		
	def SetDefaultColor(self):
		num = parent.Screen.digits % 10
	
		r = eval('op.Colors.par.Color' + str(num) + 'r')
		g = eval('op.Colors.par.Color' + str(num) + 'g')
		b = eval('op.Colors.par.Color' + str(num) + 'b')
		a = eval('op.Colors.par.Color' + str(num) + 'a')
		
		parent.Screen.par.Screencolorr = r
		parent.Screen.par.Screencolorg = g
		parent.Screen.par.Screencolorb = b
		parent.Screen.par.Screenalpha = a
		
		parent.Screen.color = (r,g,b)

		#debug()
	
	def Wireframe(self, state):
		op('geo_wireframe').render = state		
		if state:
			print(parent.Screen.name + ' wireframe enabled')
		else:
			print(parent.Screen.name + ' wireframe disabled')

	def Frustum(self, state):
		op('FrustumVisualizer').display = state
		if state:
			print(parent.Screen.name + ' frustum enabled')
		else:
			print(parent.Screen.name + ' frustum disabled')
		
	def SetScreenspacePriority(self, mode):
		if mode == 'middle':
			op('select_layer1').par.top = 'out_inner'
			op('select_layer2').par.top = 'out_canvas'
			op('select_layer3').par.top = 'out_outer'
		elif mode == 'top':
			op('select_layer1').par.top = 'out_canvas'
			op('select_layer2').par.top = 'out_inner'
			op('select_layer3').par.top = 'out_outer'
			
		print(parent.Screen.name + ' screenspace priority set to ' + mode)
		
	def SetScreenspaceOpacity(self, opacity):
		parent.Screen.par.Screenspaceopacity = opacity
		
	#sets render mode for the screen object. will be deprecated soon
	def Mode(self, mode):
		if mode == '3D':
			op('level_inner').par.opacity = 1
			op('geo_projection').par.material = 'glsl_innerProj'
		if mode == '360':
			op('level_inner').par.opacity = 0
			op('geo_projection').par.material = 'constant_360'
		
		return
		
	#sets screen space canvas crop crop settings based on config values and relevant resolution multipliers
	def SetCanvas(self):
		
		#get canvas mapping from Volume Config
		canvas_mapping_x = parent.Screen.par.Canvasmappingx
		canvas_mapping_y = parent.Screen.par.Canvasmappingy
		
		#get canvas resolution
		canvas_res_w = op('select_canvas').width
		canvas_res_h = op('select_canvas').height
		
		#get screen native resolution
		screen_res_w = parent.Screen.par.Screenresolutionw
		screen_res_h = parent.Screen.par.Screenresolutionh
		
		#get screen render resolution multiplier
		screen_res_mult = parent.Screen.par.Resolutionmultiplier
		
		#get project global resolution multiplier
		global_res_mult = [0.25, 0.5, 1, 2][ui.preferences['tops.globalresize']]
		
		#normalize screen resolution based on multipliers
		norm_res_w = screen_res_w * global_res_mult * screen_res_mult
		norm_res_h = screen_res_h * global_res_mult * screen_res_mult
		
		#set crop values
		op('crop_canvas').par.cropleft = canvas_mapping_x * screen_res_mult * global_res_mult
		op('crop_canvas').par.cropright = ( screen_res_w + canvas_mapping_x ) * screen_res_mult * global_res_mult
		op('crop_canvas').par.cropbottom = canvas_mapping_y * screen_res_mult * global_res_mult
		op('crop_canvas').par.croptop = ( screen_res_h + canvas_mapping_y ) * screen_res_mult * global_res_mult
		
		#print to console
		print(parent.Screen.name + ' canvas set')
		
		return
		
