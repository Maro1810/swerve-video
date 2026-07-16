import math

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

        slash = Line([2.7, 0.7, 0], [1, 0, 0],
                     color = RED).move_to(arc_length.get_center()).shift(RIGHT*0.2, DOWN*0.2)

        self.wait(0.7)
        self.play(Create(sector), 
                  run_time = 0.5)
        
        self.wait(0.8)

        self.play(Create(r))

        self.play(Create(arc),
                  run_time = 0.3)

        self.play(Create(theta))

        self.wait(1)

        self.play(Create(s))

        self.wait(2.3)

        self.play(Create(circumference), 
                  run_time = 0.5,
                  rate_func = linear)
        
        self.wait(1)
        
        self.play(Create(arc_length),
                  run_time = 1.5,
                  rate_func = linear)
        
        self.wait(3)
        
        self.play(Create(slash),
                  run_time = 0.2)
        
        self.wait(1)

        self.play(FadeOut(arc_length, slash),
                  run_time = 0.4)

        arc_length = MathTex(r"s", "=", r"r\theta").shift(arc_length.get_center())

        self.play(Create(arc_length),
                  run_time = 0.5,
                  rate_func = linear)

        self.wait(1.4)

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != arc_length], 
                  run_time = 0.7)
               
        self.wait(0.5)
        self.play(arc_length.animate.shift(UP*4.5).scale(1.7).shift(LEFT*0.2))

        v = MathTex("v", font_size = 70).move_to([arc_length.get_center()]).shift(DOWN*2, LEFT*1.7)

        self.play(Create(v))

        arr = Arrow(start=LEFT, end=RIGHT).shift(UP*0.1, LEFT*0.4)

        self.play(Create(arr))

        om = MathTex(r"\omega", font_size = 70).move_to([arc_length.get_center()]).shift(DOWN*2, RIGHT*1.2)
        
        self.play(Create(om))
        
        left = MathTex(r"\frac{d}{dt}",
                       font_size = 60)
        right = MathTex(r"\frac{d}{dt}",
                        font_size = 60)

        left.to_edge(UP).shift(UP*2)
        right.to_edge(UP).shift(UP*2, RIGHT*3)

        self.play(left.animate.next_to(arc_length[0], LEFT).shift(UP*0.1))
        self.play(arc_length[2].animate.shift(RIGHT*0.7))
        self.play(right.animate.next_to(arc_length[2], LEFT))

        self.wait(1)

        arc_length2 = MathTex(r"\frac{ds}{dt}=r\frac{d\theta}{dt}", font_size = 65)

        arc_length2.move_to([arc_length.get_center()]).shift(LEFT*0.2)

        self.play(Transform(arc_length, arc_length2), 
                  FadeOut(om, run_time = 0.2),
                  FadeOut(v, run_time = 0.2),
                  FadeOut(arr, run_time = 0.2),
                  FadeOut(left, run_time = 0.2), 
                  FadeOut(right, run_time = 0.2))
        
        self.wait(2)

        rw = MathTex(r"v=r\omega", font_size = 65).move_to(arc_length2.get_center())

        w = MathTex(r"\omega=\frac{d\theta}{dt}")
        lin = MathTex(r"v=\frac{ds}{dt}")
        
        self.play(Uncreate(arc_length, run_time = 0.5))
        self.play(Create(rw))

        self.wait(0.5)
        self.play(Create(w), w.animate.move_to(rw.get_center()).shift(DOWN*1.5, LEFT*2))
        self.wait(1.2)
        self.play(Create(lin), lin.animate.move_to(rw.get_center()).shift(DOWN*1.5, RIGHT*2))
        
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time = 2)

