def loadIcons():
    global Info_ICON, Warning_ICON, Error_ICON, imgW, imgH, LogArray
    imgW, imgH = 30, 30
    Info_ICON = loadImage("icons/Info.png")
    Warning_ICON = loadImage("icons/Warning.png")
    Error_ICON = loadImage("icons/Error.png")
    w, h = imgW, imgH
    Info_ICON.resize(w, h)
    Warning_ICON.resize(w, h)
    Error_ICON.resize(w, h)
    # Log("A", "Info")
    # delay(1000)
    # Log("B", "Warning")

logMaxId = 0
LogArray = []

def echo(Message, T = "Info"):
    print Message, T
    global LogArray, logMaxId
    LogArray.append(Log(Message, T, logMaxId))
    logMaxId += 1

def updateLog():
    global LogArray, logMaxId
    for l in LogArray:
        l.draw()
        if l.kill():
            LogArray.remove(l)
            logMaxId -= 1
            for lo in range(l.i, len(LogArray)):
                lg = LogArray[lo]
                lg.i -= 1
class Log():
    def __init__(self, s, t, num):
        self.Msg = [s, t]
        self.i = num
        self.startTime = millis()
        self.duration = 30000
        self.destroyTime = 500

    def destroy(self):
        return millis() - self.startTime >= self.duration

    def kill(self):
        return millis() - self.startTime >= self.duration + self.destroyTime + 100

    def draw(self):
        w, h = 120, 40
        xp, yp = 10, 10
        with pushStyle():
            m = str(self.Msg[0])
            t = self.Msg[1]
            w = textWidth(m) + 20 + 50
            x = width - w - xp
            y = height - h - yp
            nh = (h + yp) * self.i
            fill(255)
            stroke(100 if not self.destroy() else 100 + millis() -
                   (self.startTime + self.duration + self.destroyTime))
            strokeWeight(2)
            rect(x, y - nh, w, h, 5)
            strokeWeight(1.5)
            line(x + imgW / 4 + imgW + 8, y - nh,
                 x + imgW / 4 + imgW + 8, y + h - nh)
            fill(50 if not self.destroy() else 50 + millis() -
                 (self.startTime + self.duration + self.destroyTime))
            textAlign(RIGHT, TOP)
            text(m, x + w - 10, y - nh + 12)
            ICON = None
            if t == "Error":
                ICON = Error_ICON
            elif t == "Warning":
                ICON = Warning_ICON
            elif t == "Info":
                ICON = Info_ICON
            image(ICON, x + imgW / 4, y + h / 2 - imgH / 2 - 1 - nh)
            noStroke()
            fill(255, 0 if not self.destroy() else 00 + millis() -
                 (self.startTime + self.duration + self.destroyTime))
            rect(x + imgW / 4, y + h / 2 - imgH / 2 - 1 - nh, imgW, imgH)
