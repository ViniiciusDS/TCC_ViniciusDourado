
### Teste de interface para o TCC   ###
from tkinter import *


janela = Tk()

janela.title("TCC Program")

texto_orientacao = Label(janela, text="Escolha o arquivo com as matrizes:")

texto_orientacao.grid(row=0, column=0, sticky="w")

texto_orientacao2 = Label(janela, text="Número de Cidades:")

janela.mainloop()
