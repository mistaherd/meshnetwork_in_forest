import numpy as np
import subprocess
import re
#def Read_DHT22(port_number:int) ->tuple: 
#    return 0.000,1,000
#def Read_MCP3008(channel:int,port_number:int)->float:
#    output=4.333333333333
#    return output
#def Read_AS312(port_number:int)->bool:
#    return False
#def Read_Raspberry_PiVR220()->np.ndarray:
#    output=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#    return output
def Read_Memory_module():
	units ={"K": 10e3,"M": 10e6, "G": 10e9}
	try:
 		output=subprocess.check_output(["bash","test.sh"],universal_newlines=True)
    		regex="\d{4}\.\[0-9]{1,3}[K,M,G]"
   		match= re.search(regex,output)
		if match:
			value,unit=match.group(0).split()
			try:
				return float(value)*units[unit]
			except KeyError:
				raise ValueError(f"unknown unit: {unit}")
	except subprocess.CalledProcessError as e:
	raise ValueError(f"Error running script:{e.output}")
Read_Memory_module()
