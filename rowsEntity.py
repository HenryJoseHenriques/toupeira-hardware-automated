import string

import string

def rowInput(inputs = 2, bitsIn = 4, type_ = "STD_LOGIC_VECTOR"):
    if inputs <= 0:
        return ""

    alfabeto_minusculo = string.ascii_lowercase
    linhas = []
    
    if type_ == "STD_LOGIC_VECTOR":
        for i, letra in enumerate(alfabeto_minusculo[:inputs]):
            linhas.append(f"i_{letra} : IN {type_}({bitsIn - 1} downto 0);")
    
    elif type_ in ["STD_LOGIC", "BIT"]:
        for i, letra in enumerate(alfabeto_minusculo[:inputs]):
            linhas.append(f"i_{letra} : IN {type_};")

    return "\n".join(linhas)


def rowOutput(outputs = 1, bitsOut = 5, type_ = "STD_LOGIC_VECTOR"):
    if outputs <= 0:
        return ""
    
    alfabeto_minusculo = string.ascii_lowercase
    linhas = []

    if type_ == "STD_LOGIC_VECTOR":
        for i, letra in enumerate(alfabeto_minusculo[:outputs]):
            linhas.append(f"o_{letra} : OUT {type_}({bitsOut - 1} downto 0);")
        
    elif type_ in ["STD_LOGIC", "BIT"]:
        for i, letra in enumerate(alfabeto_minusculo[:outputs]):
            linhas.append(f"o_{letra} : OUT {type_};")
    
    return "\n".join(linhas)