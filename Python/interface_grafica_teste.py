# Teste de interface para o TCC
import tkinter as tk
from tkinter import filedialog
import os  # Para abrir o arquivo de matriz
import time  # Import the 'time' module


class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("TCC Program")

        # Variáveis de Controle
        self.num_cidades = tk.StringVar()
        self.matriz_file_path = tk.StringVar()
        self.incrementar_cidades = tk.BooleanVar(value=True)
        self.executar_forca_bruta = tk.BooleanVar(value=True)
        self.executar_alg_genetico = tk.BooleanVar(value=True)
        self.executar_simulated_annealing = tk.BooleanVar(value=True)
        self.num_cidades_inicio = tk.StringVar()
        self.num_cidades_fim = tk.StringVar()

        # Resultados
        self.resultados_text = tk.Text(self.root, height=10, width=62)
        self.resultados_text.grid(row=2, column=1, rowspan=8)

        # Aba tempo de execução
        self.label_tempo = tk.Label(self.root, text="Tempo de Execução:")
        self.label_tempo.grid(row=18, column=1)

        # Adicionando uma variável de controle para o tempo de execução
        self.tempo_execucao = tk.StringVar()
        self.tempo_execucao.set("0 segundos")

        # Exibição dinâmica do tempo de execução
        self.label_tempo_real = tk.Label(
            self.root, textvariable=self.tempo_execucao)
        self.label_tempo_real.grid(row=18, column=2)

        # Componentes da Interface
        self.create_widgets()

    def create_widgets(self):
        # Número de Cidades
        label_cidades = tk.Label(self.root, text="Número de Cidades:")
        label_cidades.grid(row=3, column=0)  # Colocar na primeira coluna

        entry_cidades = tk.Entry(self.root, textvariable=self.num_cidades)
        entry_cidades.grid(row=4, column=0)

        # Arquivo de Matriz
        label_matriz = tk.Label(self.root, text="Arquivo de Matriz:")
        label_matriz.grid(row=5, column=0)

        entry_matriz = tk.Entry(self.root, textvariable=self.matriz_file_path)
        entry_matriz.grid(row=6, column=0)

        button_browse = tk.Button(
            self.root, text="Procurar", command=self.browse_file)
        button_browse.grid(row=7, column=0)

        # Opções de Aumentar Cidades
        label_aumentar_cidades = tk.Label(
            self.root, text="Aumentar o número de cidades:")
        label_aumentar_cidades.grid(row=8, column=0)

        checkbox_aumentar_cidades = tk.Checkbutton(
            self.root, text="Sim", variable=self.incrementar_cidades)
        checkbox_aumentar_cidades.grid(row=9, column=0)

        # Caso o usuário queira aumentar o número de cidades
        # Início
        label_num_cidades_inicio = tk.Label(self.root, text="Número Inicial:")
        label_num_cidades_inicio.grid(row=10, column=0)

        entry_inicio = tk.Entry(
            self.root, textvariable=self.num_cidades_inicio)
        entry_inicio.grid(row=11, column=0)

        # Fim
        label_num_cidades_fim = tk.Label(self.root, text="Número Final:")
        label_num_cidades_fim.grid(row=12, column=0)

        entry_fim = tk.Entry(self.root, textvariable=self.num_cidades_fim)
        entry_fim.grid(row=13, column=0)

        # Opções de Métodos
        label_metodos = tk.Label(self.root, text="Métodos a serem executados:")
        label_metodos.grid(row=14, column=0)

        checkbox_forca_bruta = tk.Checkbutton(
            self.root, text="Força Bruta", variable=self.executar_forca_bruta)
        checkbox_forca_bruta.grid(row=15, column=0)

        checkbox_alg_genetico = tk.Checkbutton(
            self.root, text="Algoritmo Genético", variable=self.executar_alg_genetico)
        checkbox_alg_genetico.grid(row=16, column=0)

        checkbox_simulated_annealing = tk.Checkbutton(
            self.root, text="Simulated Annealing", variable=self.executar_simulated_annealing)
        checkbox_simulated_annealing.grid(row=17, column=0)

        # Botão Executar
        button_executar = tk.Button(
            self.root, text="Executar", command=self.executar_codigo)
        button_executar.grid(row=18, column=0)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de Texto", "*.txt")])
        self.matriz_file_path.set(file_path)

    def executar_codigo(self):
        # Lógica para executar os códigos com base nas opções selecionadas

        # Tratamento de erro para o arquivo de matriz
        if not self.matriz_file_path.get():
            tk.messagebox.showerror("Erro", "Selecione um arquivo de matriz.")
            return

        # Obtendo os valores das opções
        matriz_file_path = self.matriz_file_path.get()  # Caminho do arquivo de matriz
        incrementar_cidades = str(
            self.incrementar_cidades.get())  # Aumentar cidades

        if self.incrementar_cidades.get():
            num_cidades = "0"
            inicio_aumento = int(self.num_cidades_inicio.get()
                                 )
            fim_aumento = int(self.num_cidades_fim.get()
                              )
        else:
            inicio_aumento = "0"
            fim_aumento = "0"
            num_cidades = int(self.num_cidades.get())  # Número de cidades

        # Reiniciando o timer
        start_time = time.time()

        # Convertendo para string
        executar_forca_bruta = str(self.executar_forca_bruta.get())
        # Convertendo para string
        executar_alg_genetico = str(self.executar_alg_genetico.get())
        # Convertendo para string
        executar_simulated_annealing = str(
            self.executar_simulated_annealing.get())

        # O programa principal deve receber parâmetros conforme necessário
        command = (
            'python tcc.py '
            f'{matriz_file_path} '
            f'{incrementar_cidades} '
            f'{num_cidades} '
            f'{executar_forca_bruta} '
            f'{executar_alg_genetico} '
            f'{executar_simulated_annealing} '
            f'{inicio_aumento} '
            f'{fim_aumento} '
        )
        # Capturar a saída do programa principal
        output = os.popen(command).read()

        # Parando o timer e calculando o tempo total de execução
        elapsed_time = time.time() - start_time

        # Exibir os resultados na interface
        self.resultados_text.delete(1.0, tk.END)  # Limpar o campo de texto
        self.resultados_text.insert(tk.END, output)

        # Atualizando o timer de tempo de execução
        self.tempo_execucao.set(f"{elapsed_time:.2f} segundos")

    def mostrar_graficos(self):
        # Lógica para mostrar os gráficos usando matplotlib
        return 0


def obter_resultados(output):
    # Lógica para extrair resultados específicos do output

    return 0


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
