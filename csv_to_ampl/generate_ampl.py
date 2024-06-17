from numpy.polynomial.polynomial import polyadd, polymul
from amplpy import AMPL, ampl_notebook
from csv_data import z, L, C, s1ij
ampl = AMPL()

ampl.eval(
    """
set POLYNOMIAL_LENGTH = 0..255;
set L dimen 2; # (m, j) z danych

param z {L};  # dla pary (m,j) z danych zij
param s1 {L};  # dla pary (m,j) z danych s1ij

param C { L , POLYNOMIAL_LENGTH}; 
param K = 1000000;

var X {L} binary; 
var s {POLYNOMIAL_LENGTH} integer; 

maximize number_of_coeffs: sum {(m,j) in L} X[m,j]; 

subject to res_1 {(m,j) in L}: 
	z[m, j] - sum {i in POLYNOMIAL_LENGTH: i <= j} C[m,j, i]*s[j - i]
		+ sum {i in POLYNOMIAL_LENGTH: i > j} C[m,j, i]*s[256 + j - i] <= K*(1 - X[m,j]); 
		
subject to res_2 {(m,j) in L}: 
	z[m,j] - sum {i in POLYNOMIAL_LENGTH: i <= j} C[m,j,i]*s[j - i]
		+ sum {i in POLYNOMIAL_LENGTH: i > j} C[m,j, i]*s[256 + j - i] >= -K*(1 - X[m,j]); 
 """
)


ampl.getSet('L').set_values(L)
# ampl.getParameter('s').setValues(z)
ampl.getParameter('z').setValues(z)
ampl.getParameter('s1').setValues(s1ij)

ampl.getParameter('C').setValues(C)
# ampl.solve(solver="cplex")
ampl.export_data("dil.dat")
ampl.export_model("dil.mod")
