# Projeto Integrador - Passo 4
# Fila de Atendimento da Clínica Vida+
# Desenvolvido por João Gabriel da Silva Lucena

from collections import deque  # biblioteca ideal para filas

fila = deque()

def adicionar_paciente():
    nome = input("Nome do paciente: ")
    cpf = input("CPF: ")
    fila.append({"nome": nome, "cpf": cpf})
    print(f"✅ Paciente {nome} adicionado à fila.\n")

def atender_paciente():
    if len(fila) == 0:
        print("⚠ Nenhum paciente na fila.\n")
    else:
        paciente = fila.popleft()
        print(f"🩺 Paciente {paciente['nome']} (CPF: {paciente['cpf']}) foi atendido.\n")

def mostrar_fila():
    if len(fila) == 0:
        print("⚠ Nenhum paciente aguardando.\n")
    else:
        print("\n👥 Pacientes aguardando:")
        for i, paciente in enumerate(fila, start=1):
            print(f"{i}. {paciente['nome']} - CPF: {paciente['cpf']}")
        print()

def menu():
    while True:
        print("=== Fila de Atendimento - Clínica Vida+ ===")
        print("1 - Adicionar paciente à fila")
        print("2 - Atender paciente")
        print("3 - Mostrar fila")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        print()

        if opcao == "1":
            adicionar_paciente()
        elif opcao == "2":
            atender_paciente()
        elif opcao == "3":
            mostrar_fila()
        elif opcao == "4":
            print("👋 Encerrando o sistema de fila.")
            break
        else:
            print("❌ Opção inválida.\n")

menu()
