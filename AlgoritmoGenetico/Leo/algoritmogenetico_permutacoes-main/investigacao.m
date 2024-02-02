clear 
close all

%%
seq = ['1' '2' '3' '4'];
n = 13;
tam = length(seq);
fak = int2fak(n,tam);
perm = fak2perm(fak,seq);

res = perm2fak(perm,seq);