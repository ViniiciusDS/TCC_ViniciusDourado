# Teste de interface para o TCC
import tkinter as tk
from tkinter import filedialog
# import os  # Para abrir o arquivo de matriz
import time  # Import the 'time' module
from tcc import calcute_metodos_param  # Import tcc.py
import numpy as np  # Import the 'numpy' module


class PlaceholderEntry(tk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = 'grey'
        self.default_fg_color = self['foreground']

        self.bind('<FocusIn>', self._clear_placeholder)
        self.bind('<FocusOut>', self._set_placeholder)

        self._set_placeholder()

    def _clear_placeholder(self, event):
        if self['foreground'] == self.placeholder_color:
            self.delete(0, 'end')
            self['foreground'] = self.default_fg_color

    def _set_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['foreground'] = self.placeholder_color


class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("TCC Program")

        # Variáveis de Controle
        self.num_cidades = tk.StringVar()
        self.matriz_file_path = tk.StringVar()
        self.incrementar_cidades = tk.BooleanVar(value=False)
        self.executar_forca_bruta = tk.BooleanVar(value=True)
        self.executar_alg_genetico = tk.BooleanVar(value=True)
        self.executar_simulated_annealing = tk.BooleanVar(value=True)
        self.num_cidades_inicio = tk.StringVar()
        self.num_cidades_fim = tk.StringVar()
        self.tam_pop_ini_ag = tk.StringVar()
        self.tam_gera_ag = tk.StringVar()
        self.tx_mutacao_ag = tk.StringVar()
        self.num_int_sa = tk.StringVar()
        self.temp_ini_sa = tk.StringVar()
        self.taxa_resfriamento_sa = tk.StringVar()
        self.nmr_de_simulacoes = tk.StringVar()

        # Resultados
        self.resultados_text = tk.Text(self.root, height=10, width=62)
        self.resultados_text.grid(row=2, column=1, rowspan=8, columnspan=3)

        # Aba tempo de execução
        self.label_tempo = tk.Label(self.root, text="Tempo de Execução:")
        self.label_tempo.grid(row=18, column=1)

        # Aba Menor Rota e km Força Bruta
        self.label_menor_rota_fb = tk.Label(
            self.root, text="Menor Rota Força Bruta:")
        self.label_menor_rota_fb.grid(row=5, column=4)

        self.label_menor_rota_fb_texto = tk.Label(
            self.root, text="Menor Rota Força Bruta:")
        self.label_menor_rota_fb_texto.grid(row=3, column=5)

        # Aba Menor Rota e km Algoritmo Genético
        self.label_menor_rota_ag = tk.Label(
            self.root, text="Menor Rota Algoritmo Genético:")
        self.label_menor_rota_ag.grid(row=8, column=4)

        self.label_menor_rota_ag_texto = tk.Label(
            self.root, text="Menor Rota Algoritmo Genético:")
        self.label_menor_rota_ag_texto.grid(row=3, column=6)

        # Aba Menor Rota e km Simulated Annealing
        self.label_menor_rota_sa = tk.Label(
            self.root, text="Menor Rota Simulated Annealing:")
        self.label_menor_rota_sa.grid(row=11, column=4)

        self.label_menor_rota_sa_texto = tk.Label(
            self.root, text="Menor Rota Simulated Annealing:")
        self.label_menor_rota_sa_texto.grid(row=3, column=7)

        # Adiciona uma variável de controle para a menor rota e km da força bruta
        self.menor_rota_fb = tk.StringVar()
        self.menor_rota_fb.set("[0]")
        self.km_fb = tk.StringVar()
        self.km_fb.set("0")
        self.menor_rota_fb_texto = tk.StringVar()
        self.menor_rota_fb_texto.set("[0]")

        # Adiciona uma variável de controle para a menor rota e km do algoritmo genético
        self.menor_rota_ag = tk.StringVar()
        self.menor_rota_ag.set("[0]")
        self.km_ag = tk.StringVar()
        self.km_ag.set("0")
        self.menor_rota_ag_texto = tk.StringVar()
        self.menor_rota_ag_texto.set("[0]")

        # Adiciona uma variável de controle para a menor rota e km do simulated annealing
        self.menor_rota_sa = tk.StringVar()
        self.menor_rota_sa.set("[0]")
        self.km_sa = tk.StringVar()
        self.km_sa.set("0")
        self.menor_rota_sa_texto = tk.StringVar()
        self.menor_rota_sa_texto.set("[0]")

        # Adicionando uma variável de controle para o tempo de execução
        self.tempo_execucao = tk.StringVar()
        self.tempo_execucao.set("0 segundos")

        # Exibição dinâmica do tempo de execução
        self.label_tempo_real = tk.Label(
            self.root, textvariable=self.tempo_execucao)
        self.label_tempo_real.grid(row=18, column=2)

        # Exibição dinâmica da menor rota e km da força bruta
        self.label_menor_rota_fb_real = tk.Label(
            self.root, textvariable=self.menor_rota_fb)
        self.label_menor_rota_fb_real.grid(row=6, column=4)
        self.label_km_fb_real = tk.Label(
            self.root, textvariable=self.km_fb)
        self.label_km_fb_real.grid(row=7, column=4)
        self.label_menor_rota_fb_texto_real = tk.Label(
            self.root, textvariable=self.menor_rota_fb_texto)
        self.label_menor_rota_fb_texto_real.grid(
            row=5, column=5, rowspan=10, columnspan=1)

        # Exibição dinâmica da menor rota e km do algoritmo genético
        self.label_menor_rota_ag_real = tk.Label(
            self.root, textvariable=self.menor_rota_ag)
        self.label_menor_rota_ag_real.grid(row=9, column=4)
        self.label_km_ag_real = tk.Label(
            self.root, textvariable=self.km_ag)
        self.label_km_ag_real.grid(row=10, column=4)
        self.label_menor_rota_ag_texto_real = tk.Label(
            self.root, textvariable=self.menor_rota_ag_texto)
        self.label_menor_rota_ag_texto_real.grid(
            row=5, column=6, rowspan=10, columnspan=1)

        # Exibição dinâmica da menor rota e km do simulated annealing
        self.label_menor_rota_sa_real = tk.Label(
            self.root, textvariable=self.menor_rota_sa)
        self.label_menor_rota_sa_real.grid(row=12, column=4)
        self.label_km_sa_real = tk.Label(
            self.root, textvariable=self.km_sa)
        self.label_km_sa_real.grid(row=13, column=4)
        self.label_menor_rota_sa_texto_real = tk.Label(
            self.root, textvariable=self.menor_rota_sa_texto)
        self.label_menor_rota_sa_texto_real.grid(
            row=5, column=7, rowspan=10, columnspan=1)

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

        # Numero de Simulações
        label_simulacoes = tk.Label(self.root, text="Número de Simulações:")
        label_simulacoes.grid(row=10, column=0)

        entry_simulacoes = tk.Entry(
            self.root, textvariable=self.nmr_de_simulacoes)
        entry_simulacoes.grid(row=11, column=0)

        button_browse = tk.Button(
            self.root, text="Procurar", command=self.browse_file)
        button_browse.grid(row=7, column=0)

        # Opções de Aumentar progressivamente o número de Cidades
        label_aumentar_cidades = tk.Label(
            self.root, text="Aumentar o número de cidades:")
        label_aumentar_cidades.grid(row=8, column=0)

        checkbox_aumentar_cidades = tk.Checkbutton(
            self.root, text="Sim", variable=self.incrementar_cidades)
        checkbox_aumentar_cidades.grid(row=9, column=0)

        # Caso o usuário queira aumentar o número de cidades
        label_incrementar_cidades_ref = tk.Label(
            self.root, text="Opções para variar o Número de cidades:")
        label_incrementar_cidades_ref.grid(row=11, column=1)
        # Início
        label_num_cidades_inicio = tk.Label(self.root, text="Número Inicial:")
        label_num_cidades_inicio.grid(row=12, column=1)

        entry_inicio = PlaceholderEntry(
            self.root, "Exemplo: 5", textvariable=self.num_cidades_inicio)
        entry_inicio.grid(row=13, column=1)

        # Fim
        label_num_cidades_fim = tk.Label(self.root, text="Número Final:")
        label_num_cidades_fim.grid(row=14, column=1)

        entry_fim = PlaceholderEntry(
            self.root, "Exemplo: 10", textvariable=self.num_cidades_fim)
        entry_fim.grid(row=15, column=1)

        # Opções do Algoritmo Genético
        label_alg_genetico_ref = tk.Label(
            self.root, text="Opções do Algoritmo Genético:")
        label_alg_genetico_ref.grid(row=11, column=2)

        # Tamanho da População Inicial
        label_tam_pop_ini_ag = tk.Label(
            self.root, text="Tamanho da População Inicial:")
        label_tam_pop_ini_ag.grid(row=12, column=2)

        entry_tam_pop_ini_ag = PlaceholderEntry(
            self.root, "Exemplo: 10", textvariable=self.tam_pop_ini_ag)
        entry_tam_pop_ini_ag.grid(row=13, column=2)

        # Tamanho da Geração
        label_tam_gera_ag = tk.Label(
            self.root, text="Tamanho da Geração:")
        label_tam_gera_ag.grid(row=14, column=2)

        entry_tam_gera_ag = PlaceholderEntry(
            self.root, "Exemplo: 100", textvariable=self.tam_gera_ag)
        entry_tam_gera_ag.grid(row=15, column=2)

        # Taxa de Mutação
        label_tx_mutacao_ag = tk.Label(
            self.root, text="Taxa de Mutação:")
        label_tx_mutacao_ag.grid(row=16, column=2)

        entry_tx_mutacao_ag = PlaceholderEntry(
            self.root, "Exemplo: 0.1", textvariable=self.tx_mutacao_ag)
        entry_tx_mutacao_ag.grid(row=17, column=2)

        # Opções do Simulated Annealing
        label_simulated_annealing_ref = tk.Label(
            self.root, text="Opções do Simulated Annealing:")
        label_simulated_annealing_ref.grid(row=11, column=3)

        # Número de Interações
        label_num_int_sa = tk.Label(
            self.root, text="Número de Interações:")
        label_num_int_sa.grid(row=12, column=3)

        entry_num_int_sa = PlaceholderEntry(
            self.root, "Exemplo: 100", textvariable=self.num_int_sa)
        entry_num_int_sa.grid(row=13, column=3)

        # Temperatura Inicial
        label_temp_ini_sa = tk.Label(
            self.root, text="Temperatura Inicial:")
        label_temp_ini_sa.grid(row=14, column=3)

        entry_temp_ini_sa = PlaceholderEntry(
            self.root, "Exemplo: 0.7", textvariable=self.temp_ini_sa)
        entry_temp_ini_sa.grid(row=15, column=3)

        # Taxa de Resfriamento
        label_taxa_resfriamento_sa = tk.Label(
            self.root, text="Taxa de Resfriamento:")
        label_taxa_resfriamento_sa.grid(row=16, column=3)

        entry_taxa_resfriamento_sa = PlaceholderEntry(
            self.root, "Exemplo: 0.95", textvariable=self.taxa_resfriamento_sa)
        entry_taxa_resfriamento_sa.grid(row=17, column=3)

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
        incrementar_cidades = self.incrementar_cidades.get()  # Aumentar cidades
        nmr_de_simulacoes = int(self.nmr_de_simulacoes.get()
                                )  # Número de simulações

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

        if self.executar_alg_genetico.get():
            tam_pop_ini_ag = int(self.tam_pop_ini_ag.get()
                                 )
            tam_gera_ag = int(self.tam_gera_ag.get()
                              )
            tx_mutacao_ag = float(self.tx_mutacao_ag.get()
                                  )

        else:
            tam_pop_ini_ag = "0"
            tam_gera_ag = "0"
            tx_mutacao_ag = "0"

        if self.executar_simulated_annealing.get():
            num_int_sa = int(self.num_int_sa.get()
                             )
            temp_ini_sa = float(self.temp_ini_sa.get()
                                )
            taxa_resfriamento_sa = float(self.taxa_resfriamento_sa.get()
                                         )
        else:
            num_int_sa = "0"
            temp_ini_sa = "0"
            taxa_resfriamento_sa = "0"

        # Reiniciando o timer
        start_time = time.time()

        # Convertendo para string
        executar_forca_bruta = self.executar_forca_bruta.get()
        # Convertendo para string
        executar_alg_genetico = self.executar_alg_genetico.get()
        # Convertendo para string
        executar_simulated_annealing = self.executar_simulated_annealing.get()

        # O programa principal deve receber parâmetros conforme necessário

        # Capturar a saída do programa principal
        resultados_tcc = calcute_metodos_param(matriz_file_path, incrementar_cidades, num_cidades,
                                               executar_forca_bruta, executar_alg_genetico,
                                               executar_simulated_annealing, inicio_aumento,
                                               fim_aumento, tam_pop_ini_ag, tam_gera_ag, num_int_sa,
                                               temp_ini_sa, taxa_resfriamento_sa, tx_mutacao_ag,
                                               nmr_de_simulacoes)

        # Parando o timer e calculando o tempo total de execução
        elapsed_time = time.time() - start_time

        # Exibir os resultados na interface
        for metodo, dados in resultados_tcc.items():
            self.resultados_text.insert(
                tk.END, f"{metodo}:\n")
            self.resultados_text.insert(
                tk.END, f"Média do Tempo: {dados['media_tempo']} segundos\n")
            self.resultados_text.insert(
                tk.END, f"Desvio Padrão do Tempo: {dados['desvio_padrao_tempo']} segundos\n\n")

        # Atualizando a menor rota da força bruta
        atualizar_rotas(self, resultados_tcc)
        atualizar_nomes_cidades(self, resultados_tcc, matriz_file_path)

        # Atualizando o timer de tempo de execução
        self.tempo_execucao.set(f"{elapsed_time:.2f} segundos")

    def mostrar_graficos(self):
        # Lógica para mostrar os gráficos usando matplotlib
        return 0


def atualizar_rotas(self, resultados):
    # Lógica para atualizar as rotas na interface
    self.menor_rota_fb.set(
        f"{resultados['Força Bruta']['Menor Rota']}")
    self.km_fb.set(
        f"{resultados['Força Bruta']['Menor Distância']} km")

    self.menor_rota_ag.set(
        f"{resultados['Algoritmo Genético']['Menor Rota']}")
    self.km_ag.set(
        f"{resultados['Algoritmo Genético']['Menor Distância']} km")

    self.menor_rota_sa.set(
        f"{resultados['Simulated Annealing']['Menor Rota']}")
    self.km_sa.set(
        f"{resultados['Simulated Annealing']['Menor Distância']} km")

    return 0


def atualizar_nomes_cidades(self, resultados, matriz_file_path):
    # Lógica para atualizar os nomes das cidades na interface
    matriz = np.genfromtxt(matriz_file_path, delimiter='\t', dtype=str)

    # Obtendo os nomes das cidades da última coluna da matriz
    nomes_cidades = matriz[:, -1]

    # Criando a numeração das cidades
    numeracao_cidades = [str(i) + " - " + nome for i,
                         nome in enumerate(nomes_cidades)]

    # Atualizando os nomes das cidades na interface para a melhor rota da força bruta
    if self.executar_forca_bruta.get() and resultados['Força Bruta'] is not None:
        melhor_rota_fb = [int(idx)
                          for idx in resultados['Força Bruta']['Menor Rota']]
        nomes_cidades_fb = [numeracao_cidades[i] for i in melhor_rota_fb]
        self.menor_rota_fb_texto.set("\n".join(nomes_cidades_fb))
    else:
        self.menor_rota_fb_texto.set("")   # Limpar a menor rota da força bruta

    # Atualizando os nomes das cidades na interface para a melhor rota do algoritmo genético
    if self.executar_alg_genetico.get() and resultados['Algoritmo Genético'] is not None:
        melhor_rota_ag = [
            int(idx) for idx in resultados['Algoritmo Genético']['Menor Rota']]
        nomes_cidades_ag = [numeracao_cidades[i] for i in melhor_rota_ag]
        self.menor_rota_ag_texto.set("\n".join(nomes_cidades_ag))
    else:
        # Limpar a menor rota do algoritmo genético
        self.menor_rota_ag_texto.set("")

    # Atualizando os nomes das cidades na interface para a melhor rota do simulated annealing
    if self.executar_simulated_annealing.get() and resultados['Simulated Annealing'] is not None:
        melhor_rota_sa = [
            int(idx) for idx in resultados['Simulated Annealing']['Menor Rota']]
        nomes_cidades_sa = [numeracao_cidades[i] for i in melhor_rota_sa]
        self.menor_rota_sa_texto.set("\n".join(nomes_cidades_sa))
    else:
        # Limpar a menor rota do simulated annealing
        self.menor_rota_sa_texto.set("")

    return 0


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
