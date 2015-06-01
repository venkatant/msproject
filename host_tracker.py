__author__ = 'venkat'


from tkinter import *
from json_http_handler import *


class HostTracker:
    def __init__(self):
        self.switch_id = 0
        self.port_id = 0
        self.port_mac = '00:00:00:00:00:00'
        self.port_ip = '0.0.0.0'
        self.port_vlan = 0
        self.static_host = FALSE

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
    toplevel.geometry("800x200")

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

        no_of_hosts += 1

        host_tracker_obj.displayhostinfo()
    for host1 in host_list:
        print(host1)

    # sort the list with switch_is as Key
    host_list.sort(key=lambda host:host.switch_id)

    for row in range(no_of_hosts+1):

        current_row = []

        for column in range(6):

            if row == 0:
                if column == 0:
                    label = Label(toplevel, text="Switch ID", borderwidth=0, width=15, fg="red")
                elif column == 1:
                    label = Label(toplevel, text="Port ID", borderwidth=0, width=10, fg="red")
                elif column == 2:
                    label = Label(toplevel, text="Port MAC", borderwidth=0, width=10, fg="red")
                elif column == 3:
                    label = Label(toplevel, text="Port IP", borderwidth=0, width=10, fg="red")
                elif column == 4:
                    label = Label(toplevel, text="Port VLAN", borderwidth=0, width=10, fg="red")
                elif column == 5:
                    label = Label(toplevel, text="Static Host", borderwidth=0, width=10, fg="red")

                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.configure(bg="white")

            else:
                if column == 0:
                    label = Label(toplevel, text="%s" % host_list[row-1].switch_id, borderwidth=0, width=15)
                elif column == 1:
                    label = Label(toplevel, text="%s" % host_list[row-1].port_id, borderwidth=0, width=10)
                elif column == 2:
                    label = Label(toplevel, text="%s" % host_list[row-1].port_mac, borderwidth=0, width=10)
                elif column == 3:
                    label = Label(toplevel, text="%s" % host_list[row-1].port_ip, borderwidth=0, width=10)
                elif column == 4:
                    label = Label(toplevel, text="%s" % host_list[row-1].port_vlan, borderwidth=0, width=10)
                elif column == 5:
                    label = Label(toplevel, text="%s" % host_list[row-1].static_host, borderwidth=0, width=10)

                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.configure(bg="white")
                current_row.append(label)

        for column in range(6):
            toplevel.grid_columnconfigure(column, weight=1)

    return
