@echo off
REM Ativar o ambiente virtual
call "C:\Users\viniv\Desktop\engenhariaeletrica\TCC_ViniciusDourado\Python\TCC_viniciusD\Scripts\activate.bat"

REM Executar o script da interface gráfica
python "C:\Users\viniv\Desktop\engenhariaeletrica\TCC_ViniciusDourado\Python\interface_grafica_teste.py"

REM Desativar o ambiente virtual
deactivate
