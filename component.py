import rowsEntity as re


def interfaceEntity(name = "AndGate", inputs = 2, outputs = 1, bitsIn = 4, bitsOut = 5, type = "STD_LOGIC_VECTOR"):
    entityVHDL = f"""
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

ENTITY {name} IS
    PORT(
        {re.rowInput(inputs, bitsIn, type)}
        {re.rowOutput(outputs, bitsOut, type)}
    );
END {name};
"""
    return entityVHDL

def aplicationArchitecture(name="AndGate", signal="", constant="", types_="", components="", attribute="", implementation=""):
    ArchitectureVHDL = f"""
ARCHITECTURE behavioral_{name} OF {name} IS
"""

    parts = [signal, constant, types_, components, attribute]

    for part in parts:
        if part:
            ArchitectureVHDL += f"{part}\n"

    ArchitectureVHDL += f"""
BEGIN
    {implementation}
END behavioral_{name};
"""
    return ArchitectureVHDL
