from numpy.polynomial.polynomial import polyadd, polymul
from amplpy import AMPL
from csv_data import csv_to_ampl
from sys import argv

ampl = AMPL()

ampl.eval(
"""
set POLYNOMIAL_LENGTH = 0..255;
set L dimen 2;
param z {L};
param s1 {POLYNOMIAL_LENGTH};

param C { L , POLYNOMIAL_LENGTH}; 
param K = 1000000;
"""
)

def generate_ampl(dataset: str):
	z, L, C, s1ij = csv_to_ampl(dataset)

	ampl.getSet('L').set_values(L)
	ampl.getParameter('z').setValues(z)
	ampl.getParameter('s1').setValues(s1ij)

	ampl.getParameter('C').setValues(C)
	ampl.export_data(f"./csv_to_ampl/{dataset}.dat")

if __name__ == "__main__":
	file = argv[1]
	generate_ampl(file)