%%
disp('Problema do Caixeiro Viajante')
clear 
close all

%% Distâncias
Dist(1,:) = [0, 89.5, 24.7, 15.8, 39.2, 100];
Dist(2,:) = [85.1, 0, 72.5, 91.4, 84.1, 121];
Dist(3,:) = [24.4, 72.2, 0, 34.9, 18.0,  79];
Dist(4,:) = [15.6, 91.2, 35,   0, 52.1, 113];
Dist(5,:) = [39,    84, 18.4, 49.5, 0, 61.2];
Dist(6,:) = [99.7, 120, 79.4, 110, 60.9, 0];

%   1 = Londrina
%   2 = Porecatu
%   3 = Rolândia
%   4 = Ibiporã
%   5 = Arapongas
%   6 = Maringá

%%
cidadeInicio = 1;
nSolucoes = factorial(length(Dist)-1);
tamSolucao = length(Dist) +1;
solucao = zeros(tamSolucao,1);
solucao(1,1) = cidadeInicio;
solucao(tamSolucao,1) = cidadeInicio;

perm_inicial = create_seq0(length(Dist));
perm_inicial(perm_inicial == int2str(cidadeInicio)) = []; 


%%
%---Calculos preliminares---
vLim = nSolucoes       %Faixa de valores em X e Y [-vLim; +vLim]
res = 1   %Resoluçao
nBit = numel(dec2bin(vLim/res))


%---Inicializaçao de parametros do AG---
gMax = 100             %Numero maximo de Geraçoes
nC = 20                %Numero de Cromossomos (Tamanho da Populaçao)
pP = 0.25             %Porcentagem de Pais
pFCO = 0.50           %Porcentagem de Filhos surgidos de Cross-over
pFMU = 1 - pP - pFCO  %Porcentagem de Filhos surgidos de Mutaçao
nP = round(pP*nC)     %Numero de Cromossomos-Pais em cada geraçao
nFCO = round(pFCO*nC) %Numero de Cromossomos-Filhos surgidos de Cross-over
nFMU = nC - nP - nFCO %Numero de Cromossomos-Filhos surgidos de Mutaçao
nG = (nBit)     %Numero de genes de cada cromossomo
                  
%---Parametros de Cross-over---
%qCO = 2                %Qte. Max. ptos. de ocorrencia por cromossomo

%---Parametros de Mutaçao---
qMU = 15                 %Qte. Max. de mutaçoes por cromossomo


tic   %Inicio da contagem de tempo


%---Criaçao da populaçao inicial---
Pop = round(rand(nG,nC));
%Pop(:,1) = [1; 1; 1; 0; 0; 0; 1];
%perm = char(zeros(nBit,nC));
%---Algoritmo Genetico---
for g = 1:gMax,
    
    disp(g)
    
	%---Calculo da Aptidao de cada individuo---
	for j = 1:nC,
        temp = num2str(Pop(:,j))';  %Le codigo binario de X
        
        %Transforma codigo binario em Numero Real
        %X(1,j) = -sign(Pop(1,j)-0.5)*bin2dec(num2str(temp))*res;
        
        %temp = num2str(Pop((nBit+3):nG,j))';  %Le codigo binario de Y
        %Transforma codigo binario em Numero Real
        %Y(1,j) = -sign(Pop((nBit+2),j)-0.5)*bin2dec(num2str(temp))*res;
        
        
        if(bin2dec(temp) >= nSolucoes)
            Apt(g,j) = 0;
        else       
            fak = int2fak(bin2dec(temp),length(Dist)-1);
            perm = fak2perm(fak,perm_inicial);
            solucao(2:length(Dist),1) = str2numvector(perm)';
            Apt(g,j) = 1/DistTotal(solucao,Dist);   %Calculo da Aptidao
        end
	end
    
    %---Seleçao dos "nP" cromossomos mais aptos---
    ap = Apt(g,:);
    for n = 1:nP,
        [aptMax(g,n) posMax(g,n)] = max(ap);
        ap(1,posMax(g,n)) = min(ap);
    end
    Pais = Pop(:,posMax(g,:));
    
    %---Cruzamento dos Cromossomos-Pais---
    %***Cross-over***
    for n = 1:nFCO,
        P = 1 + sum(round(rand(nP-1,1))); %sorteio do "Pai"
        M = 1 + sum(round(rand(nP-1,1))); %sorteio da "Mae"
        PAI = Pais(:,P);
        MAE = Pais(:,M);
        posCO = 1 + sum(round(rand((nG-1),1))); %Sorteio do Ponto de Cross-over
        sorteio = round(rand);
        if sorteio == 1,
            FilhosCO(1:posCO,n) = PAI(1:posCO,1);
            FilhosCO((posCO+1):nG,n) = MAE((posCO+1):nG,1);
        end
        if sorteio ==0,
            FilhosCO(1:posCO,n) = MAE(1:posCO,1);
            FilhosCO((posCO+1):nG,n) = PAI((posCO+1):nG,1);
        end
    end
            
    
    
    
    %***Mutaçao***
    for n = 1:nFMU,
        P = 1 + sum(round(rand(nP-1,1))); %sorteio do "Pai"
        PAI = Pais(:,P);
        FilhosMU(:,n) = PAI;
        Q = sum(round(rand(qMU,1))); %quantidade de mutaçoes
        if Q > 0,
            for k = 1:Q,
                posMU = 1 + sum(round(rand((nG-1),1)));
                
                if (FilhosMU(posMU,n) == 0)
                    FilhosMU(posMU,n) = 1;
                else
                    FilhosMU(posMU,n) = 0;
                end
                %FilhosMU(posMU,n) = bitcmp(PAI(posMU,1),1);
            end
        end
    end
    
    %---Populaçao da proxima geraçao---
    Pop = [Pais FilhosCO FilhosMU];
        
end


%---Resultados Finais---
%***Grafico***
clf
MaxApt = max(Apt')';
indice = (find(Apt(g) == max(MaxApt)));

fak_final = int2fak(bin2dec(num2str(Pop(:,1))'),length(Dist)-1);
perm_final = fak2perm(fak_final,perm_inicial)
solucao(2:length(Dist),1) = str2numvector(perm_final)';
DistanciaFinal = DistTotal(solucao,Dist)

plot(MaxApt,'.-b');

xlabel('Geraçao'); ylabel('Aptidão - 1/Dist');
%***Duraçao***
duracao = toc

%%
