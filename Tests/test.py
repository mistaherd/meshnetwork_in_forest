message=list("hello world")
message =[bytes(message[i],'utf-8').hex() for i in range(len(message))]
# message="".join(chr(int(message[i],16)) for i in range(len(message)))
message=",".join(message).encode()

message.decode().split(',')