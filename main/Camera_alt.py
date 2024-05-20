#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/new_env/lib/python3.9
import subprocess
class camera:
    def __init__(self):
        self.run=subprocess.run(["bash","/home/mistaherd/Documents/Github/meshnetwork_in_forest/bash_scrpits/camerea.sh"])
if __name__=="__main__":
    camera()
