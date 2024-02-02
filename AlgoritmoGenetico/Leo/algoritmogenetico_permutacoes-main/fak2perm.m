function perm = fak2perm(fak,seq)
    perm = char(zeros(1,length(fak)));
    seq0 = seq;
    for k = 1:length(fak)
        digit = seq0(fak(k)+1);
        perm(k) = digit;
        seq0(seq0 == digit) = [];
    end
end