class CircleScene(Scene):
    def construct(self):
        circles = []
        colors = [BLUE, GREEN, PINK, YELLOW, ORANGE]

        ang_velocity = PI

        for i in range(3):
            circles.append(Circle(radius=i*0.5+0.5, color=colors[i]))
        
        circ_group = VGroup(*circles)

        circ_group.arrange(buff = 1)

        start = circles[1].point_at_angle(PI/2)
        end = start+RIGHT*2

        theta = ValueTracker(0)

        romega = MathTex(r"v=r\omega", font_size=50).shift(UP*2.5)

        omega = MathTex(r"\omega=\frac{11}{7}\pi", font_size=30).shift(DOWN*2.5, LEFT*0.6)
        label = MathTex(r"rad/s", font_size = 30).next_to(omega)

        arrows = [self.create_arrow(i, circles, theta, colors[i]) for i in range(3)]

        labels = [MathTex("r = ", 
        str(0.5*i+0.5), font_size=20).move_to(circles[i].get_bottom()+0.4*DOWN) for i in range(3)]

        dots = [self.dot(i, circles, theta, colors[i]) for i in range(3)]

        # self.add_sound("voiceovers/in depth vid 17.m4a")

        self.add(circ_group)
        self.add(*arrows)
        self.add(*labels)
        self.add(*dots)

        self.play(*[FadeIn(mob) for mob in self.mobjects if mob != romega])
        
        self.play(Write(romega))
        self.play(FadeIn(omega, label), run_time=0.4)
        self.play(theta.animate.set_value(22*PI), run_time=14, rate_func=linear)

    def tangent_vector(self, angle, point, radius):
        return point+np.array([-radius*math.sin(angle), radius*math.cos(angle), 0])
    
    def create_arrow(self, i, circles, theta, col):
        return always_redraw(lambda: Arrow(
            circles[i].point_at_angle(theta.get_value()),
            self.tangent_vector(theta.get_value(), circles[i].point_at_angle(theta.get_value()), 0.5*i+0.5),
            buff=0,
            color=col,
            stroke_width=1))
    
    def dot(self, i, circles, theta, col):
        return always_redraw(lambda: Dot(
            point=circles[i].point_at_angle(theta.get_value()),
            radius=0.05,
            color=col
        ))
    
