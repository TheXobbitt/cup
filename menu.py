from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks(),
            items.MenuItem(_('Users and tariffs'),
                children = [
                    items.MenuItem(_('Users'), '/admin/auth/user/'),
                    items.MenuItem(_('Tariffs'), '/admin/center/tariff/'),
                ]
            ),
            items.MenuItem(_('Nodes and domains'),
                children = [
                    items.MenuItem(_('Nodes'), '/admin/center/node/'),
                    items.MenuItem(_('Domains'), '/admin/center/domain/'),
                ]
            ),
            items.MenuItem(_('Administration'),
                children = [
                    items.MenuItem(_('Black list'), '/admin/center/blacklist/'),
                ]
            ),
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)