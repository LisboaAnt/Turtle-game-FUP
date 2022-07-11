#ANTONIO LISBOA DE CARVALHO  535865 
#JOGO FUP- IVO78
import turtle
import random
def personagem():

    def nort():
        if character.ycor() <= 180:
            character.goto(character.xcor(), character.ycor() + 10)

    def sul():
        if character.ycor() >= -275:
            character.goto(character.xcor(), character.ycor() - 10)

    def oeste():
        character.shape("shapes\garry.gif")
        if character.xcor() >= -230:
            character.goto(character.xcor() - 10, character.ycor())

    def leste():
        character.shape("shapes\garry2.gif")
        if character.xcor() <= 230:
            character.goto(character.xcor() + 10, character.ycor())

    def Key():
        # PLAYER comandos de entrada
        turtle.onkeypress(nort, 'Up')
        turtle.onkeypress(sul, 'Down')
        turtle.onkeypress(oeste, 'Left')
        turtle.onkeypress(leste, 'Right')
        turtle.listen()
    return Key()
def quadrado():
    arena = turtle.Turtle()
    arena.speed(0)
    arena.penup()
    arena.hideturtle()
    arena.setx(-250), arena.sety(200)
    arena.pendown()

    # Criar quadrado
    for _ in range(4):
        arena.forward(500)
        arena.right(90)
    arena.isvisible()
def veneno():
    global vidas
    pontos.forward(v)
    pontos.speed(10)
    if pontos.ycor() >= 190:
        pontos.goto(pontos.xcor(), 190)
        pontos.setheading(random.randint(181, 359))
    if pontos.xcor() >= 240:
        pontos.goto(240, pontos.ycor())
        pontos.setheading(random.randint(91, 270))
    if pontos.ycor() <= -290:
        pontos.setheading(random.randint(1, 179))
        pontos.goto(pontos.xcor(), -290)
    if pontos.xcor() <= -240:
        pontos.setheading(random.randint(270, 450))
        pontos.goto(-240, pontos.ycor())
    if pontos.xcor() - 20 <= character.xcor() <= pontos.xcor() + 20 and pontos.ycor() - 20 <= character.ycor() <= pontos.ycor() + 20:
        vidas += 1
        pontos.speed(0)
        pontos.goto(random.randint(-250, 250), random.randint(-200, 200))
        pontos.left(random.randint(1, 360))
def comida1():
    global v
    global score
    global vidas
    global vida2
    global total
    comida.forward(0.2)
    comida.speed(10)
    if comida.ycor() >= 190:
        comida.goto(comida.xcor(), 190)
        comida.setheading(random.randint(181, 359))
    if comida.xcor() >= 240:
        comida.goto(240, comida.ycor())
        comida.setheading(random.randint(91, 270))
    if comida.ycor() <= -290:
        comida.setheading(random.randint(1, 179))
        comida.goto(comida.xcor(), -290)
    if comida.xcor() <= -240:
        comida.setheading(random.randint(270, 450))
        comida.goto(-240, comida.ycor())
    if comida.xcor() - 20 <= character.xcor() <= comida.xcor() + 20 and comida.ycor() - 20 <= character.ycor() <= comida.ycor() + 20:
        score += 1
        total += 1
        if total == 10:
            v = 0.4
        if total == 20:
            v = 0.6
        if total == 30:
            v = 0.8
        if total == 40:
            v = 1
        comida.speed(0)
        comida.goto(random.randint(-250, 250), random.randint(-200, 200))
        comida.left(random.randint(1, 360))
        sketch.clear()
        sketch.write(f"PONTUACAO : {score}    V = {v*10}         total : {total}", align="center", font=("Courier", 24, "normal"))
#register shapes
turtle.register_shape("shapes\garry.gif")
turtle.register_shape("shapes\garry2.gif")
turtle.register_shape("shapes\cviva.gif")
turtle.register_shape("shapes\casa.gif")
turtle.register_shape("shapes\comida.gif")
turtle.register_shape("shapes\cfundo.gif")

#variaveis
v = 0.1
vidas = 0
quadrado()
velocidade = 0

#Janela
screen = turtle.Screen()
screen.bgpic("shapes\cfundo.gif")
screen.tracer()
screen.bgcolor()
screen.title('LISBOA')
screen.setup(width=1000, height=700)

#personagem
character = turtle.Turtle()
character.shape("shapes\garry.gif")
character.up()
character.speed(1)
character.setheading(90)
#vidas
vida1 = turtle.Turtle()
vida1.shape("shapes\casa.gif")
vida1.up()
vida1.speed(0)
vida1.color("red")
vida1.goto(-180,250)
vida1.setheading(90)

vida2 = turtle.Turtle()
vida2.shape("shapes\casa.gif")
vida2.up()
vida2.speed(0)
vida2.color("red")
vida2.goto(-205,250)
vida2.setheading(90)

vida3 = turtle.Turtle()
vida3.shape("shapes\casa.gif")
vida3.up()
vida3.speed(0)
vida3.color("red")
vida3.goto(-230,250)
vida3.setheading(90)

#veneno
pontos = turtle.Turtle()
pontos.shape("shapes\cviva.gif")

pontos.up()
pontos.speed(0)
pontos.sety(random.randint(-299, 199)), pontos.setx(random.randint(-249, 249))
pontos.setheading(random.randint(1, 360))


#comida
comida = turtle.Turtle()
comida.shape("shapes\comida.gif")
comida.up()
comida.speed(0)
comida.sety(random.randint(-299, 199)), pontos.setx(random.randint(-249, 249))
comida.setheading(random.randint(1, 360))

#score
total = 0
sketch = turtle.Turtle()
score = 0
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write(f"PONTUACAO : {score}    V = {v*10}         total : {total}", align="center", font=("Courier", 24, "normal"))


screen.tracer(0)
while True:
    screen.update()
    veneno()
    comida1()
    personagem()
    if score >= 10 and vidas > 0:
        score -= 10
        vidas -= 1
        sketch.clear()
        sketch.write(f"PONTUACAO : {score}    V = {v*10}         total : {total}", align="center", font=("Courier", 24, "normal"))
    if vidas == 1:
        vida2.showturtle()
    if vidas == 0:
        vida3.showturtle()
    if vidas == 1:
        vida3.hideturtle()
    if vidas == 2:
        vida2.hideturtle()
    if vidas == 3:
        vida1.hideturtle()
    if vidas == 3:
        screen.clear()
        for _ in range(200):
            sketch.write(f"Sua pontuação foi : {total}", align="center", font=("Courier", 24, "normal"))
        break