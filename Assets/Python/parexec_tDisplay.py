# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	if par.name == 'Globaltemperature':
		me.parent().par.Cameratemperature = par
		me.parent().par.Environmenttemperature = par
	elif par.name == 'Globalmagenta':
		me.parent().par.Cameramagenta = par
		me.parent().par.Environmentmagenta = par
	elif par.name == 'Globalintensity':
		me.parent().par.Cameraintensity = par
		me.parent().par.Environmentintensity = par
	elif par.name == 'Trackingmarkers':
		op.Volume.TrackingMarkers(par)
	elif par.name == 'Rendercamera':
		op.tDisplay.RenderCamera(par)
	elif par.name == 'Volumerendermode':
		op.Volume.Mode(par)
	elif par.name == 'Stype':
		if par == 0:
			parent.tDisplay.StypeDisable()
		elif par == 1:
			parent.tDisplay.StypeInit()
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
	if par.name == 'Globaltmireset':
		print('global tmi reset')
		me.parent().par.Globaltemperature = 0
		me.parent().par.Globalmagenta = 0
		me.parent().par.Globalintensity = 0
		me.parent().par.Cameratmireset.pulse()
		me.parent().par.Environmenttmireset.pulse()
	elif par.name == 'Stypereinit':
		parent.tDisplay.StypeInit()
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
	