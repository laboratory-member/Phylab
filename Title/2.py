from janim.imports import *

typst_doc = '''
#let name = "Typst"
欢迎使用 #name 进行排版。

== 数学公式
$ F = G frac(m_1 m_2,r^2) $
$ ((a, b), (c, d)) $

    
'''




class TypstExample(Timeline):
    def construct(self):
        doc = TypstDoc(typst_doc)
        typ = Typst('sum_(i=1)^n x_i')

        # Applying animations on text is slow
        self.play(Write(doc), duration=4)
        self.forward()
        self.play(FadeOut(doc))

        self.play(Write(typ))
        self.forward()
        self.play(FadeOut(typ))