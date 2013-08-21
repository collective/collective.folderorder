from zope.component import getAdapters
from yafowil.controller import Controller
from yafowil.yaml import parse_from_YAML
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from plone.folder.interfaces import IOrdering
from Products.statusmessages.interfaces import IStatusMessage

_ = MessageFactory('collective.folderorder')


def current_order_name(context):
    """Return the name of the current ordering.
    :param context: The context, for the ordering name should be returned.
    :returns: Name of the ordering resp. the named IOrdering adapter.
    :rtype: string

    """
    currentadapter = context.getOrdering()
    name = [n for n, a in getAdapters((context,), IOrdering)
            if type(a) is type(currentadapter)]
    if len(name) != 1:
        return u''
    return name[0]

def orderings_list(context):
    """Return ordering names as list.
    :param context: The content context to create the orderings list on.
    :returns: List of ordering names.
    :rtype: Python list

    """
    adapters = getAdapters((context,), IOrdering)
    def make_trans(term):
        if not term:
            return _('default')
        else:
            return _(term)
    orderings = [[x[0], make_trans(x[0])] for x in adapters]
    return orderings

class SelectFolderOrderForm(BrowserView):

    def form(self):
        form = parse_from_YAML('collective.folderorder:form.yaml', self, _)
        controller = Controller(form, self.request)
        if not controller.next:
            return controller.rendered
        self.context.REQUEST.response.redirect(controller.next)
        return u''

    def save(self, widget, data):
        neworder = unicode(data['selectedorder'].extracted)
        self.context.setOrdering(neworder)
        ordering = self.context.getOrdering()

        order_by = data['reorder_current'].extracted
        invert_sortorder = data['reorder_current_invert_checkbox'].extracted
        if order_by != '---':
            ordering.orderObjects(order_by, invert_sortorder)

        msg = neworder and neworder or _('default')
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(_(u"Set folder ordering to '%s'." % msg),
                                  type="info")

    def next(self, request):
        return '%s/select_folder_order' % self.context.absolute_url()

    @property
    def action(self):
        return self.next({})

    def currentorder(self):
        return current_order_name(self.context)

    def vocab_ordering(self):
        return orderings_list(self.context)

    def vocab_reorder(self):
        vocab = [('---', _(u'---')),
                 ('creation_date', _(u'created')),
                 ('title', _(u'title')),
                 ('id', _(u'short name')),
                 ('modification_date', _(u'last modified'))]

        return vocab
