function perm = fak_2_perm(fak, it0)
    % Apply little endian FAK to iterable IT0.

    assert(length(fak) == length(it0));
    it = it0;
    perm = cell(1, length(fak));
    
    for k = length(fak):-1:1
        a_k = fak(k);
        assert(a_k <= k && a_k >= 0);
        perm{k} = it{a_k+1};
        it(a_k+1) = [];
    end
    
    % Convert perm to the same type as it0
    if ischar(it0)
        perm = [perm{:}];
    else
        perm = it0;
        for k = 1:length(perm)
            perm{k} = perm{k}(1);
        end
        perm = cell2mat(perm);
    end
end