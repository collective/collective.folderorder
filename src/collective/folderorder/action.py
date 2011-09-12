from plone.folder.interfaces import IOrderableFolder
from Products.Five import BrowserView

class ActionAvailableView(BrowserView):
    
    def __call__(self):
        return IOrderableFolder.providedBy(self.context)