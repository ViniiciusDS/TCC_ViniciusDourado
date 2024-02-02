function [Z] = fz(X,Y) %Plota funçao do artigo Costa Filho e Poppi (1998)
                       %Autor: Ernesto F. Ferreyra Ramirez
                       %Data: 22/11/2006

Z = (3*((1-X)^2)*exp(-(X^2)-((Y+1)^2)));
Z = Z - (10*((X/5)-X^3-Y^5)*exp((-X^2)-(Y^2)));
Z = Z - ((1/3)*exp(-((X+1)^2)-(Y^2)+(3/5)*(1.7*sin(pi*X)+1.7*cos(2*Y))));
