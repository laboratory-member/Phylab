from manim import *
class title(Scene):
    def construct(self):
        svg = SVGMobject("phylab.svg")

        # 设置填充为蓝色，透明度为 1（不透明）
        svg.set_color_by_gradient(BLUE_B, BLUE_C)

        svg.scale(0.5)
 
        self.play(Flash(svg, color=BLUE, flash_radius=0.5))
        self.play(FadeIn(svg, run_time=2))

        text = Text("Flowers for Tuesday", font="Vladimir Script")
        text.next_to(svg,DOWN)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(svg),FadeOut(text))
        self.wait(1)


        preface1 = Text("If you are not confused by quantum physics", font="Microsoft YaHei UI", slant=ITALIC).scale(0.6)
        preface2 = Text("then you haven’t really understood it", font="Microsoft YaHei UI", slant=ITALIC).scale(0.6)
        preface3 = Text("Niels Bohr", font="Microsoft YaHei UI",weight=BOLD).scale(0.6)
        preface1.shift(UP*1)
        preface2.next_to(preface1,DOWN)
        preface3.next_to(preface2,DOWN)
        preface3.shift(DOWN*0.5)
        self.play(Write(preface1))
        self.play(Write(preface2))
        self.wait(2)
        self.play(Write(preface3))
        self.wait(2)

        