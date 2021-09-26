# pyMath
An implementation of numerical methods, specific to linear algebra, from first principles.

## Class Modules:
[//]: =========================

#### Polynomial
Homogenous polynomial functions of a single variable are coded as arrays of coefficients. 
Includes standard methods for:
  - multiplication, division, addition and subtraction
  - derivation
  - variable evaluation

##### Legendre Polynomial:
An implementation for the generation of Legendré Polynomials to the specified degree.

#### Matrix
Composite class for numpy arrays to primitively deal with scalar & vector space matrix algebra.
Overwrites standard operators (*,+,-) to accommodate matrix operations.
Includes the standard methods for:
  - Inverse
  - Determinant
  - Transpose
  - Echelon Form
  - Several Row and Column Operations


## Numerical method modules:
[//]: ==========================

#### newton
Newton's Method(or Newton-Raphson method) for finding roots to higher order polynomials.

#### gauss_quad 
A method for generating Gaussian-Legendre quadrature points for numerical integration

#### 1D_FEM 
A Finite Element Method (FEM) approach to solving Partial Differential Equations (PDEs) over a 1-Dimensional domain.

#### 1D_FDM
A Finite Difference Method (FDM) implemented on a 1-Dimensional domain.

#### MSH 
Create a mesh array from a .msh format file

#### solvdoku 
A sudoku solver based on variable elimination methods.

#### eratos 
An implementation of the Sieve of Eratosthenes, an algorithm for finding primes up to certain number.
