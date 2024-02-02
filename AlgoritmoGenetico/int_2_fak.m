

function numfak = int_2_fak (i, tamFak)
    %Converter Int em uma representação em Fak de tamanho tamFak
    
    fak = zeros(1,tamFak);
    num = i;

    for k=1:tamFak
       fak(k) = mod(num,(k));
       num = floor(num/(k));
    end

numfak = fak;
end