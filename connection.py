import paramiko
import time
import re
import logging
import socket
logging.basicConfig(level = logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class connection:

	def __init__(self, host, username, password):
		
		self.host = host
		self.username = username
		self.password = password
		
	def ssh_connect(self, host, username, password):
		
		try:
			remote_conn_pre=paramiko.SSHClient()
                        print "I am here :",remote_conn_pre
			remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			remote_conn_pre.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)
			return remote_conn_pre.invoke_shell()
		
		except paramiko.AuthenticationException:
			print "Authentication failed, please verify your credentials"
		
		except paramiko.SSHException as sshException:
			print "Could not establish SSH connection: %s" % sshException
		
		except socket.timeout as e:
			print "Connection timed out"
		
		except Exception,e:
			print "Exception in connecting to the server"
			print "PYTHON SAYS:",e
			self.client.close()
		
	def config(self, remote_con, config):
		
		try:
			for i in config.split("\n"):
				i = i.strip()+"\n"
				remote_con.send(i)
				time.sleep(5)
				print remote_con.recv(1000000000)
			
		except Exception as e:
			print "Error : Invalid configuration"
			print ("Error : Invalid configuration due to : ", e)
			
	
	def banner(self, cmd):
		print ("\n")
		logging.info("#"*len(cmd)+"########")
		logging.info("#"+"   "+cmd+"   "+"#")
		logging.info("#"*len(cmd)+"########")
		print ("\n")
		
	def ssh_show_cmds(self, remote_con, cmd):
		
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			return remote_con.recv(1000000000)
		
		except:
			print "Error : Invalid show command"

	def show_cmds_sw_version(self, remote_con, cmd):
		
		k = {}
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			output = remote_con.recv(1000000000)
			for out in output.split("\n"):
				pattern = "Model:\s+(.*)"
				if re.search(pattern, out):
					k['Model'] = re.search(pattern, out).group(1).strip()
				pattern = "Firmware\s+Version:\s+(.*)"
				if re.search(pattern, out):
					k['Firmware_Version'] = re.search(pattern, out).group(1).strip()
				pattern = "Distribution:\s+(.*)"
				if re.search(pattern, out):
					k['Distribution'] = re.search(pattern, out).group(1).strip()
				pattern = "board-id:\s+(.*),\s+MP\s+version\s+(.*)"
				if re.search(pattern, out):
					k['Board_id'] = re.search(pattern, out).group(1).strip()
					k['MP_version'] = re.search(pattern, out).group(2).strip()
				pattern = "mac-address:\s+(.*)"
				if re.search(pattern, out):
					k['Mac_address'] = re.search(pattern, out).group(1).strip()
				pattern = "serial-number:\s+(.*)"
				if re.search(pattern, out):
					k['Serial_number'] = re.search(pattern, out).group(1).strip()
			return k
		
		except:
			print "Error : Invalid show command"
			
	def show_cmds_stp_status(self, remote_con, cmd):
		
		k = {}
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			output = remote_con.recv(1000000000)
			for out in output.split("\n"):
				pattern = "STP Enabled\s+:\s+(\w+)"
				if re.search(pattern, out):
					k['STP_Enabled'] = re.search(pattern, out).group(1).strip()
				pattern = "Bridge\s+ID\s+:\s+(.*)"
				if re.search(pattern, out):
					k['Bridge_ID'] = re.search(pattern, out).group(1).strip()
				pattern = "Designated\s+root\s+:\s+(.*)"
				if re.search(pattern, out):
					k['Designated_root'] = re.search(pattern, out).group(1).strip()
				pattern = "Port\s+:\s+(.*)"
				if re.search(pattern, out):
					k['Port'] = re.search(pattern, out).group(1).strip()
				pattern = "Port\sID\s+:\s+(.*)"
				if re.search(pattern, out):
					k['Port_ID'] = re.search(pattern, out).group(1).strip()
				pattern = "State\s+:\s+(.*)"
				if re.search(pattern, out):
					k['State'] = re.search(pattern, out).group(1).strip()
			return k
		
		except:
			print "Error : Invalid show command"

	def show_cmds_stp_config(self, remote_con, cmd):
		
		k = {}
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			output = remote_con.recv(1000000000)
			for out in output.split("\n"):
				pattern = "\|\s+(br-lan)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(\d+)\s+\|\s+(eth0.1)\s+\|"
				if re.search(pattern, out):
					k['Bridge_Name'] = re.search(pattern, out).group(1).strip()
					k['Max_age'] = re.search(pattern, out).group(2).strip()
					k['Hello_time'] = re.search(pattern, out).group(3).strip()
					k['Forward_delay'] = re.search(pattern, out).group(4).strip()
					k['Ports'] = re.search(pattern, out).group(5).strip()
			return k
		
		except:
			print "Error : Invalid show command"
			
	def show_cmds_vlan_config(self, remote_con, cmd):
		
		k = {}
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			output = remote_con.recv(1000000000)
			for out in output.split("\n"):
				pattern = "\|\s+(100)\s+(off)\s+(tagged)\s+(\w+)\s+(off)\s+(off)\s+(tagged)\s+\|"
				if re.search(pattern, out):
					k['VLAN_ID'] = re.search(pattern, out).group(1).strip()
					k['LAN1'] = re.search(pattern, out).group(2).strip()
					k['LAN2'] = re.search(pattern, out).group(3).strip()
					k['LAN3'] = re.search(pattern, out).group(4).strip()
					k['LAN4'] = re.search(pattern, out).group(5).strip()
					k['WAN'] = re.search(pattern, out).group(6).strip()
					k['CPU'] = re.search(pattern, out).group(7).strip()
			return k
		
		except:
			print "Error : Invalid show command"
			
	def show_cmds_snmpget_sysUpTime(self, remote_con, cmd):
		
		k = {}
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			output = remote_con.recv(1000000000)
			for out in output.split("\n"):
				pattern = "DISMAN-EVENT-MIB::sysUpTimeInstance\s+=\s+Timeticks:\s+\(\d+\)\s+(.*)"
				if re.search(pattern, out):
					k['SNMP_UP_TIME'] = re.search(pattern, out).group(1).strip()
			return k
		
		except:
			print "Error : Invalid show command"
			
	def show_cmds_system_status(self, remote_con, cmd):
		
		k = {}
		try:
			cmd = cmd+"\n"
			remote_con.send(cmd)
			time.sleep(5)
			output = remote_con.recv(1000000000)
			for out in output.split("\n"):
				pattern = "Up\s+Time:\s+(.*)"
				if re.search(pattern, out):
					k['ATLAS_UP_TIME'] = re.search(pattern, out).group(1).strip()
			return k
		
		except:
			print "Error : Invalid show command"
			
	def time_to_seconds(self, UP_TIME):
	
		k = {}
		try:
			pattern = "(\d+):(\d+):(\d+)"
			if re.search(pattern, UP_TIME):
					k['HOURS'] = re.search(pattern, UP_TIME).group(1).strip()
					k['MINUTES'] = re.search(pattern, UP_TIME).group(2).strip()
					k['SECONDS'] = re.search(pattern, UP_TIME).group(3).strip()
					
			total_seconds = (int(k['HOURS']) * 3600) + (int(k['MINUTES']) * 60) + int(k['SECONDS'])
			
			return total_seconds
		
		except:
			print "Error : Conversion to seconds failed"
