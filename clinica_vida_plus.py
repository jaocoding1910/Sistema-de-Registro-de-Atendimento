# ============================================================
# 🏥 Sistema de Cadastro de Pacientes - Clínica Vida+
# Versão GUI (Interface Visual com Tkinter)
# Desenvolvido por João Gabriel da Silva Lucena
# ============================================================

import csv
import os
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox, simpledialog

# -----------------------------#
# 📁 Estrutura de pastas
# -----------------------------#
DATA_DIR = "dados_clinica"
PACIENTES_CSV = os.path.join(DATA_DIR, "pacientes.csv")
ATENDIMENTOS_CSV = os.path.join(DATA_DIR, "atendimentos.csv")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# -----------------------------#
# 🧠 Dados em memória
# -----------------------------#
pacientes = []
atendimentos = []

# -----------------------------#
# 💾 Funções utilitárias
# -----------------------------#
def carregar_dados():
    pacientes.clear()
    atendimentos.clear()

    # Pacientes
    if os.path.exists(PACIENTES_CSV):
        with open(PACIENTES_CSV, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                pacientes.append(row)

    # Atendimentos
    if os.path.exists(ATENDIMENTOS_CSV):
        with open(ATENDIMENTOS_CSV, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                atendimentos.append(row)

def salvar_pacientes():
    with open(PACIENTES_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Nome", "Idade", "Telefone", "DataCadastro"])
        w.writeheader()
        w.writerows(pacientes)

def salvar_atendimentos():
    with open(ATENDIMENTOS_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["NomePaciente", "DataISO", "Profissional", "Observacoes", "Evolucao"])
        w.writeheader()
        w.writerows(atendimentos)

# -----------------------------#
# 👤 Funções principais
# -----------------------------#
def cadastrar_paciente():
    win = Toplevel(root)
    win.title("Cadastrar Paciente")
    win.geometry("400x300")

    Label(win, text="Nome:").pack()
    nome = Entry(win); nome.pack()

    Label(win, text="Idade:").pack()
    idade = Entry(win); idade.pack()

    Label(win, text="Telefone:").pack()
    telefone = Entry(win); telefone.pack()

    def salvar():
        nome_val = nome.get().strip()
        idade_val = idade.get().strip()
        telefone_val = telefone.get().strip()

        if not nome_val or not idade_val or not telefone_val:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
            return

        for p in pacientes:
            if p["Nome"].lower() == nome_val.lower():
                messagebox.showerror("Duplicado", "Paciente já cadastrado!")
                return

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        pacientes.append({"Nome": nome_val, "Idade": idade_val, "Telefone": telefone_val, "DataCadastro": data})
        salvar_pacientes()
        atualizar_lista_pacientes()
        messagebox.showinfo("Sucesso", f"Paciente {nome_val} cadastrado!")
        win.destroy()

    Button(win, text="Salvar", command=salvar).pack(pady=10)

def registrar_atendimento():
    if not pacientes:
        messagebox.showinfo("Aviso", "Nenhum paciente cadastrado ainda.")
        return

    win = Toplevel(root)
    win.title("Registrar Atendimento")
    win.geometry("500x400")

    Label(win, text="Nome do Paciente:").pack()
    nomes = [p["Nome"] for p in pacientes]
    paciente_cb = ttk.Combobox(win, values=nomes)
    paciente_cb.pack()

    Label(win, text="Profissional:").pack()
    prof = Entry(win); prof.pack()

    Label(win, text="Observações:").pack()
    obs = Text(win, height=3); obs.pack()

    Label(win, text="Evolução:").pack()
    evo = Text(win, height=3); evo.pack()

    def salvar():
        nome = paciente_cb.get().strip()
        if not nome:
            messagebox.showwarning("Erro", "Selecione um paciente.")
            return

        a = {
            "NomePaciente": nome,
            "DataISO": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Profissional": prof.get(),
            "Observacoes": obs.get("1.0", END).strip(),
            "Evolucao": evo.get("1.0", END).strip()
        }
        atendimentos.append(a)
        salvar_atendimentos()
        messagebox.showinfo("Sucesso", f"Atendimento de {nome} registrado.")
        win.destroy()

    Button(win, text="Salvar Atendimento", command=salvar).pack(pady=10)

def ver_historico():
    nome = simpledialog.askstring("Histórico", "Digite o nome do paciente:")
    if not nome:
        return

    hist = [a for a in atendimentos if a["NomePaciente"].lower() == nome.lower()]
    if not hist:
        messagebox.showinfo("Sem histórico", "Nenhum atendimento encontrado.")
        return

    win = Toplevel(root)
    win.title(f"Histórico de {nome}")
    win.geometry("600x400")

    txt = Text(win)
    txt.pack(expand=True, fill=BOTH)

    for a in hist:
        txt.insert(END, f"\nData: {a['DataISO']}")
        txt.insert(END, f"\nProfissional: {a['Profissional']}")
        txt.insert(END, f"\nObservações: {a['Observacoes']}")
        txt.insert(END, f"\nEvolução: {a['Evolucao']}")
        txt.insert(END, "\n" + "-" * 50)

def atualizar_lista_pacientes():
    for i in tree.get_children():
        tree.delete(i)
    for p in pacientes:
        tree.insert("", END, values=(p["Nome"], p["Idade"], p["Telefone"], p["DataCadastro"]))

# -----------------------------#
# 🪟 Interface principal
# -----------------------------#
root = Tk()
root.title("🏥 Clínica Vida+ - Sistema de Cadastro e Atendimento")
root.geometry("750x500")

# Título
Label(root, text="🏥 Clínica Vida+ - Sistema de Gestão", font=("Arial", 16, "bold")).pack(pady=10)

# Botões principais
frame_btn = Frame(root)
frame_btn.pack(pady=10)

Button(frame_btn, text="➕ Cadastrar Paciente", command=cadastrar_paciente, width=22).grid(row=0, column=0, padx=5)
Button(frame_btn, text="📋 Registrar Atendimento", command=registrar_atendimento, width=22).grid(row=0, column=1, padx=5)
Button(frame_btn, text="📚 Ver Histórico", command=ver_historico, width=22).grid(row=0, column=2, padx=5)

# Lista de pacientes
Label(root, text="📋 Pacientes Cadastrados", font=("Arial", 12, "bold")).pack()

tree = ttk.Treeview(root, columns=("Nome", "Idade", "Telefone", "DataCadastro"), show="headings")
for col in ("Nome", "Idade", "Telefone", "DataCadastro"):
    tree.heading(col, text=col)
tree.pack(expand=True, fill=BOTH, pady=10)

# Carrega dados iniciais
carregar_dados()
atualizar_lista_pacientes()

root.mainloop()
