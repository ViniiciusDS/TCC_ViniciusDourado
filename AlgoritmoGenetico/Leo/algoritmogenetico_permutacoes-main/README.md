# algoritmogenetico_permutacoes
Algoritmo Genético para resolver problema do Caixeiro Viajante. O código se baseia no algoritmo implemetado pelo professor da disciplina Introdução à IA,
Ernesto Ferreyra Ramirez, em que, para resolver um problema de maximização de uma função de duas variáveis, utilizou-se a lógica de transformar os números
candidatos à solução em números binários. Dessa maneira, era possível realizar a permutação dos cromossomos de maneira que não houvesse problema.

Já no problema do caixeiro viajante, deseja-se passar por cada cidade apenas 1 vez, e criar um cromossomo em que cada gene representa uma das cidades geraria 
problema na etapa de permutação, uma vez que valores poderiam ser repetidos.

Dessa forma, a lógica dos números binários foi utilizada. Para isso, foi pensado que havia n! maneiras de se permutar as cidades, sem repeti-las. Buscou-se uma 
maneira de mapear cada permutação por um número inteiro (que pode ser transformado para binário posteriormente). Felizmente, há uma maneira de fazer isso, encontrada
na internet, disponível em: https://math.stackexchange.com/questions/4472267/creating-binary-information-from-a-permutation. A lógica é muito interessante, e envolve
escrever números em uma base fatorial (diferentemente da base decimal e da base binária, em que a base é sempre a mesma para cada dígito ou bit), em que cada número
pode ser associado a uma única permutação por meio de uma regra.

Assim, foram criadas as funções para que isso fosse possível, e aplicou-se a lógica no problema do caixeiro viajante, encontrando a solução ótima, que representa
a menor distância possível (330,09 km).




