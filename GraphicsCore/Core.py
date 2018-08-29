from Matrix import Matrix
from Message import *

class Core():

    defIX = Matrix([[1], [0], [0]])
    defIY = Matrix([[0], [1], [0]])
    defIZ = Matrix([[0], [0], [1]])

    def __init__(self):
        echo("Core Initted", "Info")

    def range(self, f, t, s):
        i = f
        out = []
        while i <= t:
            out.append(i)
            i += s
        return out + [t]

    '''<2D>'''

    def ellipse(self, pos, a, b, draw=False):
        mx, my, mz = 0, 0, 0

        ix = 1
        iy = 0
        iz = Matrix([[0], [0], [1]])
        pts = []
        f = lambda u: pos.add(Matrix([[a * cos(u)], [b * sin(u)], [0]]))

        t = self.range(0, TWO_PI, 0.1)
        s = createShape()
        s.beginShape()
        for v in self.range(0, TWO_PI, 0.1):
            p = f(v)
            pts.append(p)
            x, y, z = p.get(0, 0) + PI / HALF_PI - 2, p.get(1, 0), p.get(2, 0)
            mx += x
            my += y
            mz += z
            s.vertex(x, y, z)
        s.endShape()
        return [[s, pts], [f, 1, [0, 2 * PI]]]

    def spiral(self, pos, r, step, l, point=None, draw=False):
        ix = Matrix([[1], [0], [0]])
        iy = Matrix([[0], [1], [0]])
        iz = Matrix([[0], [0], [1]])
        pts = []
        # u = lambda t: ix.mult(
        # r * cos(t)).add(iy.mult(r * sin(t))).add(iz.mult((step * t) /
        # TWO_PI))
        u = lambda t: pos.add(Matrix(
            [[r * cos(t)], [r * sin(t)], [step * (t / TWO_PI)]]))
        s = createShape()
        s.beginShape()
        for t in self.range(-l, l, 0.1):
            p = u(t)
            pts.append(p)
            s.vertex(p.get(0, 0), p.get(1, 0), p.get(2, 0))
        s.endShape()
        return [[s, pts], [u, 1, [-l / 2, l / 2]]]

    def line(self, ax, ay, az, bx, by, bz):
        From = Matrix([[ax], [ay], [az]])
        To = Matrix([[bx], [by], [bz]])
        f = lambda t: From.mult(1 - t).add(To.mult(t))
        pts = []
        s = createShape()
        s.beginShape()
        for t in self.range(0, 1, 0.5):
            p = f(t)
            print t, f(float(t)).matrix
            pts.append(p)
            s.vertex(p.get(0, 0), p.get(1, 0), p.get(2, 0))
        s.endShape()
        return [[s, pts], [f, 1, [0, 1]]]

    '''</2D>'''

    '''<3D>'''

    def ellipsoid(self, pos, a, b, c):
        ix = Matrix([[1], [0], [0]])
        iy = Matrix([[0], [1], [0]])
        iz = Matrix([[0], [0], [1]])
        u = lambda v, u: Matrix(
            [[a * cos(v) * cos(u)], [b * cos(v) * sin(u)], [c * sin(v)]])
        ss = createShape(GROUP)
        pts = []
        for v in self.range(0, 2 * PI, 0.1):
            s = createShape()
            s.beginShape()
            for w in self.range(-PI / 2, PI / 2, 0.1):
                p = u(v, w)
                pts.append(p)
                s.vertex(p.get(0, 0), p.get(1, 0), p.get(2, 0))
            s.endShape()
            ss.addChild(s)
        return [[self.concateShape(ss), pts]], [u, 2, [0, 2 * PI], [-HALF_PI, HALF_PI]]

    '''</3D>'''

    '''<2D --> 3D>'''

    def shift(self, a, b):
        g = lambda t: a[0][1][int(map(t, 0, 1, 0, len(a[0][1]) - 1))]
        f = lambda t: b[0][1][int(map(t, 0, 1, 0, len(b[0][1]) - 1))]
        u = lambda v, w: g(w).add(f(v))
        pts = []
        ss = createShape(GROUP)
        for i in self.range(0, 1, .01):
            s = createShape()
            s.beginShape()
            for j in self.range(0, 1, .01):
                p = u(i, j)
                s.vertex(p.get(0, 0), p.get(1, 0), p.get(2, 0))
                pts.append(p)
            s.endShape()
            ss.addChild(s)
        return [[self.concateShape(ss), pts], [u, 2, [0, 1], [0, 1]]]

    def pull(self, a, b):
        st = millis()
        e = Matrix([[1], [0], [0]])
        g = lambda t: a[0][1][int(map(t, 0, 1, 0, len(a[0][1]) - 1))]
        f = lambda t: b[0][1][int(map(t, 0, 1, 0, len(b[0][1]) - 1))]

        u = lambda v, w: g(w).add(f(v))
        pts = []
        ss = createShape(GROUP)
        for i in self.range(0, 1, .01):
            s = createShape()
            s.beginShape()
            for j in self.range(0, 1, .01):
                p = u(i, j)
                s.vertex(p.get(0, 0), p.get(1, 0), p.get(2, 0))
                pts.append(p)
            s.endShape()
            ss.addChild(s)
        echo("Succeed Pull", "Info")
        echo("Pulling duration is " + str(int(millis() - st)) + "ms", "Info")
        return [[self.concateShape(ss), pts], [u, 2, [0, 1], [0, 1]]]

    '''</2D --> 3D>'''

    '''<TESTS>'''

    '''</TESTS>'''

    '''<Utils>'''

    def draw(self, m):
        j = 0
        for i in m:
            k = m[constrain(j + 1, 0, len(m) - 1)]
            line(i.get(0, 0), i.get(1, 0), i.get(2, 0),
                 k.get(0, 0), k.get(1, 0), k.get(2, 0))
            point(i.get(0, 0), i.get(1, 0), i.get(2, 0))
            j += 1

    def diff(self, r, t, h=0.001):
        '''
        r(t+h)-r(t)
        -----------
             h
        '''
        # print r(t + h)
        print r, t
        return r(t + h).minus(r(t)).div(h)

    def concateShape(self, s):
        childs = s.getChildCount()
        out = createShape(GROUP)
        for i in range(childs):
            k = (i + 1) % childs
            curS = s.getChild(i)
            nextS = s.getChild(k)
            verts = curS.getVertexCount()
            for j in range(verts - 1):
                n = (j + 1) % verts
                v = [
                    curS.getVertex(j), curS.getVertex(n),
                    nextS.getVertex(n), nextS.getVertex(j)
                ]
                c = createShape()
                c.beginShape()
                for p in v:
                    point(p.x, p.y, p.z)
                    c.vertex(p.x, p.y, p.z)
                c.endShape()
                c.setFill(color(0, 240, 0) if i %
                          2 == 0 else color(13, 145, 13))
                noStroke()
                out.addChild(c)
        return out
    '''</Utils>'''
