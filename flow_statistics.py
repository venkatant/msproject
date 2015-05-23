__author__ = 'venkat'


from header import *
from json_http_handler import *


class FlowTable:

    flow_list = []

    def __init__(self):

        self.dest_ip   = None
        self.dest_mask = None
        self.dest_Mac  = None
        self.dest_port = None
        self.dest_node = None
        return

    def updateflowtable(self, destIp, destMask, destMac, destPort, destNode):
        self.dest_ip   = destIp
        self.dest_mask = destMask
        self.dest_Mac  = destMac
        self.dest_port = destPort
        self.dest_node = destNode
        return

    def displayflowtable(self):
        print(self.dest_ip,
              self.dest_mask,
              self.dest_Mac,
              self.dest_port,
              self.dest_node)
        return


class FlowStatistics:
    def __init__(self):
        self.mylistbox = None
        self.toplevel = None

    def CurListSelet(self, evt):
        mylistbox = evt.widget
        switch=str((mylistbox.get(mylistbox.curselection())))
        print(switch)

    def CurSelet(self):
        switch = str((self.mylistbox.get(self.mylistbox.curselection())))
        print(switch)

        http_obj = HttpJsonHandler()
        json_flows = http_obj.getflowinfo(switch)

        flow_list = []
        no_of_flows = 0

        for flowCount in json_flows['flowStatistic']:
            destIp = json_flows['flowStatistic'][no_of_flows]['flow']['match']['matchField'][0]['value']
            destMask = json_flows['flowStatistic'][no_of_flows]['flow']['match']['matchField'][0]['mask']

            destPort = 0
            destnode = '00:00:00:00:00:00:00:00'

            try:
                destMac = json_flows['flowStatistic'][no_of_flows]['flow']['actions'][0]['address']
                try:
                    destPort = json_flows['flowStatistic'][no_of_flows]['flow']['actions'][1]['port']['id']
                    destnode = json_flows['flowStatistic'][no_of_flows]['flow']['actions'][1]['port']['node']['id']
                except:
                    print('')
            except KeyError:
                destPort = json_flows['flowStatistic'][no_of_flows]['flow']['actions'][0]['port']['id']
                destnode = json_flows['flowStatistic'][no_of_flows]['flow']['actions'][0]['port']['node']['id']
                destMac = '000000000000'

            # destIp, destMask, destMac, destPort, destNode
            # Create an instance of FlowTable class
            flow_table_entry = FlowTable()

            flow_table_entry.updateflowtable(destIp,destMask, destMac, destPort,destnode)

            flow_table_entry.flow_list.append(flow_table_entry)

            no_of_flows = no_of_flows + 1

            flow_table_entry.displayflowtable()

def flowstatistics():

    # Create an instance of FlowTable class
    #flow_table_entry = FlowTable()

    # Create an instance of FlowStatistics class
    obj = FlowStatistics()

    obj.toplevel = Toplevel()
    obj.toplevel.title("Flow Statistics Per Switch")
    obj.toplevel.geometry("750x500")

    '''
    Create an object of Http JSON Handler Class to receive
    resp from respective Rest URL's
    '''
    http_obj = HttpJsonHandler()
    json_nodes = http_obj.getnodeinfo()

    scrollbar = Scrollbar(obj.toplevel)
    obj.mylistbox = Listbox(obj.toplevel, yscrollcommand=scrollbar.set)

    for node in json_nodes['nodeProperties']:
        obj.mylistbox.insert(END, node['node']['id'])

    obj.mylistbox.pack(side=LEFT, fill=BOTH,)
    scrollbar.pack(side=LEFT, fill=Y)

    scrollbar.config(command=obj.mylistbox.yview)
    submit = Button(obj.toplevel, text="Submit", command=obj.CurSelet)
    submit.pack()

    # Below code to activate on selection of items in List Box
    #obj.mylistbox.bind('<<ListboxSelect>>',obj.CurListSelet)

    return