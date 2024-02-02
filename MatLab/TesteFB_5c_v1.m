clc 
clear all
tic

% Dados Cidades N = 5
% 1 - Londrina
% 2 - Ibiporã               ; Raio de 20km
% 3 - Maringá               ; Raio de 40km
% 4 - Cascavel              ; Raio de 80km
% 5 - Paranagua             ; Raio maior que 160km

DistMatriz = [0      21      98      378     485;
              21     0       111     391     498;
              98     111     0       283     523;
              378    391     283     0       603;
              485    498     523     603     0  ];
 
VetorIndi = [1 2 3 4 5];

%permutação dos indices
Pi = perms(VetorIndi);

rotateste = [1 2 3 4 5];

% Variavel da Distancia
distanciamenor = inf;
distanciamaior = 0;

% Calculo da rota
VetorDistancias   = zeros(length(Pi),1);
Indice_Rota_menor = 0;
Indice_Rota_maior = 0;

for i = 1:length(Pi)
    rota = Pi(i, :); % Armazena a rota atual
    distancia   = 0;
    
    for j = 1:length(rota)   
        Cidade_partida = rota(j);
        Cidade_chegada = rota(mod(j, length(rota)) + 1);
        distancia = distancia + DistMatriz(Cidade_partida, Cidade_chegada);
    end

    % Armazenador de distancias
    VetorDistancias(i,1) = distancia;

    % Comparadores
    if distancia < distanciamenor
        distanciamenor    = distancia;
        Indice_Rota_menor = i;
        Rota_menor        = rota;
    end
    if distancia > distanciamaior
        distanciamaior    = distancia;
        Indice_Rota_maior = i;
        Rota_maior        = rota;
    end

end

% Exibi as distâncias
disp(['A distância total da menor rota é e a rota é a:']);
distanciamenor
Indice_Rota_menor
Rota_menor
disp(['A distância total da maior rota ée a rota é a:']);
distanciamaior
Indice_Rota_maior
Rota_maior

toc























