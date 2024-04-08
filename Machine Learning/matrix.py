import random
from datetime import datetime


class Architect:
    def create_random_matrix(self,
                             rows: int = 3,
                             cols: int = 3
                             ) -> list[list[int]]:
        matrix: list[list[int]] = []
        for row in range(rows):
            matrix.append([])
            for _ in range(cols):
                matrix[row].append(random.randint(0,9))
        
        return matrix

    def check_matrix_dimensions(self, matrix: list[list]) -> tuple[int]:
        rows = len(matrix)
        columns = 0
        for row in matrix:
            if len(row) > columns:
                columns = len(row)

        return rows, columns

    def multiply_matrices(self,
                          matrix1: list[list[int|float]],
                          matrix2: list[list[int|float]]
                          ) -> list[list[int|float]]:
        if type(matrix1) != list or type(matrix2) != list:
            raise TypeError

        rows1, columns1 = self.check_matrix_dimensions(matrix1)
        rows2, columns2 = self.check_matrix_dimensions(matrix2)
        if columns1 != rows2:
            print('Matrices have incompatible dimensions')
            raise ValueError

        new_matrix: list[list[int|float]] = []
        for row in range(rows1):
            new_matrix.append([])
            for _ in range(columns2):
                new_matrix[row].append([])

        row = 0
        while row < rows1:
            column = 0
            while column < columns2:
                new_matrix[row][column] = 0
                num_index = 0
                while num_index < columns1:
                    new_matrix[row][column] += matrix1[row][num_index] * matrix2[num_index][column]
                    num_index += 1
                column += 1
            row += 1
        
        return new_matrix

    def show_matrix(self, matrix: list[list]) -> None:
        if type(matrix) != list:
            raise TypeError
        
        rows, columns = self.check_matrix_dimensions(matrix)
        longest_value_string = 0
        for row in matrix:
            for value in row:
                if len(str(value)) > longest_value_string:
                    longest_value_string = len(str(value))
        print(f'This is a {rows}x{columns} matrix:')
        for row in matrix:
            printable_row = []
            for value in row:
                value_len = len(str(value))
                value = f'{" " * (longest_value_string - value_len)}{value}'
                printable_row.append(value)
            print(printable_row)
    
    def string_to_matrix(self, string: str) -> list:
        if type(string) != str:
            raise TypeError
        if string[0] != '[' or string[-1] != ']':
            raise ValueError
        
        new_string = ''
        new_matrix = []
        while index < len(string):
            if string[index] == '[':
                index += 1
                start_index = index
                while index < len(string):
                    if string[index] == ']':
                        new_matrix.append(self.string_to_matrix[start_index:index])


        index = 0


_inst = Architect()
create_random_matrix = _inst.create_random_matrix
check_matrix_dimensions = _inst.check_matrix_dimensions
show_matrix = _inst.show_matrix
multiply_matrices = _inst.multiply_matrices


if __name__ == '__main__':
    A = create_random_matrix(int(input('Matrix A row amount: ')),int(input('Matrix A column amount: ')))
    B = create_random_matrix(int(input('Matrix B row amount: ')),int(input('Matrix B column amount: ')))
    show_initial = None
    while show_initial not in ['y', 'n']:
        show_initial = input('Show matrices A, B? (y/n) ').lower()
    start = datetime.now()
    C = multiply_matrices(A, B)

    matrices = []
    if show_initial == 'y':
        matrices = [A, B]
    if C:
        matrices.append(C)
    for matrix in matrices:
        show_matrix(matrix)
        print('')
    
    print(f'Calculation runtime: {datetime.now() - start}')