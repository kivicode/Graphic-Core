from Core import Core
from Matrix import Matrix
from Message import *

core = None
testShape = None

def setup():
    global core, testShape, l, e, li, shift, drawS, drawE
    size(1000, 800, P3D)
    core = Core()
    loadIcons()
    l = core.spiral(Matrix([[0], [0], [0]]), 1, 2, 10)
    e = core.ellipse(Matrix([[0], [0], [0]]), 1, 1)
    li = core.ellipse(Matrix([[0], [0], [0]]), .1, .1)
    shift = core.shift(l, e)
    l[0][1][0].echo()
    
    drawS = core.spiral(Matrix([[4], [0], [0]]), 1, 2, 10)[0][1]
    drawE = core.ellipse(Matrix([[3], [0], [-PI]]), 1, 1)[0][1]

def draw():
    update()
    # for k in core.range(l, 1, .1):
    #     g = lambda x: l[0][1][map(x, 0, 1, 0, len(l[0][1]) - 1)]
    #     i = core.diff(g, k)
    #     point(i.get(0, 0), i.get(1, 0), i.get(2, 0))
    # core.draw(pull[0][1])
    noFill()
    shape(shift[0][0])
    core.draw(drawS)
    core.draw(drawE)

def update(draw=True):
    background(255)
    updateLog()
    updateTransform(draw)

def keyReleased():
    echo(str(key), ["Info", "Warning", "Error"][int(random(3))])

def updateTransform(d):
    lights()
    translate(width / 2, height / 2)
    rotateY(rotation[0])
    rotateX(rotation[1])
    fill(0, 255, 0)
    scale(scaling)
    if d:
        strokeWeight(0.01)
        stroke(255, 0, 0)
        line(-1, 0, 0, 1, 0, 0)
        stroke(0, 255, 0)
        line(0, -1, 0, 0, 1, 0)
        stroke(0, 0, 255)
        line(0, 0, -1, 0, 0, 1)
    stroke(0)
    strokeWeight(0.07)

    lights()

pressed = [0, 0]
rotation = [HALF_PI, 0]
scaling = 100

def mousePressed():
    global pressed
    pressed = [mouseX, mouseY]

def keyPressed():
    global testShape

def mouseWheel(e):
    global scaling
    scaling += e.count * .1

def mouseDragged():
    global rotation
    p = pressed
    dx, dy = mouseX - p[0], mouseY - p[1]
    rotation = [
        map(dx, -width, width, -TWO_PI, TWO_PI),
        map(dy, height, -height, -TWO_PI, TWO_PI)
    ]
