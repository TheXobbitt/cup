from django.core.management.base import BaseCommand, CommandError
from cc.models import Node, Client

class Command(BaseCommand):
    def handle(self, *args, **options):
        for node_id in args:
            if node_id == 'NS':
                for client in Client.objects.all():
                    ip = ''
                    for node in client.node.filter(is_active=True):
                        ip += ';%s' % node.ip
                    print '%s%s' % (client.domain, ip)
            else:
                if Node.objects.get(name=node_id).is_active == True:
                    for client in Client.objects.filter(node__name=node_id):
                        print client
                else:
                    print 'Disable'