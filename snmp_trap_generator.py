__author__ = 'venkat'

from pysnmp.entity.rfc3413.oneliner import ntforg
from pysnmp.proto import rfc1902

class SnmpTrapGenerator(object):

    def __init__(self):
        self.community = 'public'
        self.snmpServerIP = '127.0.0.1'
        self.snmpPort = 162
        self.snmpTrapVariable = 'LinkMonitoring'
        self.snmpTrapOID = '1.3.6.1.2.1.1.1.0'
        self.snmpVarBind = ''

    def send_snmp_trap(self,param):

        if(param != None):
            self.snmpVarBind = param

        ntfOrg = ntforg.NotificationOriginator()

        ntfOrg.sendNotification(ntforg.CommunityData(self.community, mpModel=0),
                                ntforg.UdpTransportTarget((self.snmpServerIP, self.snmpPort)),
                                'trap',
                                '1.3.6.1.4.1.20408.4.1.1.2.0.432',
                                (self.snmpTrapOID, rfc1902.OctetString(self.snmpVarBind)))

        print("Sending SNMP Trap")
