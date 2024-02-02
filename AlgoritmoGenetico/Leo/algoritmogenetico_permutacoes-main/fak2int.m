
function int = fak2int(fak)
    int = 0;
    for k = 1:length(fak)
        int = int + fak(k)*factorial(length(fak)-k);
    end
end