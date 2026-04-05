class Matrix:
    def __init__(self, data):
        self.data = [row[:] for row in data]  # Deep copy
        self.n = len(self.data)

    def __mul__(self, other):
        if self.n != other.n:
            raise ValueError("Matrices must be same size for multiplication")
        result = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

