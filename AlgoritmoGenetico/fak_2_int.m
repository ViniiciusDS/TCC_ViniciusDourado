

function faknum = fak_2_int(fak)
    %Converte fak em inteiro
    i = 0;
    B_k = 1;
    
    for k=1:length(fak)
        i = i + fak(k) * B_k;
        B_k = B_k * (k);
    end

    faknum = i;
end
