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
set LEVELS;
param reward {LEVELS};
param distance {LEVELS};
var t {L, LEVELS} binary;

# exact solution, useful for testing
param s1{INDICES} integer;

var distance = sum { i in INDICES } sqrt((s1[i] - s[i]) * (s1[i] - s[i]));

# we're looking for the solution that satisfies the most equations
maximize number_of_coeffs: sum {(m,j) in L} (x[m,j] + sum {l in LEVELS} t[m,j,l] * reward[l]);

# polynomial multiplication written out as an explicit sum
subject to equation_right {(m,j) in L}: 
  z[m,j] - sum {i in INDICES: i <= j} C[m,j,i]*s[j - i] 
         + sum {i in INDICES: i > j} C[m,j,i]*s[256 + j - i]
              <= (1 - x[m,j]) * K + sum {l in LEVELS} (1 - t[m,j,l]) * distance[l];

subject to equation_left {(m,j) in L}: 
z[m,j] - sum {i in INDICES: i <= j} C[m,j,i]*s[j - i] 
         + sum {i in INDICES: i > j} C[m,j,i]*s[256 + j - i]
        >= - (1 - x[m,j]) * K - sum {l in LEVELS} (1 - t[m,j,l]) * distance[l];

data;

set LEVELS := 1 2;
param distance := 1 10 2 30;
param reward := 1 0.3 2 0.1;