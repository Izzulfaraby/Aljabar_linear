import numpy as np
matriks_A = np.array([[11,12,13],
                      [14,15,16],
                      [17,18,19]])

matriks_B = np.array([[20,21,22],
                      [23,24,25],
                      [26,27,28]])

penjumlahan_matriks = matriks_A + matriks_B
pengurangan_matriks = matriks_A - matriks_B
perkalian_skalar = matriks_A * matriks_B
perkalian_dot = np.dot(matriks_A,matriks_B)
perkalian_cross = np.cross(matriks_A,matriks_B)
Transpose_A = np.transpose(matriks_A)
Transpose_B= np.transpose(matriks_B)

print ("Matriks A: \n",matriks_A)
print ("Matriks B: \n",matriks_B)
print ("Penjumlahan matriks: \n",penjumlahan_matriks)
print ("Pengurangan matriks: \n",pengurangan_matriks)
print ("Perkalian matriks skalar: \n",perkalian_skalar)
print ("Perkalian matriks dot: \n",perkalian_dot)
print ("Perkalian matriks cross: \n",perkalian_cross)
print ("Transpose matriks A: \n",Transpose_A)
print ("Transpose matriks B: \n",Transpose_B)
