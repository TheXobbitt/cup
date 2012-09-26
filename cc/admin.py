from django.contrib import admin
from cc.models import ProxyServer, Client, Statistic

class ProxyServerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'ip', ('mem_max', 'cpu_num', 'net_max'), 'is_active')
        }),
        ('Average load', {
            'classes': ('collapse', ),
            'fields': ('av_load', ('mem_load', 'cpu_load', 'net_load'))
        }),
    )
    readonly_fields = ('mem_load', 'cpu_load', 'net_load', 'av_load')
    search_fields = ('name', 'ip')
    list_display = ('name', 'ip', 'av_load', 'is_active')
    actions = ['make_active', 'make_deactive']

    def make_active(modeladmin, request, queryset):
        count = queryset.filter(is_active = False).update(is_active = True)
        modeladmin.message_user(request, u'%s proxy servers activated.' % count)
    make_active.short_description = u'Activate selected proxy servers'

    def make_deactive(modeladmin, request, queryset):
        count = queryset.filter(is_active = True).update(is_active = False)
        modeladmin.message_user(request, u'%s proxy servers deactivated.' % count)
    make_deactive.short_description = u'Deactivate selected proxy servers'

class ClientAdmin(admin.ModelAdmin):
    search_fields = ('domain', 'ip')
    list_display = ('domain', 'is_active')
    list_filter = ('proxy__name', )
    filter_horizontal = ('proxy', )
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

admin.site.register(ProxyServer, ProxyServerAdmin)
admin.site.register(Client, ClientAdmin)
#admin.site.register(Statistic, StatisticAdmin)