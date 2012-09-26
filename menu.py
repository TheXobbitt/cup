from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks(),
            items.MenuItem(_('Administration'),
                children = [
                    items.MenuItem(_('Clients'), '/admin/cc/client/'),
                    items.MenuItem(_('Proxy servers'), '/admin/cc/proxyserver/'),
                ]
            )
#            items.AppList(
#                _('Administration'),
#                models=('django.contrib.*',)
#            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)