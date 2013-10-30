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

        order_by = data['reorder_current'].extracted
        invert_sortorder = data['reorder_current_invert_checkbox'].extracted
        reorder_msg = None
        if order_by != '---':
            ordering = self.context.getOrdering()
            ordering.orderObjects(order_by, invert_sortorder)
            reorder_msg = _(u"Reordered by '%s'.") % order_by
        else:
            reorder_msg = _("Did no reordering.")

        messages = IStatusMessage(self.request)
        messages.addStatusMessage(_(u"Set folder ordering to '%s'.") %
                                  neworder and neworder or _('default'),
                                  type="info")
        if reorder_msg:
            messages.addStatusMessage(reorder_msg, type="info")

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
        return [('---', _(u'---')),
                ('title', _(u'title')),
                ('id', _(u'short name')),
                ('creation_date', _(u'created')),
                ('modification_date', _(u'last modified'))]
