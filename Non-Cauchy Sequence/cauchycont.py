from manimlib.imports import *
import numpy as np

class connection(Scene):
    def construct(self):
        t1=TextMobject("Now Let us consider a")
        t1.shift(1.7*UP)
        t2=TextMobject("Non-Cauchy")
        t2.set_color(BLUE)
        t2.shift(0.4*UP)
        t2.scale(2.8)
        t3=TextMobject("Sequence")
        t3.scale(0.8)
        t3.shift(0.8*DOWN+2*RIGHT+0.4*UP)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(FadeIn(t3))
        self.wait(2)
        self.play(FadeOut(t1),FadeOut(t3))
        self.wait(1)

class intro(Scene):
    def construct(self):
        t1=TextMobject("Non-Cauchy")
        t2=TextMobject("Sequence")
        t2.scale(0.8)
        t2.shift(0.8*DOWN+2*RIGHT+0.4*UP)
        t1.set_color(BLUE)
        t1.scale(2.8)
        t1.shift(0.4*UP)
        self.play(ApplyMethod(t1.move_to,2.7*UP),ApplyMethod(t2.move_to,2.45*UP+4.6*RIGHT))
        self.wait(0.8)
        definition_text_1=TextMobject("A sequence, $(x_n)$ is said to be a" ,"Non-Cauchy", "Sequence if ","$\\exists$ $\\epsilon > 0$")
        definition_text_2=TextMobject("such that ","$\\forall$ K($\\epsilon$), $\\exists$ m,n $\geq$ $ K(\\epsilon)$","such that","$|x_m-x_n|\geq\\epsilon$")
        definition_text_1.shift(0.8*UP)
        definition_text_1.set_color_by_tex_to_color_map({"Non-Cauchy": YELLOW,"$\\exists$ $\\epsilon > 0$":RED})
        definition_text_2.set_color_by_tex_to_color_map({"$|x_m-x_n|\geq\\epsilon$": YELLOW,"$\\forall$ K($\\epsilon$), $\\exists$ m,n $\geq$ $ K(\\epsilon)$":BLUE})
        self.play(Write(definition_text_1))
        self.play(Write(definition_text_2))
        self.wait(3)

class to_graph(Scene):
    def construct(self):
        t1=TextMobject("Let us understand it", "graphically")
        t1.scale(1.8)
        t2=TextMobject("Consider the following","graph"," of sequence")
        t3=TextMobject("$1+(-1)^{n+2}$")
        t3.set_color(GREEN)
        t1.set_color_by_tex_to_color_map({"graphically": YELLOW})
        t2.set_color_by_tex_to_color_map({"graph":BLUE})
        self.play(Write(t1))
        self.wait(2)
        self.play(ApplyMethod(t1.shift,2.3*UP))
        self.play(Write(t2))
        self.wait(1)
        self.play(ReplacementTransform(t2,t3))
        self.wait(3)

