import copy
class MatrixSizeError(Exception):
    pass 

def handler_matrix_size(func):
    def new_func(*args, **kwargs):
        if args[0].size() != args[1].size():
            raise MatrixSizeError
        return func(*args)
    return new_func

class Matrix:
    # Part 1
    def __init__(self, matrix):
        # matrix is mutable, so we need deep copy 
        self._matrix = copy.deepcopy(matrix)
    
    def __str__(self):
        return '\n'.join('\t'.join(map(str, line)) for line in self._matrix)
    
    # Part 2
    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self._matrix == other._matrix
        else:
            raise TypeError 
        
    def size(self):
        row = len(self._matrix)
        col = len(self._matrix[0])
        return row, col
    
     # Part 3
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size() != other.size():
            raise MatrixSizeError

        n_rows, n_cols = self.size()
        new_matrix_data = [
            [
                self._matrix[i][j] + other._matrix[i][j]
                for j in range(n_cols)
            ]
            for i in range(n_rows)
        ]
        return Matrix(new_matrix_data)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size() != other.size():
            raise MatrixSizeError

        n_rows, n_cols = self.size()
        new_matrix_data = [
            [
                self._matrix[i][j] - other._matrix[i][j]
                for j in range(n_cols)
            ]
            for i in range(n_rows)
        ]
        return Matrix(new_matrix_data)

    # Part 4
    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError

        if self.size()[1] != other.size()[0]:
            raise MatrixSizeError

        new_matrix_data = [
            [
                sum([
                    self._matrix[i][k] * other._matrix[k][j]
                    for k in range(self.size()[1])
                ])
                for j in range(other.size()[1])
            ]
            for i in range(self.size()[0])
        ]
        return Matrix(new_matrix_data)

    # Part 5
    def transpose(self):
        n_rows, n_cols = self.size()
        new_matrix_data = [
            [
                self._matrix[i][j]
                for i in range(n_rows)
            ]
            for j in range(n_cols)
        ]
        return Matrix(new_matrix_data)

    # Part 6
    def tr(self):
        n_rows, n_cols = self.size()
        if n_rows != n_cols:
            raise MatrixSizeError

        return sum([self._matrix[i][i] for i in range(n_rows)])

    @staticmethod
    def additional_minor(matrix, minor_row, minor_col):
        n_rows, n_cols = matrix.size()
        new_matrix_data = [
            [
                matrix._matrix[i][j]
                for j in range(n_cols)
                if j != minor_col
            ]
            for i in range(n_rows)
            if i != minor_row
        ]
        return Matrix(new_matrix_data)

    def det(self):
        n_rows, n_cols = self.size()
        if n_rows != n_cols:
            raise MatrixSizeError

        if n_rows == 1:
            return self._matrix[0][0]
        else:
            return sum([
                (-1)**j * self._matrix[0][j] * self.additional_minor(self, 0, j).det()
                for j in range(n_cols)
            ])
