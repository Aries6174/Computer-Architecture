import storage
from addressing import Access, AddressingMode
from bin_convert import HalfPrecision, Length

# All requirements by sir:
# 1.) result should contain the two operands inputted by the user(must be array and triggered outside of the execute).
# 2.) calls execute where will determine what the opcode is.
# 3.) 1 for basic operations, 0 for jump operations
# 4.) In basic operations it should return the result immediately
# 5.) Jump Operations returns nothing, but it will pass whatever it will pass whatever
#       is the value in the 2nd operand to the PC using addressing.py and storage.
# 6.) Guess which addressing mode is necessary for this part.
# 

# Initialize the PC in the register storage
storage.register.store("PC", 0)  # Starting the program counter at 0

class Program:
    # Only Objective is Execute
    def execute(self, result, opcode):
        category = opcode[2:5]  # Extracting the last 3 bits of the opcode

        if opcode[1] == '1':
            catDecimal = "".join(category)  # Keep as a binary string
            # Use the binary string to determine the operation
            if catDecimal == "000":  # Modulo
                result["outcome"] = result["op"][0] % result["op"][1]
            elif catDecimal == "001":  # Addition
                result["outcome"] = result["op"][0] + result["op"][1]
            elif catDecimal == "010":  # Subtraction
                result["outcome"] = result["op"][0] - result["op"][1]
            elif catDecimal == "011":  # Multiplication
                result["outcome"] = result["op"][0] * result["op"][1]
            elif catDecimal == "100":  # Division
                try:
                    result["outcome"] = result["op"][0] / result["op"][1]
                except ZeroDivisionError as e:
                    return e
            else:
                result["outcome"] = "Unknown operation"
            return result["outcome"]

        # Operand 1 is compared to 0, and if true, Operand 2 is used as the address to jump to
        elif opcode[1] == '0':
            catDecimal = "".join(category)  # Keep as a binary string

            if catDecimal == "000" and result["op"][0] == 0:
                result["address"] = AddressingMode.direct(result["op"][1])
            elif catDecimal == "001" and result["op"][0] != 0:
                result["address"] = AddressingMode.direct(result["op"][1])
            elif catDecimal == "010" and result["op"][0] < 0:
                result["address"] = AddressingMode.direct(result["op"][1])
            elif catDecimal == "011" and result["op"][0] <= 0:
                result["address"] = AddressingMode.direct(result["op"][1])
            elif catDecimal == "100" and result["op"][0] > 0:
                result["address"] = AddressingMode.direct(result["op"][1])
            elif catDecimal == "101" and result["op"][0] >= 0:
                result["address"] = AddressingMode.direct(result["op"][1])
            elif catDecimal == "110":
                result["address"] = AddressingMode.direct(result["op"][1])
            else:
                result["address"] = "Condition not met"
            
            # Update the Program Counter (PC) with the new address if it's not a calculation result
            if isinstance(result["address"], int):
                storage.register.store("PC", result["address"])
            return result["address"]

        else:
            result["outcome"] = "The Opcode's Write bit is neither a 1 nor a 0."
            return result["outcome"]

if __name__ == "__main__":
    result = {"op": [0, 0], "address": 0}
    opcode = input("Enter Opcode: ")
    opcodeList = list(opcode)
    
    result["op"][0] = int(input("Enter Operand 1: "))
    result["op"][1] = int(input("Enter Operand 2: "))
    
    myProgram = Program()
    outcome = myProgram.execute(result, opcodeList)
    print(outcome)
