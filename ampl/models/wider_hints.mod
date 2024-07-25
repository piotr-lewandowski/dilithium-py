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

# with additional hints about some variables
# hint that s[j] = s_hint[j] or s[j] = s_hint[j] + 1
set HINTS within INDICES;
param s_hint{HINTS} integer;
# hint that s[j] = s_exact[j]
set EXACT within INDICES;
param s_exact{EXACT} integer;

# auxiliary variables to model the equality as two inequalities
var x{L}  binary;
param K = 1e9;

# exact solution, useful for testing
param s1{L} integer;

# we're looking for the solution that satisfies the most equations
maximize number_of_coeffs: sum {(m,j) in L} x[m,j];

# polynomial multiplication written out as an explicit sum
subject to equation_right {(m,j) in L}: 
  z[m,j] - sum {i in INDICES: i <= j} C[m,j,i]*s[j - i] 
         + sum {i in INDICES: i > j} C[m,j,i]*s[256 + j - i]
              <= (1 - x[m,j]) * K;

subject to equation_left {(m,j) in L}: 
z[m,j] - sum {i in INDICES: i <= j} C[m,j,i]*s[j - i] 
         + sum {i in INDICES: i > j} C[m,j,i]*s[256 + j - i]
        >= - (1 - x[m,j]) * K;

subject to exact_hint {j in EXACT}:
  s[j] = s_exact[j];

subject to approximate_hint {j in HINTS}:
  s_hint[j] - 1 <= s[j] <= s_hint[j] + 1;
