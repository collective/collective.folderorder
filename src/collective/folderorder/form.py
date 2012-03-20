from zope.component import getAdapters
import yafowil.loader
from yafowil.controller import Controller
from yafowil.yaml import parse_from_YAML
from zope.i18nmessageid import MessageFactory
from Products.Five import BrowserView
from plone.folder.interfaces import IOrdering 
from Products.statusmessages.interfaces import IStatusMessage

_ = MessageFactory('collective.folderorder')

class SelectFolderOrderForm(BrowserView):
    
    def form(self):
        form = parse_from_YAML('collective.folderorder:form.yaml', self,  _)
        controller = Controller(form, self.request)
        if not controller.next:
            return controller.rendered
        self.context.REQUEST.response.redirect(controller.next)
        return u''    
    
    def save(self, widget, data):
        neworder = unicode(data['selectedorder'].extracted)
        self.context.setOrdering(neworder)
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(_(u"Set folder ordering to '%s'." % neworder), 
                                  type="info")
                   
    def next(self, request):
        return '%s/select_folder_order' % self.context.absolute_url()
    
    @property
    def action(self):
        return self.next({})     
    
    def currentorder(self):
        currentadapter =  self.context.getOrdering()
        name = [n for n, a in getAdapters((self.context,), IOrdering)  
                if type(a) is type(currentadapter)]
        if len(name) != 1:
            return u''
        return name[0]        
    
    def vocab_ordering(self):
        orderings = [[x[0], _(x[0])] for x in getAdapters((self.context,), IOrdering)]
        for idx in range(0, len(orderings)):
            if not orderings[idx][0]:
                orderings[idx][1] = _('default')
        return orderings
