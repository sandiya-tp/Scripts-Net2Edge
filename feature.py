import telnetlib
import time
import pexpect
import subprocess
import re

class feature:
    username = ""
    password = ""
    con = ""
    logger_obj = ""
    flag = 0

    def __init__(self, con_obj, command, logger_obj):
        self.con_obj = con_obj
        self.command = command
        self.logger_obj = logger_obj

    def show_version(self):
        try:
           self.logger_obj.log_info("Inside Feature check...")
           self.logger_obj.log_print("\nInside Feature check...\n")
           output = self.con_obj.exec_command("show file sw-pack")
           match = re.search('main\s+([a-z A-Z]+)\.bin\s+([0-9]\.[0-9]\.[0-9]\([0-9]\.[0-9]\))\s+([0-9]\.[0-9])\s+[0-9]+', output)
	   if match is not None:
	     self.logger_obj.log_print("\nSoftware Version is  " +  match.group(2))
             self.logger_obj.log_info("\nSoftware Version is  " +  match.group(2))
	   else:
	     self.logger_obj.log_print("\nSoftware Version is not found")
             self.logger_obj.log_info("\nSoftware Version is not found")
             self.logger_obj.bannerInfo('Unable get software version', 'ERROR')
        except:
            raise
            self.logger_obj.log_exception()
        
    def CPU_Measurement(self):
        try:
           output = self.con_obj.exec_command("show configure system cpu-utilization")
           match = re.search('Min.*\s+(\d+)\s+Cur.*\s+(\d+)\s+Max.*\s+(\d+)\s+Average.*\s+(\d+)', output)
           if match is not None:
	     CPU_Values = {'Min': int(match.group(1)), 'Cur': int(match.group(2)), 'Max': int(match.group(3)), 'Average': int(match.group(4))}
             self.logger_obj.log_print("\nCPU values are  " + '\tMinimum:' + match.group(1) + '\tCurrent:' + match.group(2) + '\tMaximum:' + match.group(3) + '\tAverage:' + match.group(4))
             self.logger_obj.log_info("\nCPU values are  " + match.group(1) +  match.group(2) + match.group(3) + match.group(4))
	     return CPU_Values
           else:
             self.logger_obj.log_print("\nError while measuring CPU utilization\n")
             self.logger_obj.log_info("\nError while measuring CPU utilization\n")

        except:
            raise
            self.logger_obj.log_exception()

    def CPU_Comparison(self, MeasurementsA, MeasurementsB, Threshold):
	flag = 0       		
	try:
	  cur_Percentage = (MeasurementsB['Cur'] - MeasurementsA['Cur'])/MeasurementsB['Cur'] * 100
	  max_Percentage = ((MeasurementsB['Max'] - MeasurementsA['Max'])/MeasurementsB['Max']) * 100		                              
          avg_Percentage = ((MeasurementsB['Average'] - MeasurementsA['Average'])/MeasurementsB['Average']) * 100
	  if cur_Percentage >= Threshold:
	    flag = 1
	  if max_Percentage >= Threshold:
	    flag = 1
          if avg_Percentage >= Threshold:
            flag = 1
          if flag:
	     self.logger_obj.log_print("\nFailed, CPU utilization is more than threshold value\n")
             self.logger_obj.log_info("\nFailed, CPU utilization is more than threshold value\n")
          else:
             self.logger_obj.log_print("\nCPU utilization is normal during test for the threshold value\n")
             self.logger_obj.log_info("\nCPU utilization is normal during test for the threshold value\n")

        except:
          raise
          self.logger_obj.log_exception()
		  

    def Bulk_configuration(self, commands):
        
        self.logger_obj.log_info("Inside feature.Bulk_configuration()")
        self.logger_obj.log_print("\nConfiguring DUT...\n")
        return_status = False
        try:
            for command in commands.splitlines():
	   	self.con_obj.exec_command(command)
        except:
            self.logger_obj.log_error(sys.exc_info())
        else:
            return return_status

    def Interface_status(self, inerface_list, status):

        return_status = False
        time_status = 0
        try:
            output = self.con_obj.exec_command('show configure port ethernet 3 status')
            print(output)
        except:
            self.logger_obj.log_error(sys.exc_info())
        else:
            return return_status
            