class RobotScene(Scene):
    def construct(self):
        chassis = Square(side_length=2, fill_color=BLUE_C, fill_opacity=1.0)

        modules = []

        pos = []

        top_left = chassis.get_left()+chassis.get_top()
        top_right = chassis.get_right()+chassis.get_top()
        bottom_left = chassis.get_left()+chassis.get_bottom()
        bottom_right = chassis.get_right()+chassis.get_bottom()

        pos.append(top_right)
        pos.append(top_left)
        pos.append(bottom_left)
        pos.append(bottom_right)

        romega = MathTex(r"||v||=||r||\omega", font_size=50).shift(UP*2.5)

        dir = MathTex("direction", "=", r"\ ?", font_size=50).shift(DOWN*2)

        r_vector = MathTex(r"r=\left\langle r_x,r_y \right\rangle", font_size=40).shift(RIGHT*3+UP)
        r_ortho = MathTex(r"r_\bot", "=", r"\left\langle -r_y,r_x \right\rangle", font_size=40).shift(RIGHT*2+UP*2)

        r_ortho_unit = MathTex(r"\hat{r}_\bot", "=", r"\left\langle \frac{-r_y}{||r||},\frac{r_x}{||r||} \right\rangle", font_size=40)

        for i in range(len(pos)):
            mod = Rectangle(width=0.2, height=0.5, fill_color=GRAY, fill_opacity=1.0).move_to(pos[i])

            modules.append(mod)

        pos_vectors = []

        for i in range(len(pos)):
            pos_vectors.append(Arrow(chassis.get_center(), 
                pos[i], stroke_width=2, buff=0, tip_length=0.2, color=LOGO_BLACK))
            
        vel_vectors = []

        for i in range(len(pos)):
            point = pos[i] - chassis.get_center()

            vel_vectors.append(Arrow(pos[i], pos[i]+[-point[1], point[0], 0], 
                    stroke_width=4, buff=0, tip_length=0.2, color=ORANGE))
        
        vec_copy = vel_vectors[0].copy()

        full_chassis = VGroup(chassis, Dot(chassis.get_center(), radius=0.05, color=BLACK))

        # self.add_sound("voiceovers/in depth vid 18.m4a")
        
        self.play(Create(full_chassis))

        self.play(*[Create(module) for module in modules], run_time=0.3)

        self.wait(0.7)

        for i in range(len(pos)):
            self.play(Create(pos_vectors[i]), run_time=0.7)

        self.wait(2.5)

        for i in range(len(pos)):
            if i==0:
                continue
            self.play(Uncreate(pos_vectors[i]), run_time=0.25)
        
        r = MathTex("r").shift(UP*0.6+RIGHT*0.2)

        self.play(Write(r))

        self.wait(2.5)
        
        self.play(*[Transform(mod, mod.copy().rotate(PI/4)) if index%2 == 0
                    else Transform(mod, mod.copy().rotate(-PI/4)) for index, mod in enumerate(modules)])

        self.play(Create(vel_vectors[0]))
   
        full_robot = VGroup(full_chassis, *modules, pos_vectors[0], r, vel_vectors[0])

        self.play(Rotate(full_robot, 
                         angle=2*PI, 
                         about_point=chassis.get_center()),
                         rate_func=linear,
                         run_time=5)
        
        self.play(Uncreate(vel_vectors[0]), run_time=0.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)

        full_robot.remove(vel_vectors[0])

        # self.add_sound("voiceovers/in depth vid 19.m4a")

        self.wait(0.6)

        self.play(Write(romega), run_time=0.7)

        self.wait(2)

        vec = Arrow(chassis.get_center(), top_right, stroke_width=5, buff=0, tip_length=0.5, color=ORANGE)

        self.play(Create(vec))

        self.play(Write(dir), Rotate(vec, angle=2*PI, about_point=chassis.get_center()), run_time=2)

        self.wait(1)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.4)

        self.play(FadeIn(full_robot))

        self.play(Write(r_vector))

        self.wait(2)

        self.play(Create(vec_copy))

        self.wait(1.5)

        self.play(Create(r_ortho))

        self.wait(1.2)

        self.play(r_ortho.animate.shift(UP*1.3+LEFT*2))

        r_ortho_unit.move_to(r_ortho)

        r_ortho_copy = r_ortho.copy()

        self.play(Transform(r_ortho, r_ortho_unit))

        self.play(ScaleInPlace(vec_copy, 0.4))

        self.play(vec_copy[0].animate.set_stroke(width=4, family=False), run_time=0.2)

        self.play(vec_copy.animate.move_to(top_right+UP*0.2+LEFT*0.2))

        # self.add_sound("voiceovers/in depth vid 19.m4a")

        romega = MathTex(r"\omega ||r||", font_size=40)

        romega.to_edge(UP).shift(RIGHT+UP*2)

        self.wait(2)

        self.play(Indicate(r_ortho[2]))

        self.play(FadeOut(r_ortho[0]), FadeOut(r_ortho[1]))

        self.play(romega.animate.next_to(r_ortho_unit[2], LEFT, buff=0.2))

        slash = Line([-0.5, 3.4, 0], [0, 3.0, 0],
                     color = RED).shift(LEFT*0.8+UP*0.1)
        
        slash2 = slash.copy().shift(RIGHT*1.1+DOWN*0.3)

        slash3 = slash2.copy().shift(RIGHT)

        self.wait(1)
        
        self.play(Create(slash), Create(slash2), Create(slash3))

        self.wait(1)

        romega2 = MathTex(r"\omega").move_to(romega)

        self.play(Transform(r_ortho[2], r_ortho_copy[2]), 
                  Transform(romega, romega2), 
                  FadeOut(slash), FadeOut(slash2), FadeOut(slash3), run_time = 0.5)
        
        self.play(r_ortho[2].animate.shift(LEFT*0.25), romega.animate.shift(RIGHT*0.45), run_time = 0.5)

        self.wait(1)

        v_rot = MathTex(r"v_{rot}=\left\langle -\omega r_y, \omega r_x \right\rangle", font_size=40).move_to(romega).shift(RIGHT*0.8)

        self.play(FadeOut(romega), Transform(r_ortho[2], v_rot), ScaleInPlace(vec_copy, 2.0))

        v_rot_label = MathTex(r"v_{rot}", font_size=30, color=ORANGE).shift(UP*1.9+LEFT*0.1)

        self.play(vec_copy.animate.shift(UP*0.2+LEFT*0.2))

        self.play(Write(v_rot_label))

        self.wait(1.5)

        v_trans = Arrow(top_right, top_right+UP*1.2+RIGHT*0.4, stroke_width=4, 
                        tip_length=0.2, color=YELLOW, buff=0)
        
        v_trans_label = MathTex(r"v_{trans}", font_size=30, color=YELLOW).next_to(v_trans).shift(UP*0.5+LEFT*0.1)

        self.play(Create(v_trans), Write(v_trans_label))

        trans_component = v_trans.get_end() - v_trans.get_start()

        rot_component = vec_copy.get_end() - vec_copy.get_start()

        overall = trans_component+rot_component

        v_overall = Arrow(top_right, top_right+overall, stroke_width=4,
                          tip_length=0.2, color=GREEN, buff=0)
        
        v_overall_label = MathTex(r"v_{overall}", font_size=30, color=GREEN).shift(UP*2.9+RIGHT*1.3)
        
        self.play(Create(v_overall), Write(v_overall_label), modules[0].animate.rotate(-PI/5.5))

        v_overall_eq = MathTex(r"v_{overall}=v_{trans}+v_{rot}=\left\langle v_{xr},v_{yr} \right\rangle+\left\langle -\omega r_y,\omega r_x \right\rangle=\left\langle v_{xr}-\omega r_y,v_{yr}+\omega r_x \right\rangle",
                            font_size=35)

        v_overall_eq.shift(DOWN*2.4)

        self.play(Write(v_overall_eq))

        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

