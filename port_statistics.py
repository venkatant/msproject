__author__ = 'venkat'


from header import *
from json_http_handler import *

class PortTableStatistics:
    def __init__(self,
                 switchId = None,
                 portId = None,
                 NoOfRxPackets=None,
                 NoOfRxBytes=None,
                 NoOfRxPacketsDropped=None,
                 NoOfTxPackets=None,
                 NoOfTxBytes=None,
                 NoOfTxPacketsDropped=None
                 ):
        self.switchId = switchId
        self.portId =  portId
        self.NoOfRxPackets = NoOfRxPackets
        self.NoOfRxBytes = NoOfRxBytes
        self.NoOfRxPacketsDropped = NoOfRxPacketsDropped
        self.NoOfTxPackets = NoOfTxPackets
        self.NoOfTxBytes = NoOfTxBytes
        self.NoOfTxPacketsDropped = NoOfTxPacketsDropped

    def updateportstatistics(self,
                             switchId,
                             portId,
                             NoOfRxPackets,
                             NoOfRxBytes,
                             NoOfRxPacketsDropped,
                             NoOfTxPackets,
                             NoOfTxBytes,
                             NoOfTxPacketsDropped
                             ):
        self.switchId = switchId
        self.portId =  portId
        self.NoOfRxPackets = NoOfRxPackets
        self.NoOfRxBytes = NoOfRxBytes
        self.NoOfRxPacketsDropped = NoOfRxPacketsDropped
        self.NoOfTxPackets = NoOfTxPackets
        self.NoOfTxBytes = NoOfTxBytes
        self.NoOfTxPacketsDropped = NoOfTxPacketsDropped

    def displayportstatistics(self):
        print(
              self.switchId,
              self.portId,
              self.NoOfRxPackets,
              self.NoOfRxBytes,
              self.NoOfRxPacketsDropped,
              self.NoOfTxPackets,
              self.NoOfTxBytes,
              self.NoOfTxPacketsDropped)

def portstatistics():
    toplevel = Toplevel()
    toplevel.title("Port Statistics")
    toplevel.geometry("750x500")

    '''
    Create an object of Http JSON Handler Class to receive
    resp from respective Rest URL's
    '''
    http_obj = HttpJsonHandler()
    json_nodes = http_obj.getnodeinfo()

    # Create a list to hold the object of the portstatistics Class
    portTableList = []
    no_of_ports = 0

    print("---------START--------------")

    '''
    Outer For Loop is to iterate based on No of Nodes in the Network
    Extract the Node ID from JSON Response and append it to port_link
    '''

    for node in json_nodes['nodeProperties']:
        json_ports = http_obj.getportinfo(node['node']['id'])

        print(json.dumps(json_ports))
        print(json_ports['node']) # This will print Info belongs to each port of the Node

        for portCount in json_ports['portStatistic']:
            print(portCount['nodeConnector']['node']['id'], portCount['nodeConnector']['id'])

            # Create an instance of PortTableStatistics class
            obj = PortTableStatistics()

            # Update the content in the newly created Object
            obj.updateportstatistics(
                                     portCount['nodeConnector']['node']['id'],
                                     portCount['nodeConnector']['id'],
                                     portCount['receivePackets'],
                                     portCount['receiveBytes'],
                                     portCount['receiveDrops'],
                                     portCount['transmitPackets'],
                                     portCount['transmitBytes'],
                                     portCount['transmitErrors']
                                     )

            no_of_ports = no_of_ports + 1

            # Append the Object to the port  table List
            portTableList.append(obj)

            obj.displayportstatistics()

            e = Entry(toplevel, relief=RIDGE)
            e.grid(row=0, column=0, sticky=NSEW)

            switchId = portCount['nodeConnector']['node']['id']
            portId = portCount['nodeConnector']['id']

            rows = []
            for i in range(no_of_ports+1):
                cols = []
                for j in range(8):

                    if i == 0:
                        e = Entry(toplevel, relief=RIDGE, width=15, fg="red")
                        e.grid(row=i, column=j, sticky=NSEW)

                        if j == 0:
                            e.insert(END, "  Switch ID")
                        elif j == 1:
                            e.insert(END, "  Port Number")
                        elif j == 2:
                            e.insert(END, "  No Of Rx Pkts ")
                        elif j == 3:
                            e.insert(END, "  No Of Rx Bytes")
                        elif j == 4:
                            e.insert(END, "  No Of Rx Drops")
                        elif j == 5:
                            e.insert(END, "  No Of Tx Pkts")
                        elif j == 6:
                            e.insert(END, "  No Of Tx Bytes")
                        elif j == 7:
                            e.insert(END, "  No Of Tx Drops")
                    else:
                        e = Entry(toplevel, relief=RIDGE, width=15)
                        e.grid(row=i, column=j, sticky=NSEW)

                        #e.insert(END, '%d.%d' % (i, j))
                        if (j == 0):
                            e.insert(END, '%s' % portTableList[i-1].switchId)
                        if (j == 1):
                            e.insert(END, '%s' % portTableList[i-1].portId)
                        if (j == 2):
                            e.insert(END, '%s' % portTableList[i-1].NoOfRxPackets)
                        if (j == 3):
                            e.insert(END, '%s' % portTableList[i-1].NoOfRxBytes)
                        if (j == 4):
                            e.insert(END, '%s' % portTableList[i-1].NoOfRxPacketsDropped)
                        if (j == 5):
                            e.insert(END, '%s' % portTableList[i-1].NoOfTxPackets)
                        if (j == 6):
                            e.insert(END, '%s' % portTableList[i-1].NoOfTxBytes)
                        if (j == 7):
                            e.insert(END, '%s' % portTableList[i-1].NoOfTxPacketsDropped)
                    cols.append(e)
                rows.append(cols)

    return
