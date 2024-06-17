# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	if par.name == 'Liftlevel':
		parent.lgg.parGroup.Liftcolor = par.eval()
	if par.name == 'Gammalevel':
		parent.lgg.parGroup.Gammacolor = par.eval()
	if par.name == 'Gainlevel':
		parent.lgg.parGroup.Offsetcolor = par.eval()
	if par.name == 'Offsetlevel':
		parent.lgg.parGroup.Offsetcolor = par.eval()
	
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
	
	me.parent().Reset()
	
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	