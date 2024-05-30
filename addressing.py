import storage
import storage

class Access:
    @staticmethod
    def data(addr, flow=["var"]):
        for typ in flow:
            var = storage.variable
            if typ.lower() == "mem" or typ.lower() == "memory":
                var = storage.memory
            elif typ.lower() == "reg" or typ.lower() == "register":
                var = storage.register
            addr = var.load(addr)
        return addr

class AddressingMode:
    @staticmethod
    def direct(addr):
        # Directly returns the address
        return addr
