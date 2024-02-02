
function numvector = str2numvector(str)
    numvector = zeros(1,length(str));
    for k = 1:length(str)
        numvector(k) = str2num(str(k));
    end
end