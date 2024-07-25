# global parameters
param POLY_DEGREE = 255;
set INDICES = 0 .. POLY_DEGREE;
# set of message numbers 
set L dimen 2;

# we're looking for the solutions to
# z = c * s
param z{L} integer;
param C{L, INDICES} integer;
var s{INDICES}  integer;

# auxiliary variables to model the equality as two inequalities
var x{L}  binary;
param K = 1e9;

# additional relaxation parameters
param max_relaxation = 91;
var r{L} >= 0, <= max_relaxation;

# exact solution, useful for testing
param s1{L} integer;

# we're looking for the solution that satisfies the most equations
maximize number_of_coeffs: sum {(m,j) in L} x[m,j] + r[m,j];

# polynomial multiplication written out as an explicit sum
subject to equation_right {(m,j) in L}: 
  z[m,j] - sum {i in INDICES: i <= j} C[m,j,i]*s[j - i] 
         + sum {i in INDICES: i > j} C[m,j,i]*s[256 + j - i]
              <= (1 - x[m,j]) * K + r[m,j];

subject to equation_left {(m,j) in L}: 
z[m,j] - sum {i in INDICES: i <= j} C[m,j,i]*s[j - i] 
         + sum {i in INDICES: i > j} C[m,j,i]*s[256 + j - i]
        >= - (1 - x[m,j]) * K - r[m,j];
