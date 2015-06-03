__author__ = 'venkat'


from header import *
from json_http_handler import *


class FlowWindow:
    bottom_frame = 0
    bottom_row = 0


class FlowTable:

    def __init__(self):

        self.dest_ip   = None
        self.dest_mask = None
        self.dest_mac  = None
        self.dest_port = None
        self.dest_node = None
        return

    def updateflowtable(self, destIp, destMask, destMac, destPort, destNode):
        self.dest_ip   = destIp
        self.dest_mask = destMask
        self.dest_mac  = destMac
        self.dest_port = destPort
        self.dest_node = destNode
        return

    def displayflowtable(self):
        print(self.dest_ip,
              self.dest_mask,
              self.dest_mac,
              self.dest_port,
              self.dest_node)
        return


class FlowStatistics:
    def __init__(self):
        self.listbox = None
        self.toplevel = None
        self.no_of_flows = 0

    def CurSelet(self):
        print("Hello")
        switch = str((self.mylistbox.get(self.mylistbox.curselection())))
        print(switch)

    def fillListWithNodesInfo(self):
        '''
        Create an object of Http JSON Handler Class to receive
        resp from respective Rest URL's
        '''
        http_obj = HttpJsonHandler()
        json_nodes = http_obj.getnodeinfo()

        for node in json_nodes['nodeProperties']:
            self.listbox.insert(END, node['node']['id'])

    def displayFlowTableTitle(self, bottom_frame, bottom_row):

        for column in range(5):
            if column == 0:
                label = Label(bottom_frame, text="Destination IP", borderwidth=0, width=15, fg="red")
            elif column == 1:
                label = Label(bottom_frame, text="Destination Mask", borderwidth=0, width=15, fg="red")
            elif column == 2:
                label = Label(bottom_frame, text="Output Mac", borderwidth=0, width=15, fg="red")
            elif column == 3:
                label = Label(bottom_frame, text="Output Port", borderwidth=0, width=15, fg="red")
            elif column == 4:
                label = Label(bottom_frame, text="Output Node", borderwidth=0, width=25, fg="red")

            label.configure(bg="white")
            label.grid(row=bottom_row, column=column, sticky="nsew", padx=1, pady=1)

        return

    def displayFlowTableContent(self, flow_list, flow_window_obj):

        bottom_frame = flow_window_obj.bottom_frame
        bottom_row = flow_window_obj.bottom_row

        #for row in range(4):
        for row in flow_list:
            current_row = []

            for column in range(5):
                if column == 0:
                    label = Label(bottom_frame, text="%s" % row.dest_ip, borderwidth=0, width=15)
                elif column == 1:
                    label = Label(bottom_frame, text="%s" % row.dest_mask, borderwidth=0, width=15)
                elif column == 2:
                    label = Label(bottom_frame, text="%s" % row.dest_mac, borderwidth=0, width=15)
                elif column == 3:
                    label = Label(bottom_frame, text="%s" % row.dest_port, borderwidth=0, width=15)
                elif column == 4:
                    label = Label(bottom_frame, text="%s" % row.dest_node, borderwidth=0, width=25)

                label.configure(bg="white")
                label.grid(row=bottom_row, column=column, sticky="nsew", padx=1, pady=1)

                current_row.append(label)

            bottom_row += 1

            for column in range(5):
                bottom_frame.grid_columnconfigure(column, weight=1)

        return

    def CurListSelet(self, evt, flow_window_obj):
        #mylistbox = evt.widget
        switch=str((self.listbox.get(self.listbox.curselection())))
        print(switch)

        '''
        Create an object of Http JSON Handler Class to receive
        resp from respective Rest URL's
        '''
        http_obj = HttpJsonHandler()
        json_flows = http_obj.getflowinfo(switch)

        no_of_flows = 0
        flow_list = []

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

            flow_table_entry.updateflowtable(destIp, destMask, destMac, destPort, destnode)

            flow_list.append(flow_table_entry)
            no_of_flows += 1

            flow_table_entry.displayflowtable()

        # sort the list with switch_is as Key
        flow_list.sort(key=lambda host:host.dest_ip)

        self.displayFlowTableContent(flow_list, flow_window_obj)

def flowstatistics():

    # Create an instance of FlowTable class
    #flow_table_entry = FlowTable()

    # Create an instance of FlowStatistics class
    obj = FlowStatistics()

    '''
    scrollbar.config(command=obj.mylistbox.yview)
    submit = Button(obj.toplevel, text="Submit", command=obj.CurSelet)
    submit.pack()
    '''
    toplevel = Toplevel()
    toplevel.title("Flow Monitoring")
    toplevel.geometry("750x250")

    top_row = 0
    bottom_row = 0

    top_frame = Frame(toplevel)
    top_frame.pack(side=TOP)

    top_label = Label(top_frame, text=" SELECT SWITCH TO GET FLOW ENTRIES", fg="red", borderwidth=0, width=40)
    top_label.grid(row=top_row, rowspan=1)
    top_row += 1

    bottom_frame = Frame(toplevel)
    bottom_frame.pack(side=TOP)

    bottom_label = Label(bottom_frame, fg="green")
    bottom_label.grid(row=bottom_row)
    bottom_row += 1

    scrollbar = Scrollbar(top_frame)
    obj.listbox = Listbox(top_frame, yscrollcommand=scrollbar.set)
    obj.listbox.config(height=4)

    # Fills the list of nodes in the List Box
    obj.fillListWithNodesInfo()

    obj.listbox.grid(row=top_row, column=0, sticky="nsew", padx=1, pady=1)
    scrollbar.grid(row=top_row, column=1, sticky="nsew", padx=1, pady=1)

    scrollbar.config(command=obj.listbox.yview)

    obj.displayFlowTableTitle(bottom_frame, bottom_row)
    bottom_row += 1

    flow_window_obj = FlowWindow()
    flow_window_obj.bottom_row = bottom_row
    flow_window_obj.bottom_frame = bottom_frame

    # Below code to activate on selection of items in List Box
    obj.listbox.bind('<<ListboxSelect>>', lambda event, arg=flow_window_obj: obj.CurListSelet(event, flow_window_obj))

    return