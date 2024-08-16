# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	
	op.Volume.Reinit()
	op.Volume.SetCanvas()
	
	return

def onCreate():
	return

def onExit():
	return

def onFrameStart(frame):
	return

def onFrameEnd(frame):
	return

def onPlayStateChange(state):
	return

def onDeviceChange():
	return

def onProjectPreSave():
	
	op.Camera.saveExternalTox()
	print('camera component saved')
	op.Volume.saveExternalTox()
	print('volume component saved')
	op.Screen_Template.saveExternalTox()
	print('screen component saved')
	
	return

def onProjectPostSave():
	return

	