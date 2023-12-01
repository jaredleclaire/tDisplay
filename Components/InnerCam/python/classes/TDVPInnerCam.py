
class TDVPInnerCam:
    """
    TDVPInnerCam description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def ShowLabel(self, show):
        op("text_label").bypass = not show

    def ShowBorder(self, show):
        op("rectangle_border").bypass = not show

    def ShowKeyingScreen(self, show):
        op("constant_green_screen").bypass = not show

    def ExposureStopAdjust(self, stop, intensityOffset):
        intensity = 1 + intensityOffset
        self.ownerComp.par.I = self.exposureStopAdjust(stop, intensity)

    def exposureStopAdjust(stops, intensity):
        return intensity * 2**stops - 1
