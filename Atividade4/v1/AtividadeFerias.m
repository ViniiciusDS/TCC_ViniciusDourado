%clc 
clear all
tic_total = tic;

% Dados Cidades N = 15
% 1 - UEL,Londrina                          | 26 - Foz do Iguacu, PR       
% 2 - Ibipora, PR                           | 27 - Borrazopolis, PR
% 3 - Maringa, PR                           | 28 - Guapirama, PR
% 4 - Cascavel, PR                          | 29 - Inaja, PR
% 5 - Paranagua, PR                         | 30 - Nova Fatima, PR
% 6 - Perola, PR                            | 31 - Lobato, PR
% 7 - Palmas, PR                            | 32 - Araruna, PR
% 8 - Brasilandia do Sul, PR                | 33 - Jesuitas, PR
% 9 - Senges, PR                            | 34 - Santa Izabel do Oeste, PR
% 10 - Santo Antonio do Sudoeste, PR        | 35 - Centenario do Sul, PR
% 11 - Curitiba, PR                         | 36 - Sao Joao, PR
% 12 - Nova Londrina, PR                    | 37 - Florestopolis, PR
% 13 - Umuarama, PR                         | 38 - Contenda, PR
% 14 - Arapongas, PR                        | 39 - Guaratuba, PR
% 15 - Alvorada do Sul, PR                  | 40 - Luiziana, PR
% 16 - Roncador, PR                         | 41 - Cafeara, PR
% 17 - Fenix, PR                            | 42 - Castro, PR
% 18 - Maua da Serra, PR                    | 43 - Lapa, PR
% 19 - Cruzeiro do Oeste, PR                | 44 - Toledo, PR
% 20 - Urai, PR                             | 45 - Piraquara, PR
% 21 - Cornelio Procopio, PR                | 46 - Jacarezinho, PR
% 22 - Sapopema, PR                         | 47 - Matinhos, PR
% 23 - General Carneiro, PR                 | 48 - Assai, PR
% 24 - Sao Jose dos Pinhais, PR             | 49 - Paranacity, PR
% 25 - Indianopolis, PR                     | 50 - Primeiro de Maio, PR

DistMatriz = readmatrix('C:\Users\viniv\Desktop\engenhariaeletrica\TCC\Atividade4\MatrizDistOriginal.txt');

%   Nmr de simulações
n_simulacoes = 100;

%   Criação da Tabela de Resultados
Tab_Resultados = zeros(n_simulacoes,3);
Resultados_Final = zeros(1,3);

%   Nmr de cidades
num_cidades = size(DistMatriz, 1);

for sim = 1:n_simulacoes
    
    %   Sortear 10 cidades
    indi_random = randperm(num_cidades, 10);
    
    % Selecionar as 10 cidades na matriz original
    MatrizDistTrab = DistMatriz(indi_random, indi_random);
    
    % Chamar a função Força Bruta
    resultados_forca_bruta = forcabruta(MatrizDistTrab);
    
    % Acessar os resultados
    distanciamenor = resultados_forca_bruta.distanciamenor;
    Indice_Rota_menor = resultados_forca_bruta.Indice_Rota_menor;
    Rota_menor = resultados_forca_bruta.Rota_menor;
    distanciamaior = resultados_forca_bruta.distanciamaior;
    Indice_Rota_maior = resultados_forca_bruta.Indice_Rota_maior;
    Rota_maior = resultados_forca_bruta.Rota_maior;
    
    % Convertendo os índices para os números das cidades sorteadas
    cidades_sorteadas = indi_random;
    cidades_menor = cidades_sorteadas(Rota_menor);
    cidades_maior = cidades_sorteadas(Rota_maior);
    
    % Agora você tem os resultados nos formatos desejados
    disp(['A distância total da menor rota é e a rota é a:']);
    distanciamenor
    cidades_menor
    Rota_menor
    disp(['A distância total da maior rota é e a rota é a:']);
    distanciamaior
    cidades_maior
    Rota_maior
    
    tempoFB = resultados_forca_bruta.tempoFB;
    
    Tab_Resultados(sim, 1) = tempoFB;

end

Resultados_Final(1,1) = mean(Tab_Resultados(:,1));
disp(['Média dos tempos das simulações: ', num2str(Resultados_Final(1,1))]);
tic_total = toc

















