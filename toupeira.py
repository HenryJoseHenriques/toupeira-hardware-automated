import string

class Toupeira:

    def __init__(self):
        pass

    def rowInput(self, inputs, bitsIn, type):
        alfabeto_minusculo = string.ascii_lowercase
        rInputs = ""
        for letra in alfabeto_minusculo:
            if type == "STD_LOGIC_VECTOR":
                rInputs += f"i_{letra} : IN STD_LOGIC_VECTOR({bitsIn - 1} downto 0);\n"
                inputs -= 1
            if inputs == 0:
                break
        return rInputs

    def rowOutput(self, outputs, bitsOut, type):
        alfabeto_minusculo = string.ascii_lowercase
        rOutputs = ""
        for letra in alfabeto_minusculo:
            if type == "STD_LOGIC_VECTOR":
                rOutputs += f"o_{letra} : OUT STD_LOGIC_VECTOR({bitsOut - 1} downto 0);\n"
                outputs -= 1
            if outputs == 0:
                break
        return rOutputs

    def entityPart(self, name, inputs, outputs, bitsIn, bitsOut, type):
        entityVHDL = f"""
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

ENTITY {name} IS
    PORT(
        {self.rowInput(inputs, bitsIn, type)}
        {self.rowOutput(outputs, bitsOut, type)}
    );
END {name};
"""
        return entityVHDL

    def architecturePartOrGate(self, name):
        architectureVHDL = f"""
ARCHITECTURE behavioral_{name} OF {name} IS
BEGIN

END behavioral_{name};
"""
        return architectureVHDL

    def orGate(self, name, inputs, outputs, bitsIn, bitsOut, type):
        with open('or.vhd', 'w') as file:
            orGateCode = self.entityPart(name, inputs, outputs, bitsIn, bitsOut, type)
            file.write(orGateCode)
            architectureCode = self.architecturePartOrGate(name)
            file.write(architectureCode)
