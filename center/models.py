from django.db import models
from django.contrib.auth.models import User

class Node(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'Node number', help_text=u'Example: Node_N, where N = number')
    color = models.CharField(max_length=7, unique=True, verbose_name=u'Chart color', help_text=u'Example: #FFFFFF')
    ip = models.IPAddressField(verbose_name=u'IP address', help_text=u'Example: 10.0.0.1')
    mem_max = models.IntegerField(verbose_name=u'Memory maximum', help_text=u'In MB. Example: 1024')
    cpu_num = models.IntegerField(verbose_name=u'Number of CPU', help_text=u'Number of cores or processors. Example: 2')
    net_max = models.IntegerField(verbose_name=u'Network speed', help_text=u'In Mbps. Example: 100')
    is_active = models.BooleanField(default=True, verbose_name=u'Is active')

    def __unicode__(self):
        return self.name

class Domain(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100, verbose_name=u'Domain name', help_text=u'Domain name of the client')
    ip = models.CharField(max_length=100, verbose_name='IP addresses', help_text=u'IP addresses of the client servers. Example: 10.0.0.1;10.0.0.2')
    node = models.ManyToManyField(Node, verbose_name=u'Nodes')
    is_active = models.BooleanField(default=True, verbose_name=u'Is active')

    def __unicode__(self):
        return self.name

class Statistic(models.Model):
    node = models.ForeignKey(Node)
    mem_load = models.FloatField(null=True, blank=True)
    cpu_load = models.FloatField(null=True, blank=True)
    net_load = models.FloatField(null=True, blank=True)
    av_load = models.FloatField(null=True, blank=True)
    tcp_conn = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class SiteStatistic(models.Model):
    node = models.ForeignKey(Node)
    site = models.ForeignKey(Domain)
    access = models.IntegerField()
    access_old = models.IntegerField()
    error = models.IntegerField()
    error_old = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class BlackList(models.Model):
    ip = models.IPAddressField(null=False, unique=True, verbose_name=u'IP address')
    node = models.ManyToManyField(Node, verbose_name=u'Nodes')
    is_active = models.BooleanField(default=True, verbose_name=u'Is active')
    date = models.DateTimeField(auto_now=True, verbose_name=u'Last updated')

    def __unicode__(self):
        return self.ip

class TariffSites(models.Model):
    name = models.CharField(max_length=20, unique=True)
    number = models.IntegerField(verbose_name=u'Number of sites')

    def __unicode__(self):
        return self.name

class TariffNodes(models.Model):
    name = models.CharField(max_length=20, unique=True)
    number = models.IntegerField(verbose_name=u'Number of nodes')

    def __unicode__(self):
        return self.name

class TariffWaf(models.Model):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=5, unique=True)

    def __unicode__(self):
        return self.name

class TariffCache(models.Model):
    name = models.CharField(max_length=20, unique=True)
    time = models.IntegerField(verbose_name=u'Time in minutes')

    def __unicode__(self):
        return self.name

class TariffSupport(models.Model):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=5, unique=True)

    def __unicode__(self):
        return self.name

class Tariff(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u'Tariff')
    sites = models.ForeignKey(TariffSites)
    antidos = models.BooleanField(default=True, verbose_name=u'AntiDDoS')
    antiprogs = models.BooleanField(default=True, verbose_name=u'AntiProgs')
    nodes = models.ForeignKey(TariffNodes)
    waf = models.ForeignKey(TariffWaf)
    geoban = models.BooleanField(default=True, verbose_name=u'Geoban support')
    ipban = models.BooleanField(default=True, verbose_name=u'IPban support')
    whitelist = models.BooleanField(default=True, verbose_name=u'Whitelist support')
    cache = models.ForeignKey(TariffCache)
    compression = models.BooleanField(default=False, )
    pictures = models.BooleanField(default=False, )
    support = models.ForeignKey(TariffSupport)

    def __unicode__(self):
        return self.name
