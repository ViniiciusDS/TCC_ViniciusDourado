
function fak = perm2fak(perm, seq)
    fak = zeros(1,length(seq));
    seq0 = seq;
    for k = 1:length(seq)
        digit = find(seq0 == perm(k));
        fak(k) = digit-1;
        seq0(digit) = [];
    end
end