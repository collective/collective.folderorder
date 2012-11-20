from plone.folder.default import DefaultOrdering

class ReversedOrdering(DefaultOrdering):
    """return reversed ids."""

    def idsInOrder(self):
        """ Return all object ids, in the correct order, reversed. """
        return list(reversed(super(ReversedOrdering, self).idsInOrder()))

    def getObjectPosition(self, id):
        """ Get the position of the given id, reversed. """
        pos = self._pos()
        if id in pos:
            pos_ = {}
            # TODO: inefficient for lots of objects in folder
            for (val, key) in enumerate(self.idsInOrder(), start=0):
                # key is object, val is position
                pos_[key] = val
            return pos_[id]
        else:
            raise ValueError('No object with id "%s" exists.' % id)
