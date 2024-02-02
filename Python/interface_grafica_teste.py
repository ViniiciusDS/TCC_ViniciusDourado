# Teste de interface para o TCC
import tkinter as tk
from tkinter import filedialog
import os  # Para abrir o arquivo de matriz


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

        # Campos de Resultados Específicos
        self.label_media_fb = tk.Label(
            self.root, text="Média Execução Força Bruta:")
        # Colocar na primeira coluna
        self.label_media_fb.grid(row=10, column=1, sticky='w')

        self.resultado_media_fb = tk.Entry(self.root, state='readonly')
        # Colocar na primeira coluna
        self.resultado_media_fb.grid(row=11, column=1, sticky='w')

        self.label_media_ag = tk.Label(
            self.root, text="Média Execução Algoritmo Genético:")
        self.label_media_ag.grid(row=12, column=1, sticky='w')

        self.resultado_media_ag = tk.Entry(self.root, state='readonly')
        self.resultado_media_ag.grid(row=13, column=1, sticky='w')

        self.label_media_sa = tk.Label(
            self.root, text="Média Execução Simulated Annealing:")
        self.label_media_sa.grid(row=14, column=1, sticky='w')

        self.resultado_media_sa = tk.Entry(self.root, state='readonly')
        self.resultado_media_sa.grid(row=15, column=1, sticky='w')

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

        # Campos de Resultados
        # self.label_resultados = tk.Label(
        #    self.root, text="Resultados:", font=('Helvetica', 16, 'bold'))
        # self.label_resultados.grid(row=5, column=1, sticky='w', pady=10)

        # self.resultados_text = tk.Text(
        #    self.root, height=10, width=40, wrap=tk.WORD)
        # self.resultados_text.grid(row=6, column=1, columnspan=2, pady=10)

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
        # Certifique-se de adicionar as condições para as opções selecionadas

        # Obtendo os valores das opções
        matriz_file_path = self.matriz_file_path.get()  # Caminho do arquivo de matriz
        num_cidades = int(self.num_cidades.get())  # Número de cidades
        incrementar_cidades = str(
            self.incrementar_cidades.get())  # Aumentar cidades
        # Convertendo para string
        executar_forca_bruta = str(self.executar_forca_bruta.get())
        # Convertendo para string
        executar_alg_genetico = str(self.executar_alg_genetico.get())
        # Convertendo para string
        executar_simulated_annealing = str(
            self.executar_simulated_annealing.get())
        inicio_aumento = int(self.num_cidades_inicio.get()
                             ) if incrementar_cidades else 0
        fim_aumento = int(self.num_cidades_fim.get()
                          ) if incrementar_cidades else 0

        # Lógica para executar os métodos com base nas opções selecionadas
        # ...

        # Exemplo: Executar o programa principal (substitua pela lógica real)
        # O programa principal deve receber parâmetros conforme necessário
        command = (
            'python tcc.py '
            f'{matriz_file_path} '
            f'{num_cidades} '
            f'{incrementar_cidades} '
            f'{executar_forca_bruta} '
            f'{executar_alg_genetico} '
            f'{executar_simulated_annealing} '
            f'{inicio_aumento} '
            f'{fim_aumento} '
        )
        # os.system(command)
        # Capturar a saída do programa principal
        output = os.popen(command).read()

        # Exibir os resultados na interface
        self.resultados_text.delete(1.0, tk.END)  # Limpar o campo de texto
        self.resultados_text.insert(tk.END, output)
        # Exibir resultados específicos
        resultados_dict = obter_resultados(output)
        self.resultado_media_fb.config(state='normal')
        self.resultado_media_fb.delete(0, tk.END)
        self.resultado_media_fb.insert(0, str(resultados_dict['media_fb']))
        self.resultado_media_fb.config(state='readonly')

        self.resultado_media_ag.config(state='normal')
        self.resultado_media_ag.delete(0, tk.END)
        self.resultado_media_ag.insert(0, str(resultados_dict['media_ag']))
        self.resultado_media_ag.config(state='readonly')

        self.resultado_media_sa.config(state='normal')
        self.resultado_media_sa.delete(0, tk.END)
        self.resultado_media_sa.insert(0, str(resultados_dict['media_sa']))
        self.resultado_media_sa.config(state='readonly')


def obter_resultados(output):
    # Lógica para extrair resultados específicos do output
    # ...

    # Vamos supor que a saída contém linhas no formato "Média FB: 123.45"
    media_fb = None
    media_ag = None
    media_sa = None

    lines = output.split('\n')
    for line in lines:
        if line.startswith("Média FB:"):
            media_fb = float(line.split(":")[1].strip())
        elif line.startswith("Média AG:"):
            media_ag = float(line.split(":")[1].strip())
        elif line.startswith("Média SA:"):
            media_sa = float(line.split(":")[1].strip())

    return {'media_fb': media_fb, 'media_ag': media_ag, 'media_sa': media_sa}


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
