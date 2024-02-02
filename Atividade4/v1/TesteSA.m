
%%%%%%%%% TESTE SIMULATED ANNEALING  %%%%%%%%%%%%%%%%

clear all
tic_total = tic;

DistMatriz = [0      21     98      378     485     309     525     319     308     534;
              21     0      111     391     498     322     538     332     285     547;
              98     111    0       283     523     212     508     222     399     439;
              378    391    283     0       603     171     310     106     556     163;
              485    498    523     603     0       693     450     697     371     657; 
              309    322    212     171     693     0       497     63      638     327;
              525    538    508     310     450     497     0       409     493     221;
              319    332    222     106     697     63      409     0       648     262;
              308    285    399     556     371     638     493     648     0       622;
              534    547    439     163     657     327     221     262     622     0];



resultados_SA = simulatedAnnealing(DistMatriz,0.7,0.95,1000);

tempoSA = resultados_SA.tempoSA
menordistSA = resultados_SA.menorDistancia
melhor_rota_sa = resultados_SA.melhorRota



tic_total = toc(tic_total)









