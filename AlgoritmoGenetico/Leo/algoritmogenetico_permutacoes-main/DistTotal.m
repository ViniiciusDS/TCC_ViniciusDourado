%%

function disttotal = DistTotal(solucao, Dist)
    disttotal = 0;
    for k = 1:(numel(solucao)-1)
        disttotal = disttotal + Dist(solucao(k),solucao(k+1));
    end
end