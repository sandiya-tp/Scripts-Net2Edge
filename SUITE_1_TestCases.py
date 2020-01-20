import sys
import pdb
sys.path.append("C:\Python27\Scripts")
#from StcPython import StcPython
import connection
import DebugLogger
import logging
import feature
import re
import time
import Config
sys.path.append("C:\Program Files\Spirent Communications\Spirent TestCenter 4.94\Spirent TestCenter Application\HltAPI\SourceCode")
command =''
logger_obj = DebugLogger.DebugLogger("Python.log")

global result
global connection_obj
def Req_1():
	SUITE_1_TC_21()
	SUITE_1_TC_22()
	SUITE_1_TC_23()
	SUITE_1_TC_24()
	SUITE_1_TC_25()
	SUITE_1_TC_26()
	SUITE_1_TC_27()
	SUITE_1_TC_28()

def SUITE_1_TC_21():
	
	# Variable declarations
	global result
	global connection_obj
	DebugLogger.test_result_flag = 0
	
	# Establishing SSH connection
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 1 : VERIFY SSH CONNECTION ESTABLISHMENT")
	
	result = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	print(result.recv(100000000000000000))
	
	# Closing SSH connection
	result.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')

def SUITE_1_TC_22():
	
	# Variable declarations
	global result
	global connection_obj
	DebugLogger.test_result_flag = 0
		
	# Establishing SSH connection
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 2 : DISPLAY DEVICE SW VERSION")
	
	result = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	print(result.recv(100000000000000000))
	
	# Displays output of the command : "show version"
	print (connection_obj.ssh_show_cmds(result, "show version"))
	
	# Closing SSH connection
	result.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
		
