###snapshot-version: 0.1.4
###model-start
set POLYNOMIAL_LENGTH = 0 .. 255;
set L dimen 2;
param z{L};
param s1{L};
param C{L, POLYNOMIAL_LENGTH};
param K = 1e+06;
var X{L}  binary;
var s{POLYNOMIAL_LENGTH}  integer;
maximize number_of_coeffs: sum{(m,j) in L} X[m,j];
subject to res_1{(m,j) in L} : z[m,j] - sum{i in POLYNOMIAL_LENGTH: i <= j} C[
  m,j,i]*s[j - i] + sum{i in POLYNOMIAL_LENGTH: i > j} C[m,j,i]*s[256 + j - i]
   <= K*(1 - X[m,j]);
subject to res_2{(m,j) in L} : z[m,j] - sum{i in POLYNOMIAL_LENGTH: i <= j} C[
  m,j,i]*s[j - i] + sum{i in POLYNOMIAL_LENGTH: i > j} C[m,j,i]*s[256 + j - i]
   >= -(K*(1 - X[m,j]));
###model-end

###current-problem/environment-start
problem Initial;
environ Initial;
###current-problem/environment-end

###objectives-start
objective number_of_coeffs;
###objectives-end

###fixes-start
###fixes-end

###drop-restore-start
###drop-restore-end

