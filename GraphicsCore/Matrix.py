class Matrix():

    def __init__(self, row, useMatrix=False):
        self.matrix = []
        if not useMatrix:
            for i in row:
                self.matrix.append(i)
        else:
            self.matrix = row

    # def __call__(self):
    #     return self

    def abs(self):
        if self.size() == [3, 1]:
            return dist(self.get(0, 0), self.get(1, 0), self.get(2, 0), 0, 0, 0)

    def echo(self):
        print "Matrix:"
        for i in self.matrix:
            s = "\t|"
            k = 0
            for j in i:
                s += str(j) + (" " if k != len(i) - 1 else "")
                k += 1
            print s + "|"

    def get(self, i, j):
        return self.matrix[i][j]

    def size(self):
        return [len(self.matrix), len(self.matrix[0])]  # [rows, columns]

    def add(self, other):
        output = []
        if self.size() == other.size():
            r, c = self.size()[0], self.size()[1]
            for i in range(r):
                row = []
                for j in range(c):
                    col = self.matrix[i][j] + other.matrix[i][j]
                    row.append(col)
                output.append(row)
        return Matrix(output)

    def div(self, o):
        try:
            return self.mult(1 / o)
        except:
            return self.mult(1 / 0.001)

    def minus(self, other):
        output = []
        if self.size() == other.size():
            r, c = self.size()[0], self.size()[1]
            for i in range(r):
                row = []
                for j in range(c):
                    col = self.matrix[i][j] - other.matrix[i][j]
                    row.append(col)
                output.append(row)
        return Matrix(output)

    def mult(self, scalar):
        r, c = self.size()[0], self.size()[1]
        m = self.matrix
        for i in range(r):
            for j in range(c):
                m[i][j] = float(float(m[i][j]) * float(scalar))
        nm = Matrix(m, True)
        return nm

    def mmult(self, b):
        a = self
        c = a
        m, n = a.size()[0], a.size()[1]
        l, k = b.size()[0], b.size()[1]
        if l == n:
            for i in range(m):
                for j in range(n):
                    sum = 0
                    for o in range(n):
                        sum += a.matrix[i][o] * b.matrix[o][j]
                    c.matrix[i][j] = sum
        return c
    
    

    def srotate(self, A, B, C):
        x, y, z = self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]
        rm = [
            [1, 0, 0],
            [0, cos(A), -sin(A)],
            [0, sin(A), cos(A)]
        ]
        nx = x * rm[0][0] + y * rm[0][1] + z * rm[0][2]
        ny = x * rm[1][0] + y * rm[1][1] + z * rm[1][2]
        nz = x * rm[2][0] + y * rm[2][1] + z * rm[2][2]

        rm = [
            [cos(B), 0, sin(A)],
            [0, 1, 0],
            [0 - sin(B), 0, cos(B)]
        ]
        nx = x * rm[0][0] + y * rm[0][1] + z * rm[0][2]
        ny = x * rm[1][0] + y * rm[1][1] + z * rm[1][2]
        nz = x * rm[2][0] + y * rm[2][1] + z * rm[2][2]

        rm = [
            [cos(C), -sin(C), 0],
            [sin(C), cos(C), 0],
            [0, 0, 1]
        ]
        nx = x * rm[0][0] + y * rm[0][1] + z * rm[0][2]
        ny = x * rm[1][0] + y * rm[1][1] + z * rm[1][2]
        nz = x * rm[2][0] + y * rm[2][1] + z * rm[2][2]
        strokeWeight(.1)
        point(nx, ny, nz)
        return Matrix([[nx], [ny], [nz]])

    def rotate(self, p, A, B, C):
        px, py, pz = p.matrix[0][0], p.matrix[1][0], p.matrix[2][0]
        sx, sy, sz = self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]
        x, y, z = px - sx, py - sy, pz - sz
        rm = [
            [cos(A), -sin(A), sin(A)],
            [sin(B), cos(B), -sin(B)],
            [-sin(C), sin(C), cos(C)]
        ]
        nx = x * rm[0][0] + y * rm[0][1] + z * rm[0][2] + px
        ny = x * rm[1][0] + y * rm[1][1] + z * rm[1][2] + py
        nz = x * rm[2][0] + y * rm[2][1] + z * rm[2][2] + pz
        strokeWeight(.1)
        point(nx, ny, nz)
        return Matrix([[nx], [ny], [nz]])

    def T(self):
        out = self.matrix
        r, c = self.size()[0], self.size()[1]
        if r == c:
            for i in range(r):
                for j in range(c):
                    out[i][j] = self.matrix[j][i]
            self.matrix = out
        return self
