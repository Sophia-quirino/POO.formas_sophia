import turtle


class Figura:
    def __init__(self, cor, tamanho, x, y):
        """
        Construtor da classe base Figura.
        :param cor: cor de preenchimento da figura.
        :param tamanho: tamanho da figura (varia conforme o tipo).
        :param x: posição X no canvas.
        :param y: posição Y no canvas.
        """
        self.cor = cor
        self.tamanho = tamanho
        self.x = x
        self.y = y
        
    def mover(self):
        """Move a tartaruga para a posição especificada sem desenhar."""
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

    def desenhar(self):
        """Método genérico, sobrescrito nas subclasses."""
        pass  


class Quadrado(Figura):
    def desenhar(self):
        """DESENHA UM QUADRADO"""
        self.mover()
        turtle.color(self.cor)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.tamanho)
            turtle.right(90)
        turtle.end_fill()


class Triangulo(Figura):
    def desenhar(self):
        """DESENHA UM TRIANGULO"""
        self.mover()
        turtle.color(self.cor)
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(self.tamanho)
            turtle.left(120)
        turtle.end_fill()


class Circulo(Figura):
    def desenhar(self):
        """DESENHA UM CIRCULO"""
        self.mover()
        turtle.color(self.cor)
        turtle.begin_fill()
        turtle.circle(self.tamanho)
        turtle.end_fill()


class Hexagono(Figura):
    def desenhar(self):
        """DESENHA UM HEXAGONO"""
        self.mover()
        turtle.color(self.cor)
        turtle.begin_fill()
        for _ in range(6):
            turtle.forward(self.tamanho)
            turtle.left(60)
        turtle.end_fill()



# Programa principal

turtle.speed(3)  # Velocidade média do desenho

formas = [
    Quadrado("black", 100, -200, 100),
    Triangulo("orange", 100, 0, 100),
    Circulo("pink", 50, 200, 100),
    Hexagono("blue", 70, 0, -150)
]

for forma in formas:
    forma.desenhar()

turtle.hideturtle()
turtle.done()


