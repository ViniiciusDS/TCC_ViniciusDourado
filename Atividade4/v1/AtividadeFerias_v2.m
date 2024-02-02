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
% 23 - General Carneiro, PR                 | 48 - Assai, PR1
% 24 - Sao Jose dos Pinhais, PR             | 49 - Paranacity, PR
% 25 - Indianopolis, PR                     | 50 - Primeiro de Maio, PR

%   Matrizes de dados
%DistMatriz = readmatrix('MatrizDistOriginal.txt');
DistMatriz = readmatrix('MatrizDistProfessor.txt');
%DistMatriz = readmatrix('MatrizDistOriginal.txt');

%   Nmr de simulações e cidades aleatórias
n_simulacoes  = 10;
N_cidades     = 10;     %%%%%%    12 é o limite para força bruta %%%%%%%%

%   Tamanho População inicial e Numero de gerações para o Algoritmo Genético
tam_Pop_ini_AG = 10;
tam_gera_AG    = 100;

%   Variaveis para o modelo de Simulated Annealing
num_int_SA  = 100;
temp_ini    = 0.7;
taxa_resfri = 0.95;

%   Criação da Tabela de Resultados
Tab_Resultados_tempo   = zeros(n_simulacoes,3);
Resultados_Final_tempo = zeros(1,3);
Tab_Resultados_dist    = zeros(n_simulacoes,3);


%   Nmr de cidades
num_cidades = size(DistMatriz, 1);

RotaTeste = [1,2,3,4,5,6,7,8,9,10];

for sim = 1:n_simulacoes
    
    %   Sortear 10 cidades
    indi_random = randperm(num_cidades, N_cidades);
    
    % Selecionar as 10 cidades na matriz original
    MatrizDistTrab = DistMatriz(indi_random, indi_random);
    
    % Chamar a função Força Bruta
    resultados_forca_bruta = forcabruta(MatrizDistTrab);
    
    % Chamar a função Algoritmo Genético
    resultados_algoritmo_getenico = alggenetico(MatrizDistTrab,tam_Pop_ini_AG,tam_gera_AG);
    
    % Chamar a função Simulated Annealing
    resultados_SA = simulatedAnnealing(MatrizDistTrab,temp_ini,taxa_resfri,num_int_SA);

    %   Organização dos dados de saída das funções
    %   tempo:
    tempoFB = resultados_forca_bruta.tempoFB;
    tempoAG = resultados_algoritmo_getenico.tempoAG;
    tempoSA = resultados_SA.tempoSA;
    %   Distancia:
    menordistFB = resultados_forca_bruta.distanciamenor;
    menordistAG = resultados_algoritmo_getenico.menorDistancia;
    menordistSA = resultados_SA.menorDistancia;

    %   Tabulação dos resultados
    Tab_Resultados_tempo(sim, 1) = tempoFB;
    Tab_Resultados_dist(sim, 1)  = menordistFB;
    Tab_Resultados_tempo(sim, 2) = tempoAG;
    Tab_Resultados_dist(sim, 2)  = menordistAG;
    Tab_Resultados_tempo(sim, 3) = tempoSA;
    Tab_Resultados_dist(sim, 3)  = menordistSA;

end

% Calcula a média dos tempos das simulações
Resultados_Final_tempo(1,1) = mean(Tab_Resultados_tempo(:, 1));
Resultados_Final_tempo(1,2) = mean(Tab_Resultados_tempo(:, 2));
Resultados_Final_tempo(1,3) = mean(Tab_Resultados_tempo(:, 3));

% Calcula o desvio padrão dos tempos das simulações
desvio_padrao_temposFB = std(Tab_Resultados_tempo(:, 1));
desvio_padrao_temposAG = std(Tab_Resultados_tempo(:, 2));
desvio_padrao_temposSA = std(Tab_Resultados_tempo(:, 3));

% Crie um gráfico de linha para cada método
plot(num_cidades_vec, Tab_Resultados_tempo(:, 1), '-o', 'DisplayName', 'Força Bruta','LineWidth',5);
hold on;
plot(num_cidades_vec, Tab_Resultados_tempo(:, 2), '-o', 'DisplayName', 'Algoritmo Genético','LineWidth',5);
plot(num_cidades_vec, Tab_Resultados_tempo(:, 3), '-o', 'DisplayName', 'Simulated Annealing','LineWidth',5);

xlabel('Número de Cidades','FontSize', 20);
ylabel('Tempo de Execução (segundos)','FontSize', 20);
title('Tempo de Execução x Número de Cidades','FontSize', 20);
legend('Location', 'Northwest','FontSize',20);
% Configurar o tamanho da fonte dos números nos eixos x e y
ax = gca; % Obtenha o objeto dos eixos atuais
ax.FontSize = 20; % Altere o tamanho da fonte dos números dos eixos x e y aqui

grid on;
grid on;
hold off; 

% Crie um gráfico de linha para Algoritmo Genético e Simulated Annealing
figure;
plot(num_cidades_vec, Tab_Resultados_tempo(:, 2), '-o', 'DisplayName', 'Algoritmo Genético','LineWidth',5);
hold on;
plot(num_cidades_vec, Tab_Resultados_tempo(:, 3), '-o', 'DisplayName', 'Simulated Annealing','LineWidth',5);

xlabel('Número de Cidades','FontSize', 20);
ylabel('Tempo de Execução (segundos)','FontSize', 20);
title('Tempo de Execução de Algoritmo Genético e Simulated Annealing x Número de Cidades','FontSize', 20);
legend('Location', 'Northwest','FontSize',20);
grid on;
hold off;
% Configurar o tamanho da fonte dos números nos eixos x e y
ax = gca; % Obtenha o objeto dos eixos atuais
ax.FontSize = 20; % Altere o tamanho da fonte dos números dos eixos x e y aqui
grid on;

% Crie um gráfico de barras das distâncias em função do número de cidades
figure;
bar(num_cidades_vec, Tab_Resultados_dist, 'grouped');
xlabel('Número de Cidades', 'FontSize', 20);
ylabel('Distância', 'FontSize', 20);
title('Distância x Número de Cidades', 'FontSize', 20);
legend({'Força Bruta', 'Algoritmo Genético', 'Simulated Annealing'}, 'FontSize', 16);
% Configurar o tamanho da fonte dos números nos eixos x e y
ax = gca; % Obtenha o objeto dos eixos atuais
ax.FontSize = 20; % Altere o tamanho da fonte dos números dos eixos x e y aqui
grid on;

%   Exibe o Resultado final
%   Força bruta
disp(['Média dos tempos das simulações do Método Força Bruta: ', num2str(Resultados_Final_tempo(1,1)), ' segundos']);
disp(['Desvio padrão dos tempos das simulações: ', num2str(desvio_padrao_temposFB), ' segundos']);
%   Algoritmo Genético
disp(['Média dos tempos das simulações do Método Algoritmo Genético: ', num2str(Resultados_Final_tempo(1,2)), ' segundos']);
disp(['Desvio padrão dos tempos das simulações: ', num2str(desvio_padrao_temposAG), ' segundos']);
%   Simulated Annealing
disp(['Média dos tempos das simulações do Método Simulated Annealing: ', num2str(Resultados_Final_tempo(1,3)), ' segundos']);
disp(['Desvio padrão dos tempos das simulações: ', num2str(desvio_padrao_temposSA), ' segundos']);


% Exibe o tempo total de execução do programa
tic_total = toc(tic_total);
disp(['Tempo total de execução do programa: ', num2str(tic_total), ' segundos']);
















