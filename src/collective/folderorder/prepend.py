from plone.folder.default import DefaultOrdering


class PrependOrdering(DefaultOrdering):
    """prepend new added content"""
       
    def notifyAdded(self, id):
        """ 
        Inform the ordering implementation that an item was added 
        """
        order = self._order(True)
        pos = self._pos(True)
        order.insert(0, id)
        pos.clear()
        for n, id in enumerate(order):
            pos[id] = n
