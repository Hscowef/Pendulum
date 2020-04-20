import tkinter as tk
import math

class Pendulum:
    def __init__(self, root, canvas, origin, lenght, ball_radiant, angle):
        self.root = root
        self.canvas = canvas
        self.origin = origin
        self.lenght = lenght
        self.ball_radiant = ball_radiant
        self.angle = angle
        self.av = 0
        self.a_ac = 0
        self.flag = 0

        x = math.sin(self.angle) * self.lenght
        y = math.cos(self.angle) * self.lenght
        ball = (self.origin[0] + x, self.origin[1] + y)
        self.line = self.canvas.create_line(self.origin[0], self.origin[1], ball[0], ball[1], width=2.5)
        self.oval = self.canvas.create_oval(ball[0] - self.ball_radiant, ball[1] - self.ball_radiant, ball[0] + self.ball_radiant, ball[1] + self.ball_radiant, width=2.5)

    def update_pendulum(self):
        x = math.sin(self.angle) * self.lenght
        y = math.cos(self.angle) * self.lenght
        ball = (self.origin[0] + x, self.origin[1] + y)
        
        self.canvas.coords(self.line, self.origin[0], self.origin[1], ball[0], ball[1])
        self.canvas.coords(self.oval, ball[0] - self.ball_radiant, ball[1] - self.ball_radiant, ball[0] + self.ball_radiant, ball[1] + self.ball_radiant)

        self.angle += self.av
        self.a_ac = -0.01 * math.sin(self.angle)
        self.av += self.a_ac
        self.av *= 0.995

        if self.flag > 0:
            self.root.after(25, self.update_pendulum)


    def start(self):
        if not self.flag:
            self.flag = 1
            self.update_pendulum()

    def stop(self):
        self.flag = 0



if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500, bg="Ivory")
    canvas.pack(side=tk.LEFT, padx =5, pady =5)
    
    pendulum = Pendulum(root, canvas, (250, 100), 150, 20, 40 * math.pi / 180)

    tk.Button(root,text='Quit', width =8, command=root.quit).pack(side=tk.BOTTOM)
    tk.Button(root, text='Start', width =8, command=pendulum.start).pack()
    tk.Button(root, text='Stop', width =8, command=pendulum.stop).pack()  
    root.mainloop()