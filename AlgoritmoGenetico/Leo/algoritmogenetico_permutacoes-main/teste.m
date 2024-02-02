
clear 
close all

%%
Alphabet = ['A' 'B' 'C' 'D'];
n_symbols = length(Alphabet);
n_bits = 1 + cast((log(factorial(n_symbols)-1) / log(2)),'uint16');

%(Alphabet, "ABCDEFGHJI", "BACDEFGHIJ", "JABCDEFGHI",
             %"BCDEFGHIJA", "JIHGFEDCBA"):
 perm = ['C' 'A' 'B' 'D'];
%for perm = 1:length(Alphabet)
    disp(perm)
    fak = perm_to_fak (perm, Alphabet);
    disp(fak)
    i = fak_to_int(fak);
    %i= compose(dec2bin(i));
    disp(sprintf('%07d',i));
%end

inteiro_em_fak = int_to_fak(i,10)
resposta = fak_apply(fak,Alphabet)