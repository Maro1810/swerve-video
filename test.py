from manim import *
import numpy as np

class SectorScene(Scene):
    def construct(self):
        sector = Sector(radius=3.0, angle=60*DEGREES)

        shift = np.array([-1.5, -0.7, 0])

        sector.shift(shift)

        arc = Arc(angle=60*DEGREES)

        arc.shift(shift)

        arc.set_color(PINK)
        
        sector.set_color(BLUE)

        s = MathTex("s").move_to([2.9, 1.6, 0]).shift(shift)
        r = MathTex("r").move_to([1.5,-0.3,0]).shift(shift)
        theta = MathTex(r"\theta").move_to([1.1, 0.7, 0]).shift(shift)

        circumference = MathTex(r"C=2\pi r").move_to([-0.5, 2, 0]).shift(shift)

        arc_length = MathTex(r"s=\frac{\theta}{2\pi}\cdot 2\pi r").move_to([1.5,-1.7, 0]).shift(shift)

        self.play(Create(sector), 
                  run_time = 0.5)
        self.wait(0.2)

        self.play(Create(r))

        self.play(Create(arc))

        self.play(Create(theta))
        self.play(Create(s))

        self.play(Create(circumference), 
                  run_time = 0.5,
                  rate_func = linear)
        
        self.play(Create(arc_length),
                  run_time = 1.0,
                  rate_func = linear)
        
        self.wait(1)

        # arc_length = MathTex(r"s=r\theta")

        # self.play(Create(arc_length),
        #           run_time = 0.2,
        #           rate_func = linear)

        self.wait(3)