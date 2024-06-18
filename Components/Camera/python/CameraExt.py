class Camera:
    """
    TDVPCamInner description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def ShowLabel(self):
        op("label").bypass = False
        print('camera label enabled')

    def HideLabel(self):
        op("label").bypass = True
        print('camera label disabled')

    def ShowBorder(self):
        op("border").bypass = False
        print('camera border enabled')

    def HideBorder(self):
        op("border").bypass = True
        print('camera border disabled')

    def ShowKeyingScreen(self):
        op("chroma_screen").bypass = False
        print('camera keying screen enabled')

    def HideKeyingScreen(self):
        op("chroma_screen").bypass = True
        print('camera keying screen disabled')
        
    def ShowFrustum(self):
    	op('FrustumVisualizer').display = True
    	print('camera frustum visualizer enabled')
    	
    def HideFrustum(self):
    	op('FrustumVisualizer').display = False
    	print('camera frustum visualizer disabled')
    	
    def EnableDoF(self):
    	op('Swaggy_Bokeh_v1_0').allowCooking = True
    	op('switch_DoF').par.index = 1
    	print('depth of field enabled')
    
    def DisableDoF(self):
    	op('Swaggy_Bokeh_v1_0').allowCooking = False
    	op('switch_DoF').par.index = 0
    	print('depth of field disabled')
    	
    def ShowAll(self):
    	parent.Camera.ShowBorder()
    	parent.Camera.ShowFrustum()
    	parent.Camera.ShowLabel()
    	
    	parent.Camera.par.Showborder = 1
    	parent.Camera.par.Showfrustum = 1
    	parent.Camera.par.Showlabel = 1
    	
    	print('all camera helpers enabled')
    
    def HideAll(self):
    	parent.Camera.HideBorder()
    	parent.Camera.HideFrustum()
    	parent.Camera.HideLabel()
    	
    	parent.Camera.par.Showborder = 0
    	parent.Camera.par.Showfrustum = 0
    	parent.Camera.par.Showlabel = 0
    	
    	print('all camera helpers disabled')
    	
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
