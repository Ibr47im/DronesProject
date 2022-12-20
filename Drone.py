import UDPServer
from mavsdk import System
import asyncio

class Drone:
    def __init__(self) -> None:

        self.Sys_id=1
        self.udp_server = UDPServer.UDPServer()
        self.udp_server.init_server()
        self.drone=System()
        self.armed=False

    async def init_drone(self):

        print("Connecting to drone ...")
        await self.drone.connect(system_address="udp://:14540")

        print("Waiting for drone to connect...")
        async for state in self.drone.core.connection_state():
            if state.is_connected:
                print(f"-- Connected to drone!")
                break

        print("Waiting for drone to have a global position estimate...")
        async for health in self.drone.telemetry.health():
            if health.is_global_position_ok and health.is_home_position_ok:
                print("-- Global position estimate OK")
                break
        print("Fetching amsl altitude at home location....")


    async def start_drone_receive(self):
        while(True):
            self.message ,self.client_ip=self.udp_server.start_server()
            
            print(self.message["Header"])
            if(self.message["Payload"][0]==1 and not self.armed):
                await self.arm()
                self.armed=True
            elif(self.message["Payload"][0]==2):

                height=self.message["Payload"][1]
                await self.takeoff(height)
            elif(self.message["Payload"][0]==3):
                await self.land()
                
            elif(self.message["Payload"][0]==4):
                await self.disarm()
            elif(self.message["Payload"][0]==5):
                target_location=self.message["Payload"][1]
                await self.goto(target_location)

            await self.info()
    
    async def arm(self):
        print("Arming")
        await self.drone.action.arm()

    async def takeoff(self, height):
        if(not self.armed):
            await self.arm()

        print("Taking off")
        await self.drone.action.set_takeoff_altitude(height)
        await self.drone.action.takeoff()

    async def disarm(self):
        await self.drone.action.disarm()
        #self.armed = False
   
    async def land(self):
        await self.drone.action.land()

    async def heartbeat(self): 
        pass
      
    async def info(self): 
        gps_infromation=None
        armed_state=None
        latitude=None
        longitude=None
        async for gps_info in self.drone.telemetry.gps_info():
            gps_infromation=gps_info
            print(f"GPS info: {gps_info}")
            break
        async for arming in self.drone.telemetry.armed():
            armed_state=arming
            print(f"Armed info: {arming}")
            break
        async for terrain_info in self.drone.telemetry.home():
            latitude = terrain_info.latitude_deg
            longitude = terrain_info.longitude_deg
            break
        self.udp_server.send(f'gps_infromation are: {gps_infromation} \n armed_state {armed_state} \n latitude {latitude} \n{longitude}')

        
    async def goto(self,target_location:list):
        await self.drone.action.goto_location(target_location[0], target_location[1], target_location[2], target_location[3])

            
            
        

 
   


     
        
    

    

        
    

