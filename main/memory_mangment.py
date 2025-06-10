#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/.venv/lib/python3.11.9

import re
import subprocess

class Memory_tester():
	def __init__(self):
		self.units={"K":10e3,"M": 10e6,"G":10e9}
		self.regex ="^(\d+(?:\.\d+)?[K,M,G])"
		self.fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/bash_scrpits/memorytest.sh" 
		self.output_bash=subprocess.run(['bash',self.fname],capture_output=True,text=True)
	def check_memory(self):
		try:
			match=re.match(self.regex,self.output_bash.stdout[:-1])
			if match:
				value,unit=self.output_bash.stdout[:-1][:-1],self.output_bash.stdout[:-1][-1:]
				try:
					return float(value)*self.units[unit]
				except KeyError:
					raise ValueError(f"unknown unit: {unit}")
		except subprocess.CalledProcessError as e:
			raise ValueError(f"Error running script:{e.output}")
	def error_check(self):
		mem=round(self.check_memory())
		max=32*10e9
		if mem >= round(0.2* max):
			raise MemoryError("memory on pi is about to  used up")

if __name__=="__main__":

	Memory_tester()
