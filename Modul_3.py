
# SLPDV NumPy
import numpy as np

Matriks_A = np.array([[2,3],
                [1,-1]])
Matriks_B = np.array([7,1])

hasil = np.linalg.solve (Matriks_A,Matriks_B)

print ("Hasil SPLDV adalah:")
print ("x =",hasil[0],"y =",hasil[1])

# SLPDV SymPy
import sympy as sp

Matriks_A = sp.Matrix([[2,3],
                       [1,-1]])
Matriks_B = sp.Matrix([7,1])

hasil = Matriks_A.solve (Matriks_B)

print ("Hasil SPLDV adalah:")
print ("x =",hasil[0],"y =",hasil[1])

# SLPDV NumPy
import numpy as np

Matriks_A = np.array([[1, 2, 1],
                      [3, -1, 2],
                      [-2, 3, -1]])
Matriks_B = np.array([10, 5, -9])

hasil = np.linalg.solve(Matriks_A, Matriks_B)
print("Hasil SPLTV adalah:")
print("x =", hasil[0], ", y =", hasil[1], ", z =", hasil[2])

# SLPDV SymPy
import sympy as sp
x, y, z = sp.symbols('x y z')
eq1 = sp.Eq(x + 2*y + z, 10)
eq2 = sp.Eq(3*x - y + 2*z, 5)
eq3 = sp.Eq(-2*x + 3*y - z, -9)

solusi2_sympy = sp.solve((eq1, eq2, eq3), (x, y, z))
print("Solusi dengan SymPy:")
print(solusi2_sympy)
