import component as cp

def createGate(name, operation, inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    # Validação de parâmetros
    if inputs < 2 and operation != "NOT":
        raise ValueError(f"O número de entradas para {name} deve ser no mínimo 2.")
    
    if bitsIn != bitsOut:
        bitsIn = bitsOut
    
    # Gerar entidade
    entity, name_input, name_output = cp.interfaceEntity(name, inputs, outputs, bitsIn, bitsOut, type)

    # Implementação da lógica
    implemented = ""
    if operation == "NOT":
        implemented += f"{name_output[0]} <= NOT({name_input[0]});\n"
    else:
        for i in range(inputs - 1):
            implemented += f"{name_output[0]} <= {name_input[i]} {operation} {name_input[i+1]};\n"

    # Arquitetura final
    architecture = cp.aplicationArchitecture(implementation=implemented)
    return entity + architecture

# Funções específicas reutilizando a função base
def andGate(name="andGate", inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "AND", inputs, outputs, bitsIn, bitsOut, type)

def orGate(name="orGate", inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "OR", inputs, outputs, bitsIn, bitsOut, type)

def norGate(name="norGate", inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "NOR", inputs, outputs, bitsIn, bitsOut, type)

def nandGate(name="nandGate", inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "NAND", inputs, outputs, bitsIn, bitsOut, type)

def xorGate(name="xorGate", inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "XOR", inputs, outputs, bitsIn, bitsOut, type)

def xnorGate(name="xnorGate", inputs=2, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "XNOR", inputs, outputs, bitsIn, bitsOut, type)

def notGate(name="notGate", inputs=1, outputs=1, bitsIn=4, bitsOut=4, type="STD_LOGIC_VECTOR"):
    return createGate(name, "NOT", inputs, outputs, bitsIn, bitsOut, type)