def SUITE_1_TC_23():
	
	# Variable declarations
	DebugLogger.test_result_flag = 0

	# Establishing SSH connection
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 3 : STP CONFIGURATION AND VERIFICATION")
	
	result = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	print(result.recv(100000000000000000))
	
	# Banner log output
	connection_obj.banner ("STP CONFIGURATION PART")
	
	# STP configurations
	cmd ='''configure interface lan bridge stp enable
			configure stp lan forward-delay 10
			configure stp lan hello-time 5
			configure stp lan maximum-age 15'''
	
	connection_obj.config(result,cmd)
	
	# Displays output of the command : "show stp status lan"
	print (connection_obj.ssh_show_cmds(result, "\nshow stp status lan"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show stp status lan"
	out = connection_obj.show_cmds_stp_status(result, "show stp status lan")
	
	# Verification of configured STP status : yes
	if (out['STP_Enabled'] != "yes"):
		DebugLogger.test_result_flag += 1
	
	# Displays output of the command : "show stp config"
	print (connection_obj.ssh_show_cmds(result, "\nshow stp config"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show stp config"
	out = connection_obj.show_cmds_stp_config(result, "show stp config")
	
	# Verification of configured STP Forward delay : 10 
	if (out['Forward_delay'] != "10"):
		DebugLogger.test_result_flag += 1
		
	# Verification of configured STP Hello time : 5
	if (out['Hello_time'] != "5"):
		DebugLogger.test_result_flag += 1
		
	# Verification of configured STP Max age : 15
	if (out['Max_age'] != "15"):
		DebugLogger.test_result_flag += 1
	
	# Banner log output
	connection_obj.banner ("STP DELETION PART")
	
	# STP configurations
	cmd ='''configure interface lan bridge stp disable'''
	
	connection_obj.config(result,cmd)
	
	# Closing SSH connection
	result.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
		

def SUITE_1_TC_24():

	# Establishing SSH connection
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 4 : VLAN CONFIGURATION AND TRAFFIC VERIFICATION")
	
	result = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	print(result.recv(100000000000000000))
	
	# Variable declarations
	DebugLogger.test_result_flag = 0
	stc = StcPython()
	szChassisIp = "192.168.0.15"
	port1 = "2/4"
	port2 = "2/7"
	port_list = ['$port1',' $port2']
		
	# Banner log output
	connection_obj.banner ("VLAN CONFIGURATION PART")
	
	# VLAN configurations
	cmd ='''configure vlan add 100
			configure vlan port 100 LAN2 tagged
			configure vlan port 100 LAN3 tagged
			configure vlan port 100 CPU tagged
			configure interface vlan100 add
			configure interface vlan100 ifname add eth0.100'''
	
	connection_obj.config(result,cmd)

	# Displays output of the command : "show vlan config"
	print (connection_obj.ssh_show_cmds(result, "\nshow vlan config"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show vlan config"
	out = connection_obj.show_cmds_vlan_config(result, "show vlan config")
	
	# Verification of configured VLAN ID : 100
	if (out['VLAN_ID'] != "100"):
		DebugLogger.test_result_flag += 1
	
	# Verification of VLAN 100 tagging : LAN2
	if (out['LAN2'] != "tagged"):
		DebugLogger.test_result_flag += 1
	
	# Verification of VLAN 100 tagging : LAN3
	if (out['LAN3'] != "tagged"):
		DebugLogger.test_result_flag += 1
		
	# Verification of VLAN 100 tagging : CPU
	if (out['CPU'] != "tagged"):
		DebugLogger.test_result_flag += 1
	
	# Logging
	stc.config("automationoptions", logto="stdout", loglevel="INFO")

	# Banner log output - Loading saved traffic file
	connection_obj.banner ("LOADING SAVED TRAFFIC FILE")
	
	stc.perform("LoadFromDatabase", DatabaseConnectionString = "STC_file.tcc")
	stc.apply()
	
	# Banner log output - Connecting to STC Chassis : 192.168.0.15
	connection_obj.banner ("CONNECTING TO STC CHASSIS : 192.168.0.15")
	
	stc.connect(szChassisIp)
	
	# Banner log output - Reserving ports : 2/4 and 2/7
	connection_obj.banner ("RESERVING PORTS : 2/4 AND 2/7")
	
	stc.reserve("{0}/{1}/{2} {3}/{4}/{5}".format(szChassisIp, port1.split("/")[0], port1.split("/")[1], szChassisIp, port2.split("/")[0], port2.split("/")[1]))
	
	# Banner log output - Set port Mappings
	connection_obj.banner ("SET PORT MAPPINGS")
	
	stc.perform("SetupPortMappings")
	hProject = stc.get("system1", "children-project")
	portList = stc.get(hProject, "children-port")
	deviceList = stc.get(hProject, "children-emulateddevice")
	sb_list = []
	portList = portList.split()
	for port in portList :
		sb = stc.get(port, 'children-streamblock');
		sb_list.append(sb );
	
	# Banner log output - Start all Traffics
	connection_obj.banner ("START ALL TRAFFICS")
	
	stc.perform("DevicesStartAll")
	stc.perform("streamblockstartcommand" , StreamBlockList = sb_list)
	
	# Banner log output - Subscribe for Statistics
	connection_obj.banner ("SUBSCRIBE FOR STATISTICS")
	
	rds1 = stc.subscribe(Parent=hProject, resultparent=sb_list, ConfigType="StreamBlock", viewAttributeList= ['FrameCount', 'FrameRate'], resulttype="TxStreamResults")
	rds2 = stc.subscribe(Parent=hProject, resultparent=sb_list, ConfigType="StreamBlock", viewAttributeList= ['FrameCount', 'FrameRate'], resulttype="RxStreamSummaryResults")
	time.sleep(10)
	
	resultList1 = stc.get(rds1, "ResultHandleList")
	resultList2 = stc.get(rds2, "ResultHandleList")
	resultList1 = resultList1.split()
	resultList2 = resultList2.split()
	
	for result1 in resultList1 :
		TxRate = stc.get(result1, "FrameRate");
		
	for result1 in resultList2 :
		RxRate = stc.get(result1, "FrameRate");
	
	print "\n======================================="
	print "|||||||| TX RATE       |      ", TxRate, "|"
	print "======================================="
	print "======================================="
	print "|||||||| RX RATE       |      ", RxRate, "|"
	print "======================================="
	
	# Comparing TX rate and RX rate
	if ( int(TxRate) - int(RxRate) != 0):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : Transmitted RATE and Recieved RATE are different *****")
		
	# Banner log output - Refresh Statistics
	connection_obj.banner ("REFRESH STATISTICS")
	
	stc.perform("RefreshResultViewCommand" , ResultDataSet = rds1)
	stc.perform("RefreshResultViewCommand" , ResultDataSet = rds2)
	
	# Banner log output - Stop Trafic
	connection_obj.banner ("STOP TRAFIC")
	
	stc.perform("streamblockstopcommand" , StreamBlockList = sb_list)
	time.sleep(5)
	
	# Banner log output - Get Traffic results
	connection_obj.banner ("GET TRAFFIC RESULTS")
	
	resultList1 = stc.get(rds1, "ResultHandleList")
	resultList2 = stc.get(rds2, "ResultHandleList")
	resultList1 = resultList1.split()
	resultList2 = resultList2.split()
	
	for result1 in resultList1 : 
		TxCount = stc.get(result1, "FrameCount");
		
	for result1 in resultList2 : 
		RxCount = stc.get(result1, "FrameCount");
		
	print "\n==============================================="
	print "|||||||| TX FRAME COUNT       |      ", TxCount, "  |"
	print "==============================================="
	print "==============================================="
	print "|||||||| RX FRAME COUNT       |      ", RxCount, "  |"
	print "==============================================="

	# Comparing TX frame count and RX frame count
	if (((int(TxCount) - int(RxCount))/100) > 4):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : Traffic loss (TX frame count - RX frame count) is more than acceptable difference *****")
	
	# Banner log output - Stop all STC devices
	connection_obj.banner ("STOP ALL STC DEVICES")
	
	stc.perform("DevicesStopAllCommand")
	
	# Banner log output - Disconnect STC Chassis
	connection_obj.banner ("DISCONNECT STC CHASSIS")
	
	stc.disconnect()
	time.sleep(5)
	
	# Banner log output
	connection_obj.banner ("VLAN DELETION PART")
	
	# VLAN deletion
	cmd ='''configure interface vlan100 delete
			configure vlan delete 100'''
	
	connection_obj.config(result,cmd)
	time.sleep(5)
	
	# Closing connection
	result.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
		
def SUITE_1_TC_25():
	
	# Establishing SSH connection
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 5 : VLAN REMOVAL AND TRAFFIC VERIFICATION")
	
	result = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	print(result.recv(100000000000000000))
	
	# Variable declarations
	DebugLogger.test_result_flag = 0
	stc = StcPython()
	szChassisIp = "192.168.0.15"
	port1 = "2/4"
	port2 = "2/7"
	port_list = ['$port1',' $port2']
	
	# Banner log output
	connection_obj.banner ("VLAN CONFIGURATION PART")
	
	# VLAN configurations
	cmd ='''configure vlan add 100
			configure vlan port 100 LAN2 tagged
			configure vlan port 100 LAN3 tagged
			configure vlan port 100 CPU tagged
			configure interface vlan100 add
			configure interface vlan100 ifname add eth0.100'''
	
	connection_obj.config(result,cmd)

	# Displays output of the command : "show vlan config"
	print (connection_obj.ssh_show_cmds(result, "\nshow vlan config"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show vlan config"
	out = connection_obj.show_cmds_vlan_config(result, "show vlan config")
	
	# Verification of configured VLAN ID : 100
	if (out['VLAN_ID'] != "100"):
		DebugLogger.test_result_flag += 1
	
	# Verification of VLAN 100 tagging : LAN2
	if (out['LAN2'] != "tagged"):
		DebugLogger.test_result_flag += 1
	
	# Verification of VLAN 100 tagging : LAN3
	if (out['LAN3'] != "tagged"):
		DebugLogger.test_result_flag += 1
		
	# Verification of VLAN 100 tagging : CPU
	if (out['CPU'] != "tagged"):
		DebugLogger.test_result_flag += 1
	
	# Banner log output - VLAN tag removal from interface LAN3
	connection_obj.banner ("VLAN TAG REMOVAL FROM INTERFACE LAN3")
	
	cmd ='''\nconfigure vlan port 100 LAN3 off'''
	connection_obj.config(result,cmd)
	
	# Displays output of the command : "show vlan config"
	print (connection_obj.ssh_show_cmds(result, "\nshow vlan config"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show vlan config"
	out = connection_obj.show_cmds_vlan_config(result, "show vlan config")
	
	# Verification of VLAN 100 tagging : LAN3
	if (out['LAN3'] != "off"):
		DebugLogger.test_result_flag += 1
	
	# Logging
	stc.config("automationoptions", logto="stdout", loglevel="INFO")
	
	# Banner log output - Loading saved traffic file
	connection_obj.banner ("LOADING SAVED TRAFFIC FILE")
	
	stc.perform("LoadFromDatabase", DatabaseConnectionString = "STC_file.tcc")
	stc.apply()
	
	# Banner log output - Connecting to STC Chassis : 192.168.0.15
	connection_obj.banner ("CONNECTING TO STC CHASSIS : 192.168.0.15")
	
	stc.connect(szChassisIp)
	
	# Banner log output - Reserving ports : 2/4 and 2/7
	connection_obj.banner ("RESERVING PORTS : 2/4 AND 2/7")
	
	stc.reserve("{0}/{1}/{2} {3}/{4}/{5}".format(szChassisIp, port1.split("/")[0], port1.split("/")[1], szChassisIp, port2.split("/")[0], port2.split("/")[1]))
	
	# Banner log output - Set port Mappings
	connection_obj.banner ("SET PORT MAPPINGS")
	
	stc.perform("SetupPortMappings")
	hProject = stc.get("system1", "children-project")
	portList = stc.get(hProject, "children-port")
	deviceList = stc.get(hProject, "children-emulateddevice")
	sb_list = []
	portList = portList.split()
	for port in portList :
		sb = stc.get(port, 'children-streamblock');
		sb_list.append(sb );
	
	# Banner log output - Start all Traffics
	connection_obj.banner ("START ALL TRAFFICS")
	
	stc.perform("DevicesStartAll")
	stc.perform("streamblockstartcommand" , StreamBlockList = sb_list)
	
	# Banner log output - Subscribe for Statistics
	connection_obj.banner ("SUBSCRIBE FOR STATISTICS")
	
	rds1 = stc.subscribe(Parent=hProject, resultparent=sb_list, ConfigType="StreamBlock", viewAttributeList= ['FrameCount', 'FrameRate'], resulttype="TxStreamResults")
	rds2 = stc.subscribe(Parent=hProject, resultparent=sb_list, ConfigType="StreamBlock", viewAttributeList= ['FrameCount', 'FrameRate'], resulttype="RxStreamSummaryResults")
	time.sleep(10)
	
	resultList1 = stc.get(rds1, "ResultHandleList")
	resultList2 = stc.get(rds2, "ResultHandleList")
	resultList1 = resultList1.split()
	resultList2 = resultList2.split()
	
	for result1 in resultList1 :
		TxRate = stc.get(result1, "FrameRate");
		
	for result1 in resultList2 :
		RxRate = stc.get(result1, "FrameRate");
	
	print "\n======================================="
	print "|||||||| TX RATE       |      ", TxRate, "|"
	print "======================================="
	print "======================================="
	print "|||||||| RX RATE       |      ", RxRate, "|"
	print "=======================================\n"
	
	# Comparing TX rate and RX rate
	if ( int(RxRate) > 100):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : Traffic was not dropped after removing VLAN Tag *****")
		
	# Banner log output - Refresh Statistics
	connection_obj.banner ("REFRESH STATISTICS")
	
	stc.perform("RefreshResultViewCommand" , ResultDataSet = rds1)
	stc.perform("RefreshResultViewCommand" , ResultDataSet = rds2)
	
	# Banner log output - Stop Trafic
	connection_obj.banner ("STOP TRAFIC")
	
	stc.perform("streamblockstopcommand" , StreamBlockList = sb_list)
	time.sleep(5)
	
	# Banner log output - Stop all STC devices
	connection_obj.banner ("STOP ALL STC DEVICES")
	
	stc.perform("DevicesStopAllCommand")
	
	# Banner log output - Disconnect STC Chassis
	connection_obj.banner ("DISCONNECT STC CHASSIS")
	
	stc.disconnect()
	time.sleep(5)
	
	# Banner log output
	connection_obj.banner ("VLAN DELETION PART")
	
	# VLAN deletion
	cmd ='''configure interface vlan100 delete
			configure vlan delete 100'''
	
	connection_obj.config(result,cmd)
	time.sleep(5)
	
	# Closing SSH connection
	result.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
		
def SUITE_1_TC_26():
	
	# Variable declarations
	DebugLogger.test_result_flag = 0
	
	# Establishing SSH connection (result1 - ATLAS and restult2 - LINUX)
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 6 : SNMP V1 CONFIGURATION AND VERIFICATION")
	
	result1 = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	result2 = connection_obj.ssh_connect(Config.s_host, Config.s_user, Config.s_passwd)
	time.sleep(5)
	print(result2.recv(100000000000000000))
	
	# Displays output of the command (ATLAS) : "show system status"
	print (connection_obj.ssh_show_cmds(result1, "\nshow system status"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show system status"
	out = connection_obj.show_cmds_system_status(result1, "show system status")
	
	# Displays ATLAS System up time obtained by the commmand : "show system status" 
	print ("\nAtlas system up time : "+ out['ATLAS_UP_TIME']+"\n")
	
	# Converting ATLAS_UP_TIME in to seconds
	Up_Time_1 = out['ATLAS_UP_TIME']
	Time_Atlas = connection_obj.time_to_seconds(Up_Time_1)

	# Displays output of the command (LINUX) : "\nsnmpget -v 1 -c public 192.168.1.1 sysUpTime.0"
	print (connection_obj.ssh_show_cmds(result2, "snmpget -v 1 -c public 192.168.1.1 sysUpTime.0"))
	time.sleep(5)

	# Dictionary creation (keys & values) for output of the command : "snmpget -v 1 -c public 192.168.1.1 sysUpTime.0"
	out = connection_obj.show_cmds_snmpget_sysUpTime(result2, "snmpget -v 1 -c public 192.168.1.1 sysUpTime.0")
	
	# Displays System up time obtained by snmpget command
	print ("\nSNMP system up time : "+ out['SNMP_UP_TIME'])

	# Converting SNMP_UP_TIME in to seconds
	Up_Time_2 = out['SNMP_UP_TIME']
	Time_Snmp = connection_obj.time_to_seconds(Up_Time_2)
	
	time.sleep(5)
	# Verifying whether ATLAS_UP_TIME and SNMP_UP_TIME are closely equal
	if (abs(Time_Snmp - Time_Atlas) > 50):
		DebugLogger.test_result_flag += 1
		# Banner log output
		connection_obj.banner ("***** FAIL : ATLAS up time and SNMP fetched up time are different *****")
	
	# Closing SSH connection
	result1.close()
	result2.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
		
def SUITE_1_TC_27():
	
	# Variable declarations
	DebugLogger.test_result_flag = 0
	
	# Establishing SSH connection (result1 - ATLAS and restult2 - LINUX)
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 7 : SNMP V2 CONFIGURATION AND VERIFICATION")
	
	result1 = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	result2 = connection_obj.ssh_connect(Config.s_host, Config.s_user, Config.s_passwd)
	time.sleep(5)
	print(result2.recv(100000000000000000))
	
	# Displays output of the command (ATLAS) : "show system status"
	print (connection_obj.ssh_show_cmds(result1, "\nshow system status"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show system status"
	out = connection_obj.show_cmds_system_status(result1, "show system status")
	
	# Displays ATLAS System up time obtained by the commmand : "show system status" 
	print ("\nAtlas system up time : "+ out['ATLAS_UP_TIME']+"\n")
	
	# Converting ATLAS_UP_TIME in to seconds
	Up_Time_1 = out['ATLAS_UP_TIME']
	Time_Atlas = connection_obj.time_to_seconds(Up_Time_1)
	
	# Displays output of the command (LINUX) : "\nsnmpget -v 2c -c public 192.168.1.1 sysUpTime.0"
	print (connection_obj.ssh_show_cmds(result2, "snmpget -v 2c -c public 192.168.1.1 sysUpTime.0"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "snmpget -v 1 -c public 192.168.1.1 sysUpTime.0"
	out = connection_obj.show_cmds_snmpget_sysUpTime(result2, "snmpget -v 2c -c public 192.168.1.1 sysUpTime.0")
	
	# Displays System up time obtained by snmpget command
	print ("\nSNMP system up time : "+ out['SNMP_UP_TIME'])
	
	# Converting SNMP_UP_TIME in to seconds
	Up_Time_2 = out['SNMP_UP_TIME']
	Time_Snmp = connection_obj.time_to_seconds(Up_Time_2)
	
	time.sleep(5)
	# Verifying whether ATLAS_UP_TIME and SNMP_UP_TIME are closely equal
	if (abs(Time_Snmp - Time_Atlas) > 50):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : ATLAS up time and SNMP fetched up time are different *****")
	
	# Closing SSH connection
	result1.close()
	result2.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
		
def SUITE_1_TC_28():
	
	# Variable declarations
	DebugLogger.test_result_flag = 0
	
	# Establishing SSH connection (result1 - ATLAS and restult2 - LINUX)
	connection_obj = connection.connection(Config.host, Config.user, Config.passwd)
	
	# Banner log output
	connection_obj.banner ("TEST CASE 8 : SNMP V3 CONFIGURATION AND VERIFICATION")
	
	result1 = connection_obj.ssh_connect(Config.host, Config.user, Config.passwd)
	time.sleep(5)
	result2 = connection_obj.ssh_connect(Config.s_host, Config.s_user, Config.s_passwd)
	time.sleep(5)
	print(result2.recv(100000000000000000))

	# SNMP V3 - NO_AUTH_NO_PRIV CASE
	
	# Banner log output
	connection_obj.banner ("SNMP V3 (NO_AUTH_NO_PRIV) CONFIGURATION/DELETION AND VERIFICATION")
	
	# Displays output of the command (ATLAS) : "show system status"
	print (connection_obj.ssh_show_cmds(result1, "\nshow system status"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show system status"
	out = connection_obj.show_cmds_system_status(result1, "show system status")
	
	# Displays ATLAS System up time obtained by the commmand : "show system status" 
	print ("\nAtlas system up time : "+ out['ATLAS_UP_TIME']+"\n")
	
	# Converting ATLAS_UP_TIME in to seconds
	Up_Time_1 = out['ATLAS_UP_TIME']
	Time_Atlas = connection_obj.time_to_seconds(Up_Time_1)
	
	# SNMP v3 (NoAuthNoPriv) configurations
	cmd ='''configure snmp enable true
			configure snmp v3 user thinkpalmuser
			configure snmp v3 user thinkpalmuser securityLevel noAuthNoPriv'''
	connection_obj.config(result1,cmd)

	# Displays output of the command (ATLAS) : "show snmp config v3"
	print (connection_obj.ssh_show_cmds(result1, "show snmp config v3"))
	time.sleep(10)
	
	# Displays output of the command (LINUX) : "snmpget -v 3 -u thinkpalmuser -l NoauthNoPriv 192.168.1.1 sysUpTime.0"
	print (connection_obj.ssh_show_cmds(result2, "snmpget -v 3 -u thinkpalmuser -l NoauthNoPriv 192.168.1.1 sysUpTime.0"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "snmpget -v 3 -u thinkpalmuser -l NoauthNoPriv 192.168.1.1 sysUpTime.0"
	out = connection_obj.show_cmds_snmpget_sysUpTime(result2, "snmpget -v 3 -u thinkpalmuser -l NoauthNoPriv 192.168.1.1 sysUpTime.0")
	
	# Displays System up time obtained by snmpget command
	print ("\nSNMP system up time : "+ out['SNMP_UP_TIME'])
	
	# Converting SNMP_UP_TIME in to seconds
	Up_Time_2 = out['SNMP_UP_TIME']
	Time_Snmp = connection_obj.time_to_seconds(Up_Time_2)

	time.sleep(5)
	# Verifying whether ATLAS_UP_TIME and SNMP_UP_TIME are closely equal
	if (abs(Time_Snmp - Time_Atlas) > 50):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : ATLAS up time and SNMP fetched up time are different *****")
		
	# SNMP v3 (noAuthNoPriv) configuration deletion
	cmd ='''configure snmp v3 user thinkpalmuser delete
			configure snmp enable false'''
	connection_obj.config(result1,cmd)
	time.sleep(5)

	# SNMP V3 - AUTH_NO_PRIV CASE
	
	# Banner log output
	connection_obj.banner ("SNMP V3 (AUTH_NO_PRIV) CONFIGURATION/DELETION AND VERIFICATION")
	
	# Displays output of the command (ATLAS) : "show system status"
	print (connection_obj.ssh_show_cmds(result1, "\nshow system status"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show system status"
	out = connection_obj.show_cmds_system_status(result1, "show system status")
	
	# Displays ATLAS System up time obtained by the commmand : "show system status" 
	print ("\nAtlas system up time : "+ out['ATLAS_UP_TIME']+"\n")
	
	# Converting ATLAS_UP_TIME in to seconds
	Up_Time_1 = out['ATLAS_UP_TIME']
	Time_Atlas = connection_obj.time_to_seconds(Up_Time_1)
	
	# SNMP v3 (AuthPriv) configurations
	cmd ='''configure snmp enable true
			configure snmp v3 user thinkpalmuser
			configure snmp v3 user thinkpalmuser securityLevel authNoPriv authProtocol MD5 authKey thinkpalmuser'''
	connection_obj.config(result1,cmd)

	# Displays output of the command (ATLAS) : "show snmp config v3"
	print (connection_obj.ssh_show_cmds(result1, "show snmp config v3"))
	time.sleep(10)
	
	# Displays output of the command (LINUX) : "snmpget -v 3 -u thinkpalmuser -l authNoPriv -a MD5 -A thinkpalmuser 192.168.1.1 sysUpTime.0"
	print (connection_obj.ssh_show_cmds(result2, "snmpget -v 3 -u thinkpalmuser -l authNoPriv -a MD5 -A thinkpalmuser 192.168.1.1 sysUpTime.0"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "snmpget -v 3 -u thinkpalmuser -l authNoPriv -a MD5 -A thinkpalmuser 192.168.1.1 sysUpTime.0"
	out = connection_obj.show_cmds_snmpget_sysUpTime(result2, "snmpget -v 3 -u thinkpalmuser -l authNoPriv -a MD5 -A thinkpalmuser 192.168.1.1 sysUpTime.0")
	
	# Displays System up time obtained by snmpget command
	print ("\nSNMP system up time : "+ out['SNMP_UP_TIME'])
	
	# Converting SNMP_UP_TIME in to seconds
	Up_Time_2 = out['SNMP_UP_TIME']
	Time_Snmp = connection_obj.time_to_seconds(Up_Time_2)
	
	time.sleep(5)
	# Verifying whether ATLAS_UP_TIME and SNMP_UP_TIME are closely equal
	if (abs(Time_Snmp - Time_Atlas) > 50):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : ATLAS up time and SNMP fetched up time are different *****")
	
	# SNMP v3 (AuthNoPriv) configuration deletion
	cmd ='''configure snmp v3 user thinkpalmuser delete
			configure snmp enable false'''
	connection_obj.config(result1,cmd)
	time.sleep(5)

	# SNMP V3 - AUTH_PRIV CASE
	
	# Banner log output
	connection_obj.banner ("SNMP V3 (AUTH_PRIV) CONFIGURATION/DELETION AND VERIFICATION")
	
	# Displays output of the command (ATLAS) : "show system status"
	print (connection_obj.ssh_show_cmds(result1, "\nshow system status"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "show system status"
	out = connection_obj.show_cmds_system_status(result1, "show system status")
	
	# Displays ATLAS System up time obtained by the commmand : "show system status" 
	print ("\nAtlas system up time : "+ out['ATLAS_UP_TIME']+"\n")
	
	# Converting ATLAS_UP_TIME in to seconds
	Up_Time_1 = out['ATLAS_UP_TIME']
	Time_Atlas = connection_obj.time_to_seconds(Up_Time_1)
	
	# SNMP v3 (AuthPriv) configurations
	cmd ='''configure snmp enable true
			configure snmp v3 user thinkpalmadmin
			configure snmp v3 user thinkpalmadmin securityLevel authPriv authProtocol MD5 authKey thinkpalmadmin privProtocol DES privKey thinkpalmadminencryption'''
	connection_obj.config(result1,cmd)

	# Displays output of the command (ATLAS) : "show snmp config v3"
	print (connection_obj.ssh_show_cmds(result1, "show snmp config v3"))
	time.sleep(10)
	
	# Displays output of the command (LINUX) : "snmpget -v 3 -u thinkpalmadmin -l authPriv -a MD5 -A thinkpalmadmin -x DES -X thinkpalmadminencryption 192.168.1.1 sysUpTime.0"
	print (connection_obj.ssh_show_cmds(result2, "snmpget -v 3 -u thinkpalmadmin -l authPriv -a MD5 -A thinkpalmadmin -x DES -X thinkpalmadminencryption 192.168.1.1 sysUpTime.0"))
	time.sleep(5)
	
	# Dictionary creation (keys & values) for output of the command : "snmpget -v 3 -u thinkpalmadmin -l authPriv -a MD5 -A thinkpalmadmin -x DES -X thinkpalmadminencryption 192.168.1.1 sysUpTime.0"
	out = connection_obj.show_cmds_snmpget_sysUpTime(result2, "snmpget -v 3 -u thinkpalmadmin -l authPriv -a MD5 -A thinkpalmadmin -x DES -X thinkpalmadminencryption 192.168.1.1 sysUpTime.0")
	
	# Displays System up time obtained by snmpget command
	print ("\nSNMP system up time : "+ out['SNMP_UP_TIME'])

	# Converting SNMP_UP_TIME in to seconds
	Up_Time_2 = out['SNMP_UP_TIME']
	Time_Snmp = connection_obj.time_to_seconds(Up_Time_2)

	time.sleep(5)
	# Verifying whether ATLAS_UP_TIME and SNMP_UP_TIME are closely equal
	if (abs(Time_Snmp - Time_Atlas) > 50):
		DebugLogger.test_result_flag += 1
		connection_obj.banner ("***** FAIL : ATLAS up time and SNMP fetched up time are different *****")
	
	# SNMP v3 (noAuthNoPriv) configuration deletion
	cmd ='''configure snmp v3 user thinkpalmadmin delete
			configure snmp enable false'''
	connection_obj.config(result1,cmd)
	time.sleep(5)
	
	# Closing SSH connection
	result1.close()
	result2.close()
	
	# Test case validation
	if (DebugLogger.test_result_flag == 0):
		logger_obj.bannerInfo('PASSED', 'RESULT')
	else:
		logger_obj.bannerInfo('FAILED', 'RESULT')
