from django.contrib import admin
from cc.models import Node, Client, Statistic, BlackList

class NodeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'ip', ('mem_max', 'cpu_num', 'net_max'), 'is_active')
        }),
    )
    search_fields = ('name', 'ip')
    list_display = ('name', 'ip', 'is_active')
    actions = ['make_active', 'make_deactive']

    def make_active(modeladmin, request, queryset):
        count = queryset.filter(is_active = False).update(is_active = True)
        modeladmin.message_user(request, u'%s nodes activated.' % count)
    make_active.short_description = u'Activate selected nodes'

    def make_deactive(modeladmin, request, queryset):
        count = queryset.filter(is_active = True).update(is_active = False)
        modeladmin.message_user(request, u'%s nodes deactivated.' % count)
    make_deactive.short_description = u'Deactivate selected nodes'

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('domain', 'ip')
    list_display = ('domain', 'is_active')
    list_filter = ('node__name', )
    filter_horizontal = ('node', )
    actions = ['make_active', 'make_deactive']

    def make_active(modeladmin, request, queryset):
        count = queryset.filter(is_active = False).update(is_active = True)
        modeladmin.message_user(request, u'%s clients activated.' % count)
    make_active.short_description = u'Activate selected clients'

    def make_deactive(modeladmin, request, queryset):
        count = queryset.filter(is_active = True).update(is_active = False)
        modeladmin.message_user(request, u'%s clients deactivated.' % count)
    make_deactive.short_description = u'Deactivate selected clients'

class StatisticAdmin(admin.ModelAdmin):
    search_fields = ('node', )
    list_display = ('node', 'mem_load', 'cpu_load', 'net_load', 'av_load', 'tcp_conn', 'date')
    readonly_fields = ('node', 'mem_load', 'cpu_load', 'net_load', 'av_load', 'tcp_conn', 'date')
    list_filter = ('node', )

class BlackListAdmin(admin.ModelAdmin):
    search_fields = ('ip', )
    list_display = ('ip', )
    readonly_fields = ('ip', 'node')
    list_filter = ('node__name', )

admin.site.register(Node, NodeAdmin)
admin.site.register(Client, ClientAdmin)
#admin.site.register(Statistic, StatisticAdmin)
admin.site.register(BlackList, BlackListAdmin)