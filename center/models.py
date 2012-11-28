from django.db import models

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

class BlackList(models.Model):
    ip = models.IPAddressField(null=False, unique=True, verbose_name=u'IP address')
    node = models.ManyToManyField(Node, verbose_name=u'Nodes')
    is_active = models.BooleanField(default=True, verbose_name=u'Is active')
    date = models.DateTimeField(auto_now=True, verbose_name=u'Last updated')

    def __unicode__(self):
        return self.ip

class Tariff(models.Model):
    ANTIDOS = (
        ('5', '5 nodes'),
        ('10', '10 nodes'),
        ('15', '15 nodes'),
    )
    CACHE = (
        ('1440', '1 day'),
        ('60', '1 hour'),
        ('10', '10 minutes'),
    )
    WAF = (
        ('no', 'No'),
        ('yes', 'Standart'),
        ('custom', 'Custom'),
    )
    SUPPORT = (
        ('tick', 'Tickets'),
        ('tel', 'Tickets, Telephone'),
        ('adm', 'Tickets, Telephone, Admin')
    )
    name = models.CharField(max_length=50, unique=True, verbose_name=u'Tariff')
    antidos = models.CharField(max_length=2, choices=ANTIDOS, verbose_name=u'Antidos support')
    cache = models.CharField(max_length=4, choices=CACHE, verbose_name=u'Cache update time')
    compression = models.BooleanField(default=False, verbose_name=u'Compression')
    waf = models.CharField(max_length=6, choices=WAF, verbose_name=u'WAF')
    monitoring = models.BooleanField(default=False, verbose_name=u'Monitoring')
    geoban = models.BooleanField(default=False, verbose_name=u'Geoban support')
    support = models.CharField(max_length=4, choices=SUPPORT, verbose_name=u'Support')

    def __unicode__(self):
        return self.name