class ModuleStatesScene(Scene):

    def construct(self):
        wpi = ImageMobject("wpilib.png")

        # self.play(FadeIn(wpi))

        chassis_speeds = MathTex(r"\begin{bmatrix} v_x \\ v_y \\ \omega \end{bmatrix}", font_size=40)

        chassis_speeds_label = MathTex("Chassis \ Speeds", font_size=40)
        robot_relative = MathTex("(Robot-relative)", font_size=20)

        chassis_speeds.shift(LEFT*3.8)

        arrow = Arrow(ORIGIN, ORIGIN+[1.3,0,0], stroke_width=3).next_to(chassis_speeds)

        rec = Rectangle(height=1, width=3.3, color=WHITE).next_to(arrow)

        arrow2 = arrow.copy().next_to(rec)

        v_overall = MathTex(r"\begin{bmatrix} v_{xr}-\omega r_y \\ v_{yr}+\omega r_x \end{bmatrix}", font_size=40).next_to(arrow2)
        v_overall_label = MathTex(r"v_{overall}", font_size=40)

        method_label = MathTex("toSwerveModuleStates()", font_size=25).shift(LEFT*0.5)

        brace = BraceBetweenPoints([-3, 0, 0], [-1.5, 0, 0]).next_to(chassis_speeds, DOWN)
        brace2 = BraceBetweenPoints([-3, 0, 0], [-0.5, 0, 0]).next_to(v_overall, DOWN)

        chassis_speeds_label.next_to(brace, DOWN)
        robot_relative.next_to(chassis_speeds_label, DOWN)
        v_overall_label.next_to(brace2, DOWN)

        self.play(Write(chassis_speeds))
        self.play(Create(brace), Write(chassis_speeds_label))
        self.play(Write(robot_relative), run_time=0.3)

        self.wait(1.6)
        self.play(Indicate(chassis_speeds))

        self.play(Create(arrow))
        self.play(Create(rec), Write(method_label), run_time=1)
        self.play(Create(arrow2))

        self.play(Write(v_overall), run_time=0.7)
        self.play(Create(brace2), Write(v_overall_label), Indicate(v_overall))

        self.wait(0.8)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

class MatrixScene(Scene):
    def construct(self):
        states_matrix = MathTex(r"v_{overall}= \begin{bmatrix} v_{xr}-\omega r_y\\ v_{yr}+\omega r_x\end{bmatrix}=", r"\begin{bmatrix} 1 & 0 & -r_y \\ 0 & 1 & r_x \end{bmatrix}", r"\begin{bmatrix} v_x \\ v_y \\ \omega \end{bmatrix}", font_size=40)

        states_matrix.shift(UP*1.5)
        method_label = MathTex("toSwerveModuleStates()", font_size=40)

        method_label.next_to(states_matrix, DOWN).shift(DOWN*1.5)

        arrow = Arrow(start=[0, 3, 0], end=[0, 1.5, 0]).next_to(states_matrix, DOWN)
        
        self.play(Write(states_matrix), run_time=3.6)
        self.play(Indicate(states_matrix[1]))

        self.wait(0.5)

        self.play(Create(arrow))
        self.play(Write(method_label))

        self.wait(1.2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])

