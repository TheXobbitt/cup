from django.db import models

class ProxyServer(models.Model):
    name = models.CharField(max_length = 20, verbose_name = u'Node number', help_text = u'Example: Node N, where N = number')
    ip = models.IPAddressField(verbose_name = u'IP address', help_text = u'Example: 10.0.0.1')
    mem_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Memory load', help_text = u'Memory load in percents')
    mem_max = models.IntegerField(verbose_name = u'Memory maximum', help_text = u'In MB. Example: 1024')
    cpu_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'CPU load', help_text = u'CPU load in percents')
    cpu_num = models.IntegerField(verbose_name = u'Number of CPU', help_text = u'Number of cores or processors. Example: 2')
    net_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Network load', help_text = u'Network load in percents')
    net_max = models.IntegerField(verbose_name = u'Network speed', help_text = u'In Mbps. Example: 100')
    av_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Average load', help_text = u'Average load in percents')
    is_active = models.BooleanField(default = True, verbose_name = u'Is active')

    def __unicode__(self):
        return self.name

class Client(models.Model):
    domain = models.CharField(max_length = 100, verbose_name = u'Domain name', help_text = u'Domain name of the client')
    ip = models.CharField(max_length = 100, verbose_name = 'IP addresses', help_text = u'IP addresses of the client servers. Example: 10.0.0.1:10.0.0.2')
    proxy = models.ManyToManyField(ProxyServer, verbose_name = u'Proxy servers')
    is_active = models.BooleanField(default = True, verbose_name = u'Is active')

    def __unicode__(self):
        return '%s;%s;%s' % (self.is_active, self.domain, self.ip)

class Statistic(models.Model):
    node = models.CharField(max_length = 20, verbose_name = u'Node number')
    mem_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Memory load')
    cpu_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'CPU load')
    net_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Network load')
    av_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Average load')
    tcp_conn = models.IntegerField(null = 'True', blank = 'True', verbose_name = u'TCP connections number')
    date = models.DateTimeField(auto_now_add = True, verbose_name = u'Statistic time')