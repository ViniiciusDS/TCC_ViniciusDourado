import tkinter as tk
from tkinter import filedialog
import os
import subprocess


class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("TCC Program")

        # Variáveis de controle
        self.matriz_file_path = tk.StringVar()
        self.num_cidades = tk.IntVar()
        self.executar_forca_bruta = tk.BooleanVar(value=True)
        self.executar_alg_genetico = tk.BooleanVar(value=True)
        self.executar_simulated_annealing = tk.BooleanVar(value=True)

        # Componentes da interface
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        # Opção para escolher arquivo de matriz
        label_matriz = tk.Label(
            main_frame, text="Escolha o arquivo de matriz:")
        label_matriz.grid(row=0, column=0, sticky="w")

        entry_matriz = tk.Entry(
            main_frame, textvariable=self.matriz_file_path, width=30)
        entry_matriz.grid(row=0, column=1, sticky="w")

        button_browse = tk.Button(
            main_frame, text="Procurar", command=self.browse_file)
        button_browse.grid(row=0, column=2)

        # Número de cidades
        label_cidades = tk.Label(main_frame, text="Número de Cidades:")
        label_cidades.grid(row=1, column=0, sticky="w")

        entry_cidades = tk.Entry(main_frame, textvariable=self.num_cidades)
        entry_cidades.grid(row=1, column=1, sticky="w")

        # Métodos a serem executados
        label_metodos = tk.Label(
            main_frame, text="Métodos a serem executados:")
        label_metodos.grid(row=2, column=0, sticky="w")

        checkbox_forca_bruta = tk.Checkbutton(
            main_frame, text="Força Bruta", variable=self.executar_forca_bruta)
        checkbox_forca_bruta.grid(row=2, column=1, sticky="w")

        checkbox_alg_genetico = tk.Checkbutton(
            main_frame, text="Algoritmo Genético", variable=self.executar_alg_genetico)
        checkbox_alg_genetico.grid(row=2, column=2, sticky="w")

        checkbox_simulated_annealing = tk.Checkbutton(
            main_frame, text="Simulated Annealing", variable=self.executar_simulated_annealing)
        checkbox_simulated_annealing.grid(row=2, column=3, sticky="w")

        # Botão para executar
        button_executar = tk.Button(
            main_frame, text="Executar", command=self.executar_codigo)
        button_executar.grid(row=3, column=0, columnspan=4, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de Texto", "*.txt")])
        self.matriz_file_path.set(file_path)

    def executar_codigo(self):
        # Lógica para executar os códigos com base nas opções selecionadas
        # ...
        # Exemplo: Chamada do arquivo principal
        command = f"python tcc.py {self.matriz_file_path.get()} {self.num_cidades.get()} " \
                  f"{int(self.executar_forca_bruta.get())} {int(self.executar_alg_genetico.get())} " \
                  f"{int(self.executar_simulated_annealing.get())}"
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
