# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	# helpers
	if par.name == 'Debugoverlays':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Debugoverlay = par.eval()
	elif par.name == 'Trackingmarkers':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Trackingmarkers = par.eval()
		parent.Volume.par.Trackingmarkers = par.eval()
	elif par.name == 'Wireframe':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Wireframe = par.eval()
	elif par.name == 'Frustums':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Frustum = par.eval()
	# screen space
	elif par.name == 'Screenspaceopacity':
		parent.Volume.SetScreenspaceOpacity(par.eval())
	elif par.name == 'Screenspacepriority':
		parent.Volume.SetScreenspacePriority(par.eval())
	elif par.name == 'Rendermode':
		parent.Volume.Mode(par)
		
	# colorGrade
	## TMI
	elif par.name == 'Temperature':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Temperature = par
	elif par.name == 'Magenta':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Magenta = par
	elif par.name == 'Intensity':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Intensity = par
	## LGG
	elif par.name == 'Liftcolorr':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Liftcolorr = par
	elif par.name == 'Liftcolorg':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Liftcolorg = par
	elif par.name == 'Liftcolorb':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Liftcolorb = par
	elif par.name == 'Liftlevel':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Liftlevel = par
	elif par.name == 'Gammacolorr':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gammacolorr = par
	elif par.name == 'Gammacolorg':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gammacolorg = par
	elif par.name == 'Gammacolorb':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gammacolorb = par
	elif par.name == 'Gammalevel':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gammalevel = par
	elif par.name == 'Gaincolorr':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gaincolorr = par
	elif par.name == 'Gaincolorg':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gaincolorg = par
	elif par.name == 'Gaincolorb':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gaincolorb = par
	elif par.name == 'Gainlevel':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Gainlevel = par
	elif par.name == 'Offsetcolorr':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Offsetcolorr = par
	elif par.name == 'Offsetcolorg':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Offsetcolorg = par
	elif par.name == 'Offsetcolorb':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Offsetcolorb = par
	elif par.name == 'Offsetlevel':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Offsetlevel = par
	## saturation
	elif par.name == 'Saturation':
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Saturation = par
	
	else:
		pass

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
	# re-init
	if par.name == 'Reinit':
		op.Volume.Reinit()
		
	# colorGrade
	if par.name == 'Resettmi':
		# trigger colorGrade reset
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Resettmi.pulse()
		# set volume values to default
		parent.Volume.par.Temperature = 0
		parent.Volume.par.Magenta = 0
		parent.Volume.par.Intensity = 0
	elif par.name == 'Resetlgg':
		# trigger colorGrade reset
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Resetlgg.pulse()
		# set volume values to default
		parent.Volume.parGroup.Liftcolor = (0,0,0)
		parent.Volume.par.Liftlevel = 0
		parent.Volume.parGroup.Gammacolor = (0,0,0)
		parent.Volume.par.Gammalevel = 0
		parent.Volume.parGroup.Gaincolor = (0,0,0)
		parent.Volume.par.Gainlevel = 0
		parent.Volume.parGroup.Offsetcolor = (0,0,0)
		parent.Volume.par.Offsetlevel = 0
		return
	elif par.name == 'Resetsaturation':
		# trigger colorGrade reset
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Resetsaturation.pulse()
		# set volume values to default
		parent.Volume.par.Saturation = 1
		return
	elif par.name == 'Resetall':
		# trigger colorGrade reset
		children = parent.Volume.findChildren(name='Screen*',depth=1)
		for c in children:
			c.par.Resetall.pulse()
		# set volume values to default
		## TMI
		parent.Volume.par.Temperature = 0
		parent.Volume.par.Magenta = 0
		parent.Volume.par.Intensity = 0
		
		## LGG
		parent.Volume.parGroup.Liftcolor = (0,0,0)
		parent.Volume.par.Liftlevel = 0
		parent.Volume.parGroup.Gammacolor = (0,0,0)
		parent.Volume.par.Gammalevel = 0
		parent.Volume.parGroup.Gaincolor = (0,0,0)
		parent.Volume.par.Gainlevel = 0
		parent.Volume.parGroup.Offsetcolor = (0,0,0)
		parent.Volume.par.Offsetlevel = 0
		
		## saturation
		parent.Volume.par.Saturation = 1
	
	else:
		pass
	
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	