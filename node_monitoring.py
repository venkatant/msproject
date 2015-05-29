__author__ = 'venkat'


from header import *
from json_http_handler import *
from snmp_trap_generator import *
from gmail import  *


class RadioButton:
    def __init__(self):
        self.check_gmail = IntVar()
        self.check_snmp = IntVar()
        self.refresh_interval = IntVar()
        return

    def m_radioselect(self):
        print("Refresh Interval Selected is ", self.refresh_interval.get())
        return

    def m_getrefreshinterval(self):
        return self.refresh_interval.get()

    def send_mail(self):
        print("Mail", self.check_gmail.get())
        return self.check_gmail.get()

    def send_trap(self):
        print("SNMP", self.check_snmp.get())
        return self.check_snmp.get()

class LinkTables:
    def __init__(self, switch=None, port=None, status=None, bw=None):

        self.switchId = switch
        self.portName = port
        self.portStatus = status
        self.bandwidth = bw
        self.email_notify=0

    def updatelinkstatus(self, switch, port, status, bw):
        self.switchId = switch
        self.portName = port
        self.portStatus = status
        self.bandwidth = bw

        # Reset E-Mail Notify When the Link status is UP
        if self.portStatus == 1:
            self.email_notify = 0

    def printflowenties(self):
        print(self.switchId)
        print(self.portName)
        print(self.portStatus)
        print(self.bandwidth)


def linkfaultmenu():

    toplevel = Toplevel()
    toplevel.title("Link Monitoring")
    toplevel.geometry("750x300")

    rb_obj = RadioButton()

    Checkbutton(toplevel, text="Send E-Mail", variable=rb_obj.check_gmail, command=rb_obj.send_mail).grid(row=50, sticky=W)
    Checkbutton(toplevel, text="Send Trap", variable=rb_obj.check_snmp, command=rb_obj.send_trap).grid(row=51, stick=W)

    Radiobutton(toplevel, text="1 Sec ", variable=rb_obj.refresh_interval, value=1, command=rb_obj.m_radioselect).grid(row=52, column=0, sticky=W)
    Radiobutton(toplevel, text="5 Sec ", variable=rb_obj.refresh_interval, indicatoron = 1, value=5, command=rb_obj.m_radioselect).grid(row=52, column=1, sticky=W)
    Radiobutton(toplevel, text="10 Sec", variable=rb_obj.refresh_interval, value=10, command=rb_obj.m_radioselect).grid(row=52, column=2, sticky=W)
    Radiobutton(toplevel, text="30 Sec", variable=rb_obj.refresh_interval, value=30, command=rb_obj.m_radioselect).grid(row=52, column=3, sticky=W)

    rb_obj.refresh_interval.set(5)

    display(toplevel, rb_obj)

    return


def display(toplevel, rb_obj):

    '''
    Create an object of Http JSON Handler Class to receive resp from respective Rest URL's
    '''
    http_obj = HttpJsonHandler()
    json_nodes = http_obj.getnodeinfo()

    position = 0
    flowTableList = []

    # print("---------START--------------")
    ''' Outer For Loop is to iterate based on No of Nodes in the Network'''

    for node in json_nodes['nodeProperties']:
        json_link = http_obj.getlinkinfo(node['node']['id'])

        no_of_links_per_node = 0
        for flowCount in json_link['nodeConnectorProperties']:
            #print(flowCount['nodeconnector'])
            no_of_links_per_node = no_of_links_per_node + 1

        # print('-----------------------LINK INFO--------------------------')

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

                # print((pos, position, json_link['nodeConnectorProperties'][pos]['nodeconnector']['id']))

                position = position + 1

                # Append the Object to the flow table List
                flowTableList.append(obj)

    '''
    for i in range(position):
        print(flowTableList[i].switchId, flowTableList[i].portName, flowTableList[i].portStatus,
              flowTableList[i].bandwidth)
    '''
    # sort the list with switch_is as Key
    flowTableList.sort(key=lambda host:host.switchId)

    for row in range(position+1):
        current_row = []
        for column in range(4):

            if row==0:
                if column == 0:
                    label = Label(toplevel, text="Switch ID", borderwidth=0, width=10, fg="red").grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                elif column == 1:
                    label = Label(toplevel, text="Port ID", borderwidth=0, width=10, fg="red").grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                elif column == 2:
                    label = Label(toplevel, text="Link Status", borderwidth=0, width=10, fg="red").grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                elif column == 3:
                    label = Label(toplevel, text="Bandwidth", borderwidth=0, width=10, fg="red").grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            else:
                if column == 0:
                    label = Label(toplevel, text="%s" % flowTableList[row-1].switchId, borderwidth=0, width=10)
                elif column == 1:
                    label = Label(toplevel, text="%s" % flowTableList[row-1].portName, borderwidth=0, width=10)
                elif column == 2:
                    if 1 == flowTableList[row-1].portStatus:
                        status = "UP"
                    else:
                        status = "DOWN"

                    label = Label(toplevel, text="%s" % status, borderwidth=0, width=10)
                    if status == "DOWN":
                        label.configure(fg="red")

                    # Send E-Mail once per failure
                    if flowTableList[row-1].email_notify == 0 and rb_obj.check_snmp.get() == 1 and 0 == flowTableList[row-1].portStatus:
                        print("Sending Failure Notification")
                        snmpTrapGenerator().fireTrap('Hello')
                        #send_email("PORT LINK STATUS DOWN")
                        flowTableList[row-1].email_notify = 1

                elif column == 3:
                    label = Label(toplevel, text="%s" % flowTableList[row-1].bandwidth, borderwidth=0, width=10)

                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.configure(bg="white")
                current_row.append(label)

        for column in range(4):
            toplevel.grid_columnconfigure(column, weight=1)

    toplevel.after(rb_obj.m_getrefreshinterval() * 1000, display, toplevel, rb_obj)
    return
