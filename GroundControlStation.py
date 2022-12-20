import json
import asyncio
import UDPClient
import  datetime

class GroundControlStation:
    def __init__(self) -> None:
        self.UDPCLinet=UDPClient.UDPClient()
        self.UDPCLinet.connect()
        self.sys_id=3
        self.mesg_counter=1
        
   
    
    def send(self,message):
        bytes_to_send = str.encode(message)
        self.UDPCLinet.send(bytes_to_send)

    def hear(self):
       print( self.UDPCLinet.receive())


    def arm(self):
        print("arm")
        arm_dic={"Header":[self.sys_id,self.mesg_counter,str(datetime.datetime.now())]
        ,"Payload":[1]}
        self.UDPCLinet.send(json.dumps(arm_dic))
        self.mesg_counter+=1

    def takeoff(self, altitude):
        takeoff_dict={"Header":[self.sys_id,self.mesg_counter,str(datetime.datetime.now())]
        ,"Payload":[2,altitude]}
        takeoff_msg = json.dumps(takeoff_dict)
        print("takeoff")
        self.UDPCLinet.send(takeoff_msg)
        self.mesg_counter+=1


    def land(self):
        print("land")
        land_dict={"Header":[self.sys_id,self.mesg_counter,str(datetime.datetime.now())]
        ,"Payload":[3]}
        self.UDPCLinet.send(json.dumps(land_dict))
        self.mesg_counter+=1
 

    def disarm(self):
        print("disarm")
        disarm_dict={"Header":[self.sys_id,self.mesg_counter,str(datetime.datetime.now())]
        ,"Payload":[4]}
        self.UDPCLinet.send(json.dumps(disarm_dict))
        self.mesg_counter+=1

        

    def goto(self,target_location:list):
        goto_dict={"Header":[self.sys_id,self.mesg_counter,str(datetime.datetime.now())]
        ,"Payload":[5,target_location]}
        goto_msg = json.dumps(goto_dict)
        print("goto")
        self.UDPCLinet.send(goto_msg)
        self.mesg_counter+=1


        
    



                