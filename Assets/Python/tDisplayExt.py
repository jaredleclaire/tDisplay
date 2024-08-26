from TDStoreTools import StorageManager
import TDFunctions as TDF

class tDisplayExt:
	"""
	tDisplayExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		
	def RenderCamera(self, state):
		#sets state of camera render and frustum
		op.Camera.display = state
		op.Camera.allowCooking = state
		# op('null_cameraParent').display = state
		
	def RenderMode(self, mode):
		#switches rendering system mode
		op.Volume.Mode(mode)
		
	def StypeInit(self):
		#checks if a stype CHOP has been specified and creates exports for tracking channels		
		chop = op(str(parent.tDisplay.par.Stypechop))
		
		if chop != None:
			#set focal depth
			op.tDisplay.par.Focaldepth.mode = ParMode.EXPRESSION
			op.tDisplay.par.Focaldepth.expr = f"op({str(chop)})['focus_distance']"
			
			#set camera fov
			op.tDisplay.par.Camerafov.mode = ParMode.EXPRESSION
			op.tDisplay.par.Camerafov.expr = f"op({str(chop)})['padded_fov']"
			
			#set camera transform
			op.tDisplay.par.Cameratransformx.mode = ParMode.EXPRESSION
			op.tDisplay.par.Cameratransformx.expr = f"op({str(chop)})['tx']"
			
			op.tDisplay.par.Cameratransformy.mode = ParMode.EXPRESSION
			op.tDisplay.par.Cameratransformy.expr = f"op({str(chop)})['ty']"
			
			op.tDisplay.par.Cameratransformz.mode = ParMode.EXPRESSION
			op.tDisplay.par.Cameratransformz.expr = f"op({str(chop)})['tz']"
			
			#set camera rotate
			op.tDisplay.par.Camerarotatex.mode = ParMode.EXPRESSION
			op.tDisplay.par.Camerarotatex.expr = f"op({str(chop)})['rx']"
			
			op.tDisplay.par.Camerarotatey.mode = ParMode.EXPRESSION
			op.tDisplay.par.Camerarotatey.expr = f"op({str(chop)})['ry']"
			
			op.tDisplay.par.Camerarotatez.mode = ParMode.EXPRESSION
			op.tDisplay.par.Camerarotatez.expr = f"op({str(chop)})['rz']"

		else:
			raise Exception('no Stype CHOP specified')
			
	def StypeDisable(self):
		
		#set focal depth
		op.tDisplay.par.Focaldepth.mode = ParMode.CONSTANT
			
		#set camera fov
		op.tDisplay.par.Camerafov.mode = ParMode.CONSTANT
			
		#set camera transform
		op.tDisplay.par.Cameratransformx.mode = ParMode.CONSTANT
			
		op.tDisplay.par.Cameratransformy.mode = ParMode.CONSTANT
			
		op.tDisplay.par.Cameratransformz.mode = ParMode.CONSTANT
			
		#set camera rotate
		op.tDisplay.par.Camerarotatex.mode = ParMode.CONSTANT
			
		op.tDisplay.par.Camerarotatey.mode = ParMode.CONSTANT
			
		op.tDisplay.par.Camerarotatez.mode = ParMode.CONSTANT