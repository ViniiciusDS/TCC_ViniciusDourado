disp('Programa ag') %Programa de Algoritmos Geneticos soh com Cross-Over e Mutaçao
                    %Implementaçao do Exemplo de Costa Filho e Poppi (1998)
                    %Autor: Ernesto F. Ferreyra Ramirez
                    %Data: 22/11/2006

clear all

%---Calculos preliminares---
vLim = 3       %Faixa de valores em X e Y [-vLim; +vLim]
res = 0.0003   %Resoluçao
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
nG = 2*(nBit + 1)     %Numero de genes de cada cromossomo
                      %adicionado um bit de sinal (1 neg. e 0 pos.)
                      %multiplicado por 2 devido aos eixos X e Y
                  
%---Parametros de Cross-over---
%qCO = 2                %Qte. Max. ptos. de ocorrencia por cromossomo

%---Parametros de Mutaçao---
qMU = 15                 %Qte. Max. de mutaçoes por cromossomo


tic   %Inicio da contagem de tempo


%---Criaçao da populaçao inicial---
Pop = round(rand(nG,nC));

%---Algoritmo Genetico---
for g = 1:gMax,
    
    disp(g)
    
	%---Calculo da Aptidao de cada individuo---
	for j = 1:nC,
        temp = num2str(Pop(2:(nBit+1),j))';  %Le codigo binario de X
        %Transforma codigo binario em Numero Real
        X(1,j) = -sign(Pop(1,j)-0.5)*bin2dec(num2str(temp))*res;
        
        temp = num2str(Pop((nBit+3):nG,j))';  %Le codigo binario de Y
        %Transforma codigo binario em Numero Real
        Y(1,j) = -sign(Pop((nBit+2),j)-0.5)*bin2dec(num2str(temp))*res;
        
        Apt(g,j) = fz(X(1,j),Y(1,j));   %Calculo da Aptidao
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
                FilhosMU(posMU,n) = bitcmp(PAI(posMU,1),1);
            end
        end
    end
    
    %---Populaçao da proxima geraçao---
    Pop = [Pais FilhosCO FilhosMU];
        
end

%---Resultados Finais---
%***Grafico***
clf
MaxApt = max(Apt,[],2);
plot(MaxApt,'.-b');
xlabel('Geraçao'); ylabel('Funçao Z');
%***Duraçao***
duracao = toc
