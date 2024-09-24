import string

# name_inputs = []
# name_outputs = []

def rowInput(inputs=2, bitsIn=4, type_="STD_LOGIC_VECTOR",name_inputs = []):
    if inputs <= 0:
        return ""

    alfabeto_minusculo = string.ascii_lowercase
    linhas = []
    
    if type_ == "STD_LOGIC_VECTOR":
        for i, letra in enumerate(alfabeto_minusculo[:inputs]):
            nome_input = f"i_{letra.upper()}"
            linhas.append(f"{nome_input} : IN {type_}({bitsIn - 1} downto 0);")
            name_inputs.append(nome_input)
    
    elif type_ in ["STD_LOGIC", "BIT"]:
        for i, letra in enumerate(alfabeto_minusculo[:inputs]):
            nome_input = f"i_{letra.upper()}"
            linhas.append(f"{nome_input} : IN {type_};")
            name_inputs.append(nome_input)

    return "\n".join(linhas)


def rowOutput(outputs=1, bitsOut=5, type_="STD_LOGIC_VECTOR", name_outputs=[]):
    if outputs <= 0:
        return ""

    linhas = []

    if type_ == "STD_LOGIC_VECTOR":
        for i in range(outputs):
            nome_output = f"o_S{i}"
            if i == outputs - 1:  # Última linha sem ";"
                linhas.append(f"{nome_output} : OUT {type_}({bitsOut - 1} downto 0)")
            else:
                linhas.append(f"{nome_output} : OUT {type_}({bitsOut - 1} downto 0);")
            name_outputs.append(nome_output)
    
    elif type_ in ["STD_LOGIC", "BIT"]:
        for i in range(outputs):
            nome_output = f"o_S{i}"
            if i == outputs - 1:  # Última linha sem ";"
                linhas.append(f"{nome_output} : OUT {type_}")
            else:
                linhas.append(f"{nome_output} : OUT {type_};")
            name_outputs.append(nome_output)

    return "\n".join(linhas)
