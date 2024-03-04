@echo off

rem Detecta o diretório atual do script .bat
set "script_dir=%~dp0"

rem Caminho para o ambiente virtual
set "venv_dir=%script_dir%TCC_viniciusD"

rem Ativa o ambiente virtual
call "%venv_dir%\Scripts\activate"

rem Executa o script da interface gráfica
python "%script_dir%interface_grafica_teste.py"

rem Desativa o ambiente virtual
deactivate
