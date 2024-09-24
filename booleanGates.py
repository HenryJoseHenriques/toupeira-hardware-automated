import rowsEntity as re
import component as cp

def orGate(name, inputs, outputs, bitsIn, bitsOut, type):
    name_input = []
    name_outputs = []

    entity, name_input, name_outputs = cp.interfaceEntity(name, inputs, outputs, bitsIn, bitsOut, type)

    implementedOr = ""
    
    # Verificar se inputs tem ao menos 2 entradas para fazer a operação OR corretamente
    if inputs >= 2:
        # Realizar operação OR entre as entradas
        for i in range(inputs - 1):  # loop até inputs - 1 para evitar acessar índice fora dos limites
            implementedOr += f"""{name_outputs[i]} <= {name_input[i]} OR {name_input[i+1]};\n"""
    else:
        raise ValueError("O número de entradas deve ser no mínimo 2 para realizar a operação OR.")

    Architecture = cp.aplicationArchitecture(implementation=implementedOr)
    return entity+Architecture

# Testar a função orGate
#orGate("OrTest", 2, 1, 4, 5, "STD_LOGIC_VECTOR")
