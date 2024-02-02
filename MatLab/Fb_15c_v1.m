%clc 
clear all

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%   NAO RODAR %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



tic

% Dados Cidades N = 15
% 1  - UEL, Londrina
% 2  - Ibiporã               ; Raio de 20km
% 3  - Maringá               ; Raio de 40km
% 4  - Cascavel              ; Raio de 80km
% 5  - Paranagua             ; Raio maior que 160km
% 6  - Pérola
% 7  - Palmas
% 8  - Brasilandia do Sul
% 9  - Sengés
% 10 - Santo Antonio do Sudoeste
% 11 - Curitiba
% 12 - Nova londrina
% 13 - Umuarama
% 14 - Arapongas
% 15 - Alvorada do Sul

DistMatriz = [0      21     98      378     485     309     525     319     308     534     387     250     260     38      72;
              21     0      111     391     498     322     538     332     285     547     400     263     273     50      76;
              98     111    0       283     523     212     508     222     399     439     426     148     162     61      153;
              378    391    283     0       603     171     310     106     556     163     501     324     168     336     435;
              485    498    523     603     0       693     450     697     371     657     90      668     644     472     545;
              309    322    212     171     693     0       497     63      638     327     605     209     49      272     366;
              525    538    508     310     450     497     0       409     493     221     374     645     471     494     593;
              319    332    222     106     697     63      409     0       648     262     598     219     64      282     375;
              308    285    399     556     371     638     493     648     0       622     273     502     588     302     332;
              534    547    439     163     657     327     221     262     622     0       567     479     324     496     592;
              387    400    426     501     90      605     374     598     273     567     0       577     554     381     454;
              250    263    148     324     668     209     645     219     502     479     577     0       156     214     255;
              260    273    162     168     644     49      471     64      588     324     554     156     0       223     316;
              38     50     61      336     472     272     494     282     302     496     381     214     223     0       94;
              72     76     153     435     545     366     593     375     332     592     454     255     316     94      0];

VetorIndi = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15];

%permutação dos indices
Pi = perms(VetorIndi);

rotateste = [1 2 3 4 5];

% Variavel da Distancia
distanciamenor  = inf;
distanciamaior = 0;

% Calculo da rota
VetorDistancias = zeros(length(Pi),1);
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
        distanciamenor = distancia;
        Indice_Rota_menor = i;
        Rota_menor = rota;
    end
    if distancia > distanciamaior
        distanciamaior = distancia;
        Indice_Rota_maior = i;
        Rota_maior = rota;
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