class graph(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 15,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN+4*LEFT,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 16, 1),
        "y_labeled_nums": range(-5,6,1)
    }
    def construct(self):
        t1=TextMobject("$1+(-1)^{n+2}$")
        t1.scale(0.7)
        t1.to_edge(UP+RIGHT)
        t1.set_color(RED)
        self.add(t1)
        self.setup_axes(animate=True)
        self.wait(1)

        mathfunc = lambda x: 1+(-1)**(x+2)

        points=[Dot(color=RED,radius=0.05) for dot in range(1,16)]
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)
        [points[counter].shift(self.graph_origin+counter*RIGHT*x_each_unit+UP*y_each_unit*mathfunc(counter)) for counter in range(1,len(points))]

        for i in range(1,len(points)):
            self.add(points[i])
            self.wait(0.2)
        self.wait(1.5)

        t2=TextMobject("Since","there exists","atleast one $\\epsilon$")
        t2.shift(2.8*UP+0.75*RIGHT)
        #t2.scale(0.8)
        t2.set_color_by_tex_to_color_map({"there exists":BLUE,"atleast one $\\epsilon$":YELLOW})
        self.play(Write(t2))
        self.wait(1.5)
        t3=TextMobject("for which the condition is","satisfied",",")
        t3.shift(2.8*UP+0.8*RIGHT)
        #t3.scale(0.8)
        t3.set_color_by_tex_to_color_map({"satisfied":GREEN})
        self.play(ReplacementTransform(t2,t3))
        self.wait(1.5)
        t4=TextMobject("Let $\\epsilon=$1")
        t4.shift(2.8*UP+0.75*RIGHT)
        self.play(ReplacementTransform(t3,t4))
        self.wait(1)
        epsilonline=Line(start=self.graph_origin,end=UP*y_each_unit+self.graph_origin)
        epsilonline.shift(x_each_unit*RIGHT)
        self.play(Write(epsilonline))
        self.wait(1)
        self.play(FadeOut(t4))
        t5=TextMobject("$\\epsilon=1$")
        t5.scale(0.7)
        t5.shift(self.graph_origin+RIGHT*x_each_unit*1.8+UP*y_each_unit*0.8)
        self.play(FadeIn(t5))
        self.wait(1)
        t6=TextMobject("Now","$\\forall K(\\epsilon)$")
        t6.shift(2.8*UP+0.75*RIGHT)
        t6.set_color_by_tex_to_color_map({"$\\forall K(\\epsilon)$":BLUE})
        #t6.scale(0.8)
        self.play(Write(t6))
        self.wait(0.8)

        k_points=[Dot(color=WHITE, radius=0.05) for point in range(0,15)]
        [k_points[i].shift(self.graph_origin+RIGHT*(i+1)*x_each_unit) for i in range(0,15)]
        for j in range(0,15):
            self.add(k_points[j])
            self.wait(0.15)
        self.wait(1.7)

        t7=TextMobject("(Consider any","one","point)")
        t7.shift(2.1*DOWN+1.5*RIGHT)
        t7.set_color_by_tex_to_color_map({"one":RED})
        self.play(FadeIn(t7))
        #self.wait(1)
        self.wait(1)
        self.play(FadeOut(t7))
        for j in range(0,14):
            self.remove(k_points[j])
        self.wait(0.5)
        kdot=Dot(color=WHITE,radius=0.07)
        kdot.shift(self.graph_origin+6*RIGHT*x_each_unit)
        self.play(Write(kdot))        
        kpoint=TextMobject("K($\\epsilon$)")
        kpoint.set_color(BLUE)
        kpoint.scale(0.4)
        kpoint.shift(self.graph_origin+RIGHT*x_each_unit*6.5+DOWN*y_each_unit*0.4)
        self.play(Write(kpoint))
        self.wait(1)

        t8=TextMobject("$\\exists$ m,n","$\geq$","K($\\epsilon$)")
        t8.shift(2.8*UP+0.75*RIGHT)
        t8.set_color_by_tex_to_color_map({"$\\exists$ m,n":BLUE,"K($\\epsilon$)":YELLOW})
        #t8.scale(0.8)
        self.play(ReplacementTransform(t6,t8))
        self.wait(1.5)

        t9a=TextMobject("i.e given","any K($\\epsilon$)","we have","atleast")
        t9b=TextMobject("one pair","of m,n$ \geq K(\\epsilon)$")
        t9a.set_color_by_tex_to_color_map({"any K($\\epsilon$)":YELLOW,"atleast":BLUE})
        t9b.set_color_by_tex_to_color_map({"one pair":BLUE})
        t9a.shift(1.8*DOWN+1.5*RIGHT)
        t9b.shift(2.4*DOWN+1.5*RIGHT)
        group1=VGroup(t9a,t9b)
        self.play(Write(t9a))
        self.play(Write(t9b))
        self.wait(2.5)

        dot1=Dot(color=WHITE,radius=0.07)
        dot2=Dot(color=WHITE,radius=0.07)
        dot1.shift(self.graph_origin+RIGHT*9*x_each_unit)
        dot2.shift(self.graph_origin+RIGHT*10*x_each_unit)
        self.play(Write(dot1),Write(dot2))
        self.wait(0.7)
        m=TextMobject("m")
        n=TextMobject("n")
        m.scale(0.5)
        n.scale(0.5)
        m.shift(self.graph_origin+RIGHT*x_each_unit*9.3+DOWN*y_each_unit*0.28)
        n.shift(self.graph_origin+RIGHT*x_each_unit*10.3+DOWN*y_each_unit*0.28)
        m.set_color(BLUE)
        n.set_color(BLUE)
        self.play(Write(m))
        self.wait(0.1)
        self.play(Write(n))
        self.wait(1.5)

        self.play(FadeOut(group1))
        t10=TextMobject("such that","$|x_m-x_n|\geq\\epsilon$")
        t10.set_color_by_tex_to_color_map({"$|x_m-x_n|\geq\\epsilon$":YELLOW})
        t10.shift(2.8*UP+0.75*RIGHT)
        t10.scale(0.8)
        self.play(ReplacementTransform(t8,t10))
        self.wait(1.75)

        self.play(ApplyMethod(dot2.move_to,self.graph_origin+UP*y_each_unit*2+RIGHT*x_each_unit*10))
        self.wait(0.7)  

        diffdashedline=DashedLine(start=self.graph_origin+RIGHT*10*x_each_unit+2*y_each_unit*UP,end=self.graph_origin+9*RIGHT*x_each_unit+2*UP*y_each_unit,color=BLUE)
        self.play(Write(diffdashedline))

        diffline=Line(start=self.graph_origin+9*x_each_unit*RIGHT,end=self.graph_origin+9*x_each_unit*RIGHT+2*UP*y_each_unit)
        self.play(Write(diffline))
        self.wait(1.8)

        self.play(ApplyMethod(epsilonline.move_to,self.graph_origin+RIGHT*x_each_unit*4.5+DOWN*y_each_unit*3.5),ApplyMethod(diffline.move_to,self.graph_origin+RIGHT*x_each_unit*9+DOWN*y_each_unit*3.5))
        self.wait(0.1)
        self.play(FadeOut(diffdashedline),FadeOut(t5))
        self.wait(0.1)
        epsilon=TextMobject("$\\epsilon$")
        epsilon.shift(self.graph_origin+DOWN*5.5*y_each_unit+RIGHT*x_each_unit*4.5)
        epsilon.scale(0.83)
        difference=TextMobject("$|x_m-x_n|$")
        difference.shift(self.graph_origin+DOWN*5.5*y_each_unit+RIGHT*x_each_unit*9.2)
        difference.scale(0.7)
        self.play(FadeIn(epsilon),FadeIn(difference))
        self.wait(2)

        symboll=TextMobject("$\leq$")
        #symbol.scale(0.85)
        symboll.shift(self.graph_origin+RIGHT*6.5*x_each_unit+DOWN*y_each_unit*3.5)
        self.play(Write(symboll))
        self.wait(0.65)
        symbols=TextMobject("$\leq$")
        symbols.scale(0.7)
        symbols.shift(self.graph_origin+RIGHT*6.5*x_each_unit+DOWN*y_each_unit*5.5)
        self.play(Write(symbols))
        self.wait(2.5)

        self.play(FadeOut(symboll),FadeOut(symbols),FadeOut(epsilon),FadeOut(difference))
        self.wait(0.5)
        self.play(ApplyMethod(epsilonline.move_to,self.graph_origin+RIGHT*x_each_unit+UP*y_each_unit*0.5),ApplyMethod(diffline.move_to,self.graph_origin+10*x_each_unit*RIGHT+UP*y_each_unit))
        self.wait(2.5)

