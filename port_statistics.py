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
    toplevel.geometry("900x250")
    display(toplevel)

def display(toplevel):
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
            obj.updateportstatistics(portCount['nodeConnector']['node']['id'],
                                     portCount['nodeConnector']['id'],
                                     portCount['receivePackets'],
                                     portCount['receiveBytes'],
                                     portCount['receiveDrops'],
                                     portCount['transmitPackets'],
                                     portCount['transmitBytes'],
                                     portCount['transmitErrors'])

            no_of_ports += 1

            # Append the Object to the port  table List
            portTableList.append(obj)

            obj.displayportstatistics()

    # sort the list with switch_is as Key
    portTableList.sort(key=lambda host: host.switchId)

    for row in range(no_of_ports+1):
        current_row = []
        for column in range(8):

            if row == 0:
                if column == 0:
                    label = Label(toplevel, text="Switch ID", borderwidth=0, width=25, fg="red")
                elif column == 1:
                    label = Label(toplevel, text="Port ID", borderwidth=0, width=10, fg="red")
                elif column == 2:
                    label = Label(toplevel, text="No Of Rx Pkts", borderwidth=0, width=14, fg="red")
                elif column == 3:
                    label = Label(toplevel, text="No Of Rx Bytes", borderwidth=0, width=14, fg="red")
                elif column == 4:
                    label = Label(toplevel, text="No Of Rx Drops", borderwidth=0, width=14, fg="red")
                elif column == 5:
                    label = Label(toplevel, text="No Of Tx Pkts", borderwidth=0, width=14, fg="red")
                elif column == 6:
                    label = Label(toplevel, text="No Of Tx Bytes", borderwidth=0, width=14, fg="red")
                elif column == 7:
                    label = Label(toplevel, text="No Of Tx Drops", borderwidth=0, width=14, fg="red")
                label.configure(bg="white")
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)

            else:
                if column == 0:
                    label = Label(toplevel, text="%s" % portTableList[row-1].switchId, borderwidth=0, width=25)
                elif column == 1:
                    label = Label(toplevel, text="%s" % portTableList[row-1].portId, borderwidth=0, width=10)
                elif column == 2:
                    label = Label(toplevel, text="%s" % portTableList[row-1].NoOfRxPackets, borderwidth=0, width=14)
                elif column == 3:
                    label = Label(toplevel, text="%s" % portTableList[row-1].NoOfRxBytes, borderwidth=0, width=14)
                elif column == 4:
                    label = Label(toplevel, text="%s" % portTableList[row-1].NoOfRxPacketsDropped, borderwidth=0, width=14)
                elif column == 5:
                    label = Label(toplevel, text="%s" % portTableList[row-1].NoOfTxPackets, borderwidth=0, width=14)
                elif column == 6:
                    label = Label(toplevel, text="%s" % portTableList[row-1].NoOfTxBytes, borderwidth=0, width=14)
                elif column == 7:
                    label = Label(toplevel, text="%s" % portTableList[row-1].NoOfTxPacketsDropped, borderwidth=0, width=14)

                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.configure(bg="white")
                current_row.append(label)

        for column in range(8):
            toplevel.grid_columnconfigure(column, weight=1)

    toplevel.after(5000, display, toplevel)
    return
