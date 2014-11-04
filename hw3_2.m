% hw_3.2
N = 10;
X = randn(N,1);
H = X*pinv(X'*X)*X';
eig(H)