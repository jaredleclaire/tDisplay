class CamVP:
    """
    TDVPCamInner description
    """

    def __init__(self, ownerComp):
        # The component to which this extension is attached
        self.ownerComp = ownerComp

    def ShowLabel(self):
        op("label").bypass = False

    def HideLabel(self):
        op("label").bypass = True

    def ShowBorder(self):
        op("border").bypass = False

    def HideBorder(self):
        op("border").bypass = True

    def ShowKeyingScreen(self):
        op("chroma_screen").bypass = False

    def HideKeyingScreen(self):
        op("chroma_screen").bypass = True
