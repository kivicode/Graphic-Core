from Matrix import Matrix

class KShape():

    def __init__(self, f, params, pts, s):
        self.func = f
        self.params = prams
        self.points = pts
        self.center = None
        self.shape = s
        mx, my, mz = 0, 0, 0
        for i in pts:
            mx += i.get(0, 0)
            my += i.get(1, 0)
            mz += i.get(2, 0)
        mx = mx / len(pts)
        my = my / len(pts)
        mz = mz / len(pts)
        self.center = Matrix([[mx], [my], [my]])
        
