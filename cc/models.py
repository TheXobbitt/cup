from django.db import models

class Node(models.Model):
    name = models.CharField(max_length = 20, unique = 'True', verbose_name = u'Node number', help_text = u'Example: Node_N, where N = number')
    ip = models.IPAddressField(verbose_name = u'IP address', help_text = u'Example: 10.0.0.1')
    mem_max = models.IntegerField(verbose_name = u'Memory maximum', help_text = u'In MB. Example: 1024')
    cpu_num = models.IntegerField(verbose_name = u'Number of CPU', help_text = u'Number of cores or processors. Example: 2')
    net_max = models.IntegerField(verbose_name = u'Network speed', help_text = u'In Mbps. Example: 100')
    is_active = models.BooleanField(default = True, verbose_name = u'Is active')

    def __unicode__(self):
        return self.name

class Client(models.Model):
    domain = models.CharField(max_length = 100, verbose_name = u'Domain name', help_text = u'Domain name of the client')
    ip = models.CharField(max_length = 100, verbose_name = 'IP addresses', help_text = u'IP addresses of the client servers. Example: 10.0.0.1;10.0.0.2')
    node = models.ManyToManyField(Node, verbose_name = u'Nodes')
    is_active = models.BooleanField(default = True, verbose_name = u'Is active')

    def __unicode__(self):
        return self.domain

class Statistic(models.Model):
    node = models.ForeignKey(Node, max_length = 20, verbose_name = u'Node number')
    mem_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Memory load')
    cpu_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'CPU load')
    net_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Network load')
    av_load = models.FloatField(null = 'True', blank = 'True', verbose_name = u'Average load')
    tcp_conn = models.IntegerField(null = 'True', blank = 'True', verbose_name = u'TCP connections number')
    date = models.DateTimeField(auto_now_add = True, verbose_name = u'Statistic time')

class BlackList(models.Model):
    ip = models.IPAddressField(null = 'False', unique = 'True', verbose_name = u'IP address')
    node = models.ManyToManyField(Node, verbose_name = u'Nodes')
    is_active = models.BooleanField(default = True, verbose_name = u'Is active')
    date = models.DateTimeField(auto_now = True, verbose_name = u'Last updated')

    def __unicode__(self):
        return self.ip
