import math
from math import sqrt
import numbers


def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)


def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


class Matrix(object):
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        det = 0
        if self.h == 1:
            det = self[0][0]
        else:
            det = self[0][0] * self[1][1] - self[1][0] * self[0][1]
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a non-square matrix.")
        trace = 0
        for i in range(self.h):
            trace += self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            return 1 / self[0][0]
        new_grid = []
        temp = self[0][0]
        self[0][0] = self[1][1]
        self[1][1] = temp
        self[0][1] = - self[0][1]
        self[1][0] = - self[1][0]
        det = self.determinant()
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                val = self.g[i][j] / det
                new_row.append(val)
            new_grid.append(new_row)
        return Matrix(new_grid)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        num_rows = self.w
        num_cols = self.h
        new_matrix = zeroes(num_rows, num_cols)
        for i in range(self.h):
            for j in range(self.w):
                untransposed_value = self.g[i][j]
                new_matrix[j][i] = untransposed_value
        return new_matrix

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")
        new_grid = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                v1 = self.g[i][j]
                v2 = other.g[i][j]
                v3 = v1 + v2
                new_row.append(v3)
            new_grid.append(new_row)
        return Matrix(new_grid)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        new_grid = []
        for row in self.g:
            new_row = []
            for value in row:
                new_value = -1 * value
                new_row.append(new_value)
            new_grid.append(new_row)
        return Matrix(new_grid)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + -other

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise (ValueError, "Matrices can only be multiplied if the width of  A  is equal to the height of B")
        new_grid = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):
                    new_grid[i][j] += self[i][k] * other[k][j]
        return new_grid

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            new_grid = []
            for row in self.g:
                new_row = []
                for value in row:
                    new_row.append(value * other)
                new_grid.append(new_row)
            return Matrix(new_grid)
            pass
