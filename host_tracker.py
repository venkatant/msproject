__author__ = 'venkat'


from tkinter import *
from json_http_handler import *


class HostTracker:
    def __init__(self):
        switch_id   = 0
        port_id     = 0
        port_mac    = '00:00:00:00:00:00'
        port_ip     = '0.0.0.0'
        port_vlan   = 0
        static_host = FALSE

    def updatehost(self, switchId, portNo, portMac, portIp, portVlan, statisHost):
        self.switch_id   = switchId
        self.port_id     = portNo
        self.port_mac    = portMac
        self.port_ip     = portIp
        self.port_vlan   = portVlan
        self.static_host = statisHost
        return

    def displayhostinfo(self):
        print(self.switch_id,
              self.port_id,
              self.port_ip,
              self.port_mac,
              self.port_vlan,
              self.static_host)
        return

    def curselect(self):
        return


def hosttracker():
    toplevel = Toplevel()
    toplevel.title("Host Tracker")

    '''
    scrollbar = Scrollbar(toplevel)
    nodelistbox = Listbox(toplevel, yscrollcommand=scrollbar.set)

    Create an object of Http JSON Handler Class to receive resp from
    respective Rest URL's


    http_obj = HttpJsonHandler()
    json_node = http_obj.getnodeinfo()

    for node in json_node['nodeProperties']:
        nodelistbox.insert(END,  node['node']['id'])

    nodelistbox.pack(side=LEFT, fill=BOTH)
    scrollbar.pack(side=LEFT, fill=Y)
    scrollbar.config(command=nodelistbox.yview)

    host_tracker_obj = HostTracker()

    submit = Button(toplevel, text="Submit", command=host_tracker_obj.curselect())
    #submit.pack()
    '''

    print("---------START--------------")
    '''
    Create an object of Http JSON Handler Class to receive resp from
    respective Rest URL's
    '''
    http_obj = HttpJsonHandler()
    json_host = http_obj.gethostinfo()

    host_list = []
    no_of_hosts = 0

    for host in json_host['hostConfig']:

        host_tracker_obj = HostTracker()

        host_tracker_obj.updatehost(host['nodeId'],
                                    host['nodeConnectorId'],
                                    host['dataLayerAddress'],
                                    host['networkAddress'],
                                    host['vlan'],
                                    host['staticHost'])

        host_list.append(host_tracker_obj)

        no_of_hosts = no_of_hosts + 1

        #host_tracker_obj.displayhostinfo()
    for host1 in host_list:
        print(host1)

    e = Entry(toplevel, relief=RIDGE)
    e.grid(row=0, column=0, sticky=NSEW)

    rows = []
    for i in range(no_of_hosts+1):
        cols = []
        for j in range(6):

            e = Entry(toplevel, relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)

            if i == 0:
                if j == 0:
                    e.insert(END, "  Switch ID")
                elif j == 1:
                    e.insert(END, "  Port ID")
                elif j == 2:
                    e.insert(END, "  Port MAC")
                elif j == 3:
                    e.insert(END, "  Port TP")
                elif j == 4:
                    e.insert(END, "  Port Vlan")
                elif j == 5:
                    e.insert(END, "  Static Host")
            else:
                #e.insert(END, '%d.%d' % (i, j))
                if (j == 0):
                    e.insert(END, '%s' % host_list[i-1].switch_id)
                if (j == 1):
                    e.insert(END, '%s' % host_list[i-1].port_id)
                if (j == 2):
                    e.insert(END, '%s' % host_list[i-1].port_mac)
                if (j == 3):
                    e.insert(END, '%s' % host_list[i-1].port_ip)
                if (j == 4):
                    e.insert(END, '%s' % host_list[i-1].port_vlan)
                if (j == 5):
                    e.insert(END, '%s' % host_list[i-1].static_host)
            cols.append(e)
        rows.append(cols)

    return
