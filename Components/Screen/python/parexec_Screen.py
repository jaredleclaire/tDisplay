# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	
	if par.name == 'Wireframe':
		if par.eval() == True:
			parent.Screen.Wireframe(True)
		elif par.eval() == False:
			parent.Screen.Wireframe(False)
	elif par.name == 'Frustum':
		if par.eval() == True:
			parent.Screen.Frustum(True)
		elif par.eval() == False:
			parent.Screen.Frustum(False)
	elif par.name == 'Screenspaceopacity':
		parent.Screen.SetScreenspaceOpacity(par.eval())
	elif par.name == 'Screenspacepriority':
		parent.Screen.SetScreenspacePriority(par.eval())
	elif par.name == 'Rendermode':
		parent.Screen.Mode(par)\
	#colorGrade
	##TMI
	elif par.name == 'Temperature':
		op('colorGrade').par.Temperature = par
	elif par.name == 'Magenta':
		op('colorGrade').par.Magenta = par
	elif par.name == 'Intensity':
		op('colorGrade').par.Intensity = par
	##LGG
	elif par.name == 'Liftcolorr':
		op('colorGrade').par.Liftcolorr = par
	elif par.name == 'Liftcolorg':
		op('colorGrade').par.Liftcolorg = par
	elif par.name == 'Liftcolorb':
		op('colorGrade').par.Liftcolorb = par
	elif par.name == 'Liftlevel':
		op('colorGrade').par.Liftlevel = par
	elif par.name == 'Gammacolorr':
		op('colorGrade').par.Gammacolorr = par
	elif par.name == 'Gammacolorg':
		op('colorGrade').par.Gammacolorg = par
	elif par.name == 'Gammacolorb':
		op('colorGrade').par.Gammacolorb = par
	elif par.name == 'Gammalevel':
		op('colorGrade').par.Gammalevel = par
	elif par.name == 'Gaincolorr':
		op('colorGrade').par.Gaincolorr = par
	elif par.name == 'Gaincolorg':
		op('colorGrade').par.Gaincolorg = par
	elif par.name == 'Gaincolorb':
		op('colorGrade').par.Gaincolorb = par
	elif par.name == 'Gainlevel':
		op('colorGrade').par.Gainlevel = par
	elif par.name == 'Offsetcolorr':
		op('colorGrade').par.Offsetcolorr = par
	elif par.name == 'Offsetcolorg':
		op('colorGrade').par.Offsetcolorg = par
	elif par.name == 'Offsetcolorb':
		op('colorGrade').par.Offsetcolorb = par
	elif par.name == 'Offsetlevel':
		op('colorGrade').par.Offsetlevel = par
	##saturation
	elif par.name == 'Saturation':
		op('colorGrade').par.Saturation = par
		
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
	else:
		pass
		
		return
		
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	