from ast import Raise
from uu import Error
import numpy as np
import subprocess
import re
def Read_DHT22(port_number:int) ->tuple: 
    return 0.000,1,000
def Read_MCP3008(channel:int,port_number:int)->float:
    output=4.333333333333
    return output
def Read_AS312(port_number:int)->bool:
    return False
def Read_Raspberry_PiVR220()->np.ndarray:
    output=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    return output
def Read_Memory_module()->int:
    output=subprocess.check_output(["bash","test.sh"],universal_newlines=True)
    K=10e3
    M=10e6
    G=10e9
    regex="\d{4}(KMG)"
    match= re.match(regex,output)
    if match:
        integer=match.group(1)
        unit=match.group(2)
        if unit=="K":
            return int(integer)*K
        if unit=="M":
            return int(integer)*M
        if unit=="G":
            return int(integer)*G
    else:
        Raise Error("")