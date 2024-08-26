# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.
Utils = mod(op.Utils.op("Utils"))

def onValueChange(par, prev):
	# use par.eval() to get current value
	children = parent.Volume.findChildren(name='Screen*',depth=1)
	for child in children:
		try:
			Utils.CopyOnePar(parent.Volume, child, par.name)
		except Exception as e:
			# debug(e)
			pass

	if par.name == 'Screenspaceopacity':
		parent.Volume.SetScreenspaceOpacity(par.eval())
	elif par.name == 'Screenspacepriority':
		parent.Volume.SetScreenspacePriority(par.eval())
	elif par.name == 'Rendermode':
		parent.Volume.Mode(par)

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
		# set volume values to default
		parent.Volume.par.Temperature = 0
		parent.Volume.par.Magenta = 0
		parent.Volume.par.Intensity = 0
	elif par.name == 'Resetlgg':
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
		# set volume values to default
		parent.Volume.par.Saturation = 1
		return
	elif par.name == 'Resetall':
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
	elif par.name == 'EnvironmentResolution':
		w = parent.Volume.par.Environmentresolutionw
		h = parent.Volume.par.Environmentresolutionh
		parent.Volume.SetEnvResolution(w,h)
	
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	