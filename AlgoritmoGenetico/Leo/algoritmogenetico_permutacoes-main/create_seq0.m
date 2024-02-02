function seq0 = create_seq0(tam)
    seq0 = char(zeros(1,tam));
    for k = 1:tam
        seq0(k) = int2str(k);
    end
end