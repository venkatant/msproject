__author__ = 'venkat'


from header import *
from json_http_handler import *


class LinkTables:
    def __init__(self, switch=None, port=None, status=None, bw=None):
        self.check_gmail = IntVar()
        self.check_snmp = IntVar()
        self.var = IntVar()
        self.switchId = switch
        self.portName = port
        self.portStatus = status
        self.bandwidth = bw

    def updatelinkstatus(self, switch, port, status, bw):
        self.switchId = switch
        self.portName = port
        self.portStatus = status
        self.bandwidth = bw


    def printflowenties(self):
        print(self.switchId)
        print(self.portName)
        print(self.portStatus)
        print(self.bandwidth)

    def send_mail(self):
        print("Mail", self.check_gmail.get())
        return


    def send_trap(self):
        print("SNMP", self.check_snmp.get())
        return


    def mradioselect(self):
        print("Value Selected is ", self.var.get())
        return

def linkfaultmenu():

    toplevel = Toplevel()
    toplevel.title("Node Monitoring")

    '''
    Create an object of Http JSON Handler Class to receive
    resp from respective Rest URL's
    '''
    http_obj = HttpJsonHandler()
    json_nodes = http_obj.getnodeinfo()

    position = 0
    flowTableList = []

    print("---------START--------------")
    ''' Outer For Loop is to iterate based on No of Nodes in the Network'''
    for node in json_nodes['nodeProperties']:
        json_link = http_obj.getlinkinfo(node['node']['id'])

        no_of_links_per_node = 0
        for flowCount in json_link['nodeConnectorProperties']:
            print(flowCount['nodeconnector'])
            no_of_links_per_node = no_of_links_per_node + 1

        print('-----------------------LINK INFO--------------------------')

        for pos in range(no_of_links_per_node):

            if int(json_link['nodeConnectorProperties'][pos]['nodeconnector']['id']) > 0:
                # Create an array of Objects using List
                obj = LinkTables()

                # Update the content in the newly created Object
                obj.updatelinkstatus(
                    json_link['nodeConnectorProperties'][pos]['nodeconnector']['node']['id'],
                    json_link['nodeConnectorProperties'][pos]['properties']['name']['value'],
                    json_link['nodeConnectorProperties'][pos]['properties']['state']['value'],
                    json_link['nodeConnectorProperties'][pos]['properties']['bandwidth']['value'])

                print((pos, position, json_link['nodeConnectorProperties'][pos]['nodeconnector']['id']))

                position = position + 1

                # Append the Object to the flow table List
                flowTableList.append(obj)

    rows = []
    for i in range(position):

        print(flowTableList[i].switchId, flowTableList[i].portName, flowTableList[i].portStatus,
              flowTableList[i].bandwidth)

        if (flowTableList[i].switchId != None):
            cols = []
            for j in range(4):
                e = Entry(toplevel, relief=RIDGE)
                e.grid(row=i, column=j, sticky=NSEW)
                # e.insert(END, '%d.%d' % (i, j))
                if (j == 0):
                    e.insert(END, '%s' % flowTableList[i].switchId)
                if (j == 1):
                    e.insert(END, '%s' % flowTableList[i].portName)
                if (j == 2):
                    e.insert(END, '%s' % flowTableList[i].portStatus)
                if (j == 3):
                    e.insert(END, '%s' % flowTableList[i].bandwidth)
                cols.append(e)
    rows.append(cols)

    obj = LinkTables()

    Checkbutton(toplevel, text="Send E-Mail", variable=obj.check_gmail, command=obj.send_mail).grid(row=50, sticky=W)
    Checkbutton(toplevel, text="Send Trap", variable=obj.check_snmp, command=obj.send_trap).grid(row=51, stick=W)

    Radiobutton(toplevel, text="1 Sec ", variable=obj.var, value=1, command=obj.mradioselect).grid(row=52, column=0, stick=W)
    Radiobutton(toplevel, text="5 Sec ", variable=obj.var, value=5, command=obj.mradioselect).grid(row=52, column=1, stick=W)
    Radiobutton(toplevel, text="10 Sec", variable=obj.var, value=10, command=obj.mradioselect).grid(row=52, column=2, stick=W)
    Radiobutton(toplevel, text="30 Sec", variable=obj.var, value=30, command=obj.mradioselect).grid(row=52, column=3, stick=W)
    print()

    return
