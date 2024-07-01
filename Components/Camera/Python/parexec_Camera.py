# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
#
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.


def onValueChange(par, prev):
    # use par.eval() to get current value
    if par.name == 'Label':
        parent.Camera.Label(par.eval())
    elif par.name == 'Border':
        parent.Camera.Border(par.eval())
    elif par.name == 'Keyingscreen':
        parent.Camera.KeyingScreen(par.eval())
    elif par.name == 'Depthoffield':
    	if par.eval() == False:
    		parent.Camera.DisableDoF()
    	elif par.eval() == True:
    		parent.Camera.EnableDoF()
    elif par.name == 'Frustum':
    	parent.Camera.Frustum(par.eval())
    	
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
	return
	
	
def onExpressionChange(par, val, prev):
    return
    

def onExportChange(par, val, prev):
    return


def onEnableChange(par, val, prev):
    return


def onModeChange(par, val, prev):
    return
