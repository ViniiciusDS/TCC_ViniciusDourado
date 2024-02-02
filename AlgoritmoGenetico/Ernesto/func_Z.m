disp('Programa func_Z') %Plota funçao Z (dada em "fz.m")
                        %Autor: Ernesto Fernando Ferreyra Ramirez
                        %Data: 22/11/2006

clear all

v=[-3:0.1:+3];    %intervalo de valores


v1=v;

for k=1:(size(v,2)-1),
    v1=[v1;v];
end

v2=v1';

v1 = reshape(v1,1,numel(v1));
v2 = reshape(v2,1,numel(v2));

i=0;
for i=1:size(v1,2),
    x = v1(i);
    y = v2(i);
    z(i)=fz(x,y);
end

figure(1);
grid on;
plot3(v1,v2,z,'.');

figure(2);
N = sqrt(numel(z));
surf(v,v,reshape(z,N,N));
