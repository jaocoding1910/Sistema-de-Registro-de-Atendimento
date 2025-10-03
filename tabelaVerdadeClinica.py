# Tabela Verdade - Clínica Vida+
# Projeto Integrador Anhanguera
# Desenvolvido por João Gabriel da Silva Lucena

# Variáveis:
# A = Paciente tem agendamento marcado
# B = Documentos estão OK
# C = Médico disponível
# D = Pagamento em dia

print("Tabela Verdade - Sistema de Atendimento da Clínica Vida+")
print("A | B | C | D || Consulta Normal | Emergência")
print("-" * 48)

for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            for D in [False, True]:
                consulta_normal = (A and B and C) or (B and C and D)
                emergencia = C and (B or D)
                print(f"{int(A)} | {int(B)} | {int(C)} | {int(D)} || "
                      f"{int(consulta_normal)}               | {int(emergencia)}")