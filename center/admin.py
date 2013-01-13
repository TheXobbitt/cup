from django.contrib import admin
from center.models import Node, Domain, Statistic, SiteStatistic, BlackList, Tariff, TariffSites, TariffNodes, TariffWaf, TariffCache, TariffSupport

class NodeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'color', 'ip', ('mem_max', 'cpu_num', 'net_max'), 'is_active')
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

class DomainAdmin(admin.ModelAdmin):
    search_fields = ('name', 'ip')
    list_display = ('name', 'is_active')
    list_filter = ('node__name', )
    filter_horizontal = ('node', )
    actions = ['make_active', 'make_deactive']

    def make_active(modeladmin, request, queryset):
        count = queryset.filter(is_active = False).update(is_active = True)
        modeladmin.message_user(request, u'%s domains activated.' % count)
    make_active.short_description = u'Activate selected domains'

    def make_deactive(modeladmin, request, queryset):
        count = queryset.filter(is_active = True).update(is_active = False)
        modeladmin.message_user(request, u'%s domains deactivated.' % count)
    make_deactive.short_description = u'Deactivate selected domains'

class StatisticAdmin(admin.ModelAdmin):
    search_fields = ('node', )
    list_display = ('node', 'mem_load', 'cpu_load', 'net_load', 'av_load', 'tcp_conn', 'date')
    readonly_fields = ('node', 'mem_load', 'cpu_load', 'net_load', 'av_load', 'tcp_conn', 'date')
    list_filter = ('node', )

class SiteStatisticAdmin(admin.ModelAdmin):
    search_fields = ('node', 'site')
    list_display = ('node', 'site', 'access', 'error', 'date')
    readonly_fields = ('node', 'site', 'access', 'access_old', 'error', 'error_old')
    list_filter = ('node', 'site')

class BlackListAdmin(admin.ModelAdmin):
    search_fields = ('ip', )
    list_display = ('ip', 'is_active')
    readonly_fields = ('ip', 'node')
    list_filter = ('node__name', )
    actions = ['make_deactive']

    def make_deactive(modeladmin, request, queryset):
        count = queryset.filter(is_active = True).update(is_active = False)
        modeladmin.message_user(request, u'%s IP addresses deactivated.' % count)
    make_deactive.short_description = u'Deactivate selected IP address'

class TariffSitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')

class TariffNodesAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')

class TariffWafAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

class TariffCacheAdmin(admin.ModelAdmin):
    list_display = ('name', 'time')

class TariffSupportAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

class TariffAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'sites', 'antidos', 'antiprogs', 'nodes', 'waf', 'geoban', 'ipban', 'whitelist', 'cache', 'compression', 'pictures', 'support')

admin.site.register(Node, NodeAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(SiteStatistic, SiteStatisticAdmin)
admin.site.register(BlackList, BlackListAdmin)
admin.site.register(TariffSites, TariffSitesAdmin)
admin.site.register(TariffNodes, TariffNodesAdmin)
admin.site.register(TariffWaf, TariffWafAdmin)
admin.site.register(TariffCache, TariffCacheAdmin)
admin.site.register(TariffSupport, TariffSupportAdmin)
admin.site.register(Tariff, TariffAdmin)
