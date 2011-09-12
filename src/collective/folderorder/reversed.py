from zope.interface import implements
from plone.folder.default import DefaultOrdering

class ReversedOrdering(DefaultOrdering):
    """return reversed ids."""
        
    def idsInOrder(self):
        """ Return all object ids, in the correct order """
        return reversed(super(ReversedOrdering, self).idsInOrder())        