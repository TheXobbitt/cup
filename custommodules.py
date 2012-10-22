from admin_tools.dashboard import modules
from datetime import *
from cc.models import Node

class NodeSelect(modules.DashboardModule):
    def is_empty(self):
        return False

    def __init__(self, **kwargs):
        super(NodeSelect, self).__init__(**kwargs)
        self.template = 'statistic/node_select.html'
        active_nodes = Node.objects.filter(is_active=1)
        nodes = [{'id': node.id, 'name': node.name} for node in active_nodes]
        self.nodes = nodes