class conclusion1(Scene):
    def construct(self):
        t1=TextMobject("$|x_m-x_n|\geq\\epsilon$")
        t1.set_color_by_tex_to_color_map({"$|x_m-x_n|\geq\\epsilon$":YELLOW})
        t1.shift(2.8*UP+1.25*RIGHT)
        t1.scale(0.86)
        self.add(t1)
        self.wait(1)
        self.play(ApplyMethod(t1.move_to,1.5*UP))
        self.wait(1.3)
        t2=TextMobject("Similarlly","the condition is true","$\\forall$ natural numbers","m,n$\geq$$K(\\epsilon)$")
        t2.set_color_by_tex_to_color_map({"it is true":YELLOW,"$\\forall$ natural numbers":BLUE})
        t3=TextMobject("and also","$\\forall$ K($\\epsilon$)")
        t3.set_color_by_tex_to_color_map({"$\\forall$ K($\\epsilon$)":BLUE})
        t3.shift(DOWN)
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2.5)
        group1=VGroup(t1,t2,t3)

        text1=TextMobject("Hence it is a")
        text1.shift(UP)
        text2=TextMobject("Non-Cauchy","Sequence")
        text2.scale(1.7)
        text2.set_color_by_tex_to_color_map({"Non-Cauchy":GREEN,"Sequence":RED})
        group2=VGroup(text1,text2)
        self.play(ReplacementTransform(group1,group2))
        self.wait(4.5)

