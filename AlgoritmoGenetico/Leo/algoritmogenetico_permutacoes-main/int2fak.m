

function fak = int2fak(int,tam)
    fak = zeros(1,tam);
    temp = int;
    for k = 1:tam
        fak(k) = idivide(int16(temp),factorial(tam-k));
        temp = mod(temp,factorial(tam-k));
    end
end