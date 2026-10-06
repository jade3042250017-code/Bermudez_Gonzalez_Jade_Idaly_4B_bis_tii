# JADE IDALY BERMUDEZ GONZALEZ 4B BIS 
#UNIVERSIDAD TECNOLÓGICA DE DURANGO
#Practical Exam: Introduction to Object-Oriented Programming 
#Professor: Eng. Pedro Said Vara Chacón 
#Subject: Software Development



class Server:

    def __init__(self, hostname: str, ip_address: str, ram_capacity: int):
        self.hostname = hostname
        self.ip_address = ip_address
        self.ram_capacity = ram_capacity
        self.is_powered_on = False 

    def power_on(self):



        self.is_powered_on = True
        print(f"El servidor '{self.hostname}' ha sido encendido.")

    def power_off(self):
        self.is_powered_on = False
        print(f"El servidor '{self.hostname}' ha sido apagado.")

    def update_ram(self, new_ram: int):
        self.ram_capacity = new_ram
        print(
            f"La memoria RAM de '{self.hostname}' se actualizó a {self.ram_capacity} GB."
        )

#---------------------------------------------- para no confundirme pongo una division aqui#
class DataCenter:
    
    def __init__(self, region_name: str):
       
        self.region_name = region_name
        self.servers = []  

    def register_server(self, server: Server):
        self.servers.append(server)
        print(
            f"Servidor '{server.hostname}' registrado en el Data Center de {self.region_name}."
        )

    def display_active_servers(self):
        active_hostnames = [
            s.hostname for s in self.servers if s.is_powered_on
        ]

        print(f"\nservidores activos en {self.region_name} ---")
        if active_hostnames:
            for hostname in active_hostnames:
                print(f"- {hostname}")
        else:
            print("No hay servidores encendidos en este momento.")


if __name__ == "__main__":
    
    dc_us_east = DataCenter(region_name="us-east-1")

    server1 = Server(
        hostname="srv-web-01", ip_address="192.168.1.10", ram_capacity=16
    )
    server2 = Server(
        hostname="srv-db-01", ip_address="192.168.1.20", ram_capacity=32
    )
    print()

    
    dc_us_east.register_server(server1)
    dc_us_east.register_server(server2)
    print()

    server2.power_on()  
    dc_us_east.display_active_servers()
