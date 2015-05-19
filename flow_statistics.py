__author__ = 'venkat'


from header import *
from json_http_handler import *


class FlowStatistics:
    def __init__(self):
        mylistbox = None

    def mdumpfunction(self):
        return
    '''
    def CurSelet(self, evt):
        mylistbox = evt.widget
        value=str((mylistbox.get(mylistbox.curselection())))
        print(value)
    '''

    def CurSelet(self):
        value=str((self.mylistbox.get(self.mylistbox.curselection())))
        print(value)

def flowstatistics():

    toplevel = Toplevel()
    toplevel.title("Flow Statistics Per Switch")
    toplevel.geometry("500x200")

    # Create an instance of FlowStatistics class
    obj = FlowStatistics()

    '''
    Create an object of Http JSON Handler Class to receive
    resp from respective Rest URL's
    '''
    http_obj = HttpJsonHandler()
    json_nodes = http_obj.getnodeinfo()

    scrollbar = Scrollbar(toplevel)
    obj.mylistbox = Listbox(toplevel, yscrollcommand=scrollbar.set)

    for node in json_nodes['nodeProperties']:
        obj.mylistbox.insert(END, node['node']['id'])

    obj.mylistbox.pack(side=LEFT, fill=BOTH,)
    scrollbar.pack(side=LEFT, fill=Y)

    scrollbar.config(command=obj.mylistbox.yview)
    submit = Button(toplevel, text="Submit", command=obj.CurSelet)

    # Below code to activate on selection of items in List Box
    #obj.mylistbox.bind('<<ListboxSelect>>',obj.CurSelet)

    submit.pack()

    return