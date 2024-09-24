#https://wp.cbpf.br/escola-2023/wp-content/uploads/wpcfto_files/af2f7440836735403c222853d8bbbf99EscolaCBPF-2021_Parte-3_VHDL.pdf

import booleanGates as bg

name = "OrTest"

Orgate4Bits = bg.orGate(name, 2, 1, 4, 5, "STD_LOGIC_VECTOR")

with open(f"{name}.vhd","w") as file:
    file.write(Orgate4Bits)