class OptimizationScene(Scene):
    def construct(self):    
        circle = Circle(radius=2, color=BLUE)
        current_angle = Arrow(circle.get_center(), circle.point_at_angle(PI/3), color=YELLOW, buff=0)

        path_1 = current_angle.copy()
        path_2 = current_angle.copy()

        path_1_label = MathTex(r"75^{\circ}", color=GREEN)
        path_2_label = MathTex(r"105^{\circ}", color=RED)

        start_angle = MathTex(r"Start \ Angle = 60^{\circ}", font_size=30).shift(UP*3+LEFT*2)
        target_angle = MathTex(r"Target \ Angle \ = 135^{\circ}", font_size=30).shift(UP*3+RIGHT*2)

        arc1 = Arc(radius=2, start_angle=PI/3, angle=75*DEGREES, color=GREEN)
        arc2 = Arc(radius=2, start_angle=PI/3, angle=-105*DEGREES, color=RED)

        self.play(Create(circle))

        self.play(Create(current_angle))

        dashed = DashedLine(circle.point_at_angle(3*PI/4), circle.point_at_angle(-PI/4), dash_length=0.3)

        path_1.set_color(GREEN)
        path_2.set_color(RED)

        self.play(Write(start_angle))

        self.play(Create(dashed))

        self.play(Write(target_angle))

        self.play(
            Rotate(path_1, angle=5*PI/12, about_point=circle.get_center(), run_time=1.5),
            Rotate(path_2, angle=-7*PI/12, about_point=circle.get_center(), run_time=1.7),
            Create(arc1, run_time=1.5),
            Create(arc2, run_time=1.7)
        ) 

        path_1_label.next_to(arc1, UP)
        path_2_label.next_to(arc2, RIGHT)

        self.play(Write(path_1_label, run_time=0.8))
        self.play(Write(path_2_label))

        self.wait(1.5)

        self.play(Indicate(path_2_label))
        
        self.wait(1.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        ang_opt = Text("Angle Optimization", font_size=50).to_edge(UP)

        self.play(Write(ang_opt))

        current_angle = Arrow(circle.get_center(), circle.point_at_angle(PI/3), color=YELLOW, buff=0)

        circle = Circle(radius=2, color=BLUE)

        arc1 = Arc(radius=2, start_angle=PI/3, angle=75*DEGREES, color=GREEN)
        arc2 = Arc(radius=2, start_angle=PI/3, angle=-105*DEGREES, color=RED)

        dashed = DashedLine(circle.point_at_angle(3*PI/4), circle.point_at_angle(-PI/4), dash_length=0.3)

        path_1_label = MathTex(r"75^{\circ}", color=GREEN).next_to(arc1, UP)
        path_2_label = MathTex(r"105^{\circ}", color=RED).next_to(arc2, RIGHT)

        full_group = VGroup(current_angle, circle, arc1, arc2, dashed, path_1_label, path_2_label)

        full_group.shift(DOWN*0.5)

        self.play(FadeIn(full_group))

        circ = Circle(radius=0.5, color=YELLOW).move_to(path_1_label)

        self.play(Create(circ))

        self.wait(3)

        new_angle = Arrow(circle.get_center(), circle.get_right(), color=YELLOW, buff=0)

        self.play(
            FadeOut(full_group[0]), 
            FadeOut(full_group[2]), 
            FadeOut(full_group[3]), 
            FadeOut(full_group[5]), 
            FadeOut(full_group[6]),
            FadeOut(circ), Create(new_angle))

        self.wait(0.4)

        angle_indicator = Arc(radius=0.8, start_angle=0, angle=135*DEGREES).shift(DOWN*0.5)

        dashed2 = DashedLine(circle.get_center(), circle.get_right(), dash_length=0.3)

        self.play(Create(dashed2, run_time=0.4))

        angle_label = MathTex(r"135^{\circ}", font_size=30).next_to(angle_indicator, UP).shift(RIGHT*0.3+DOWN*0.1)

        self.play(Create(angle_indicator), Write(angle_label))

        self.wait(0.5)

        self.play(Rotate(new_angle, angle=-45*DEGREES, about_point=circle.get_center()))

        self.wait(1.6)

        self.play(new_angle.animate.rotate(180*DEGREES, about_point=circle.get_center()))

        self.wait(2)

        self.play(FadeOut(angle_indicator), 
                  FadeOut(dashed2), 
                  FadeOut(new_angle),
                  FadeOut(dashed2),
                  FadeOut(angle_label),
                  FadeOut(dashed))
        
        new_angle2 = Arrow(circle.get_center(), circle.get_right(), color=YELLOW, buff=0)

        