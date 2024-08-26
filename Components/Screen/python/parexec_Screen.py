# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	if par.name == 'Wireframe':
			parent.Screen.Wireframe(par.eval())
	elif par.name == 'Frustum':
		parent.Screen.Frustum(par.eval())
	elif par.name == 'Screenspaceopacity':
		parent.Screen.SetScreenspaceOpacity(par.eval())
	elif par.name == 'Screenspacepriority':
		parent.Screen.SetScreenspacePriority(par.eval())
	elif par.name == 'Rendermode':
		parent.Screen.Mode(par)
	elif par.page.name == "Color Grade":
		try:
			op("colorGrade").par[par.name] = par.eval()
		except Exception as e:
			debug(e)
	return

# Called at end of frame with complete list of individual parameter changes.
# The changes are a list of named tuples, where each tuple is (Par, previous value)
def onValuesChanged(changes):
	for c in changes:
		# use par.eval() to get current value
		par = c.par
		prev = c.prev
	return

def onPulse(par):
	#colorGrade
	if par.name == 'Resettmi':
		op('colorGrade').par.Resettmi.pulse()
		parent.Screen.par.Temperature = 0
		parent.Screen.par.Magenta = 0
		parent.Screen.par.Intensity = 0
	elif par.name == 'Resetlgg':
		#trigger colorGrade reset
		op('colorGrade').par.Resetlgg.pulse()
		#set screen values to default
		parent.Screen.parGroup.Liftcolor = (0,0,0)
		parent.Screen.par.Liftlevel = 0
		parent.Screen.parGroup.Gammacolor = (0,0,0)
		parent.Screen.par.Gammalevel = 0
		parent.Screen.parGroup.Gaincolor = (0,0,0)
		parent.Screen.par.Gainlevel = 0
		parent.Screen.parGroup.Offsetcolor = (0,0,0)
		parent.Screen.par.Offsetlevel = 0
		return
	elif par.name == 'Resetsaturation':
		op('colorGrade').par.Resetsaturation.pulse()
		parent.Screen.par.Saturation = 1
		return
	elif par.name == 'Resetall':
		#trigger colorGrade reset
		op('colorGrade').par.Resetall.pulse()
		#set screen values to default
		##TMI
		parent.Screen.par.Temperature = 0
		parent.Screen.par.Magenta = 0
		parent.Screen.par.Intensity = 0
		
		##LGG
		parent.Screen.parGroup.Liftcolor = (0,0,0)
		parent.Screen.par.Liftlevel = 0
		parent.Screen.parGroup.Gammacolor = (0,0,0)
		parent.Screen.par.Gammalevel = 0
		parent.Screen.parGroup.Gaincolor = (0,0,0)
		parent.Screen.par.Gainlevel = 0
		parent.Screen.parGroup.Offsetcolor = (0,0,0)
		parent.Screen.par.Offsetlevel = 0
		
		##saturation
		parent.Screen.par.Saturation = 1
		
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	