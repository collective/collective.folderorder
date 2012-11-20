from plone.folder.default import DefaultOrdering
from zope.container.contained import notifyContainerModified

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


    # re-implementing to support correct object moves

    def moveObjectsByDelta(self, ids, delta, subset_ids=None,
            suppress_events=False):
        """ Move the specified ids (a sequence, or a single string id)
            by the given delta (a positive or negative number). By
            default, this moves the objects within the whole set of
            sub-items in the context container, but if subset_ids is
            specified, it gives a subset of ids to consider.
            Should return the number of objects that changed position. """
        # changes for reverse ordering are marked with "# reversed"
        delta = -delta # reversed
        order = self._order()
        pos = self._pos()
        min_position = 0
        if isinstance(ids, basestring):
            ids = [ids]
        if subset_ids is None:
            # delegate to default implementation
            subset_ids = super(ReversedOrdering, self).idsInOrder() # reversed
        elif not isinstance(subset_ids, list):
            subset_ids = list(subset_ids)
        subset_ids.reverse() # reversed
        if delta > 0:                   # unify moving direction
            ids = reversed(ids)
            subset_ids.reverse()
        counter = 0
        for id in ids:
            try:
                old_position = subset_ids.index(id)
            except ValueError:
                continue
            new_position = max(old_position - abs(delta), min_position)
            if new_position == min_position:
                min_position += 1
            if not old_position == new_position:
                subset_ids.remove(id)
                subset_ids.insert(new_position, id)
                counter += 1
        if counter > 0:
            if delta > 0:
                subset_ids.reverse()
            idx = 0
            for i in range(len(order)):
                if order[i] in subset_ids:
                    id = subset_ids[idx]
                    try:
                        order[i] = id
                        pos[id] = i
                        idx += 1
                    except KeyError:
                        raise ValueError('No object with id "%s" exists.' % id)
        if not suppress_events:
            notifyContainerModified(self.context)
        return counter
