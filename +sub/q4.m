function [ output_args ] = q4( input_args )
%Q4 Summary of this function goes here
%   Detailed explanation goes here


syms x y
N = 5;
delta = 0.05;
dvc = 50;

epsi1 = originalVCBound(delta,N,dvc);
fprintf('epsi1 = %.3f\n',epsi1);
epsi2 = rademacher(delta, N, dvc);
fprintf('epsi2 = %.3f\n',epsi2);
f3 = @(x)parrondo(delta, N, dvc, x);
figure;
ezplot(f3);
% for t = -0.01:0.000001:1
%     if abs(f3(t)) < 0.0001
%         fprintf('epsi3 = %.3f\n', t);
%         break;
%     end
% end

f4 =  @(x)devroye(delta, N, dvc, x);
figure;
ezplot(f4);
% for t = -0.01:0.000001:1
%     if abs(f4(t)) < 0.0001 || t ==1
%         fprintf('epsi4 = %.3f\n', t);
%         break;
%     end
% end


epsi5 = variantVC(delta, N, dvc);
fprintf('epsi5 = %.3f\n',epsi5);
end

function res = mH(N, dvc)
    res = N^dvc;
end

function res = originalVCBound(delta, N, dvc)
    res = 8/N*log(4*mH(N,dvc)/delta);
end

function res = rademacher(delta, N, dvc)
    res = sqrt(2*log(2*N*mH(N,dvc))/N) + sqrt(2/N*log(1/delta))+1/N;
end

function res = parrondo(delta, N, dvc, epsi)
    res = sqrt(1/N*(2*epsi+ log(6*mH(2*N,dvc)/delta))) - epsi;
end

function res = devroye(delta, N, dvc, epsi)
    res = sqrt(0.5*N*(4*epsi*(1+epsi) + log(4*mH(N^2, dvc)/delta))) - epsi;
end

function res = variantVC(delta, N, dvc)
    res = sqrt(16/N*log(2*mH(N,dvc)/sqrt(delta)));
end
