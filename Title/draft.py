from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("混沌", font='Microsoft YaHei Light')
        self.play(Write(text))
        self.wait(1)
