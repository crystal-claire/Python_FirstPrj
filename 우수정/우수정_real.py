#오프닝
from turtle import*
import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t2.speed(1)
t3.speed(1)
def sq1():
    t1.up()
    t1.goto(0,-50)
    t1.down()
    t1.forward(300)
    t1.left(90)
    t1.forward(160)
    t1.left(90)
    t1.forward(600)
    t1.left(90)
    t1.forward(160)
    t1.left(90)
    t1.forward(300)
    t1.reset()
    t2.reset()
def sq():
    t1.pencolor("white")
    t1.up()
    t1.goto(0,-50)
    t1.down()
    t1.forward(300)
    t1.left(90)
    t1.forward(160)
    t1.left(90)
    t1.forward(600)
    t1.left(90)
    t1.forward(160)
    t1.left(90)
    t1.forward(300)
    t1.reset()
    t2.reset()
    t2.pencolor("white")
def sqt():
    tt1.pencolor("white")
    tt1.up()
    tt1.goto(0,-50)
    tt1.down()
    tt1.forward(300)
    tt1.left(90)
    tt1.forward(160)
    tt1.left(90)
    tt1.forward(600)
    tt1.left(90)
    tt1.forward(160)
    tt1.left(90)
    tt1.forward(300)
    tt1.reset()
    tt1.speed(1)
    t2.reset()
    t2.pencolor("white")
t2.write("[나]\n버스를 잘못 탔다.\n급하게 내렸지만 주변은 황량한 벌판...",False,"center", ("","10"))
print(sq1())
t2.write("[나]\n엇..지도가... 없다?",False,"center", ("","10"))
print(sq1())
t2.write("[나]\n노을진 첨성대를 보기 위해 경주까지 왔다. ",False,"center", ("","10"))
print(sq1())
t2.write("[나]\n오늘의 일몰 시간은 19시 39분. ",False,"center", ("","10"))
print(sq1())
t2.write("[나]\n19시 안으로 도착해야만 노을을 감상할 수 있다. ",False,"center", ("","10"))
print(sq1())
t2.write("[나]\n과연 해낼 수 있을까..? ",False,"center", ("","10"))
print(sq1())
t2.write("☆★지도 없이 여행지에서 길을 찾아라!★☆ ",False,"center", ("","10"))
print(sq1())

#문제 브릿지


screen = turtle.Screen()
screen.setup(1500, 1000)
screen.bgpic("C:\\Users\\수정\\Desktop\\플젝\\우수정\\1갈림길.gif")
screen.update()   #갈림길이 배경으로 뜸
t2.pencolor("white")


screen = turtle.Screen()
image1 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\검은고양이.gif"
screen.addshape(image1)
image2 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\수상한사람.gif"
screen.addshape(image2)
image3 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\하얀고양이.gif"
screen.addshape(image3)
t3.shape(image1)
t3.stamp()


t2.write("[나]\n앗..여기는 어디지?",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]\n세 갈림길이네....첨성대는 어디로 가야하는걸까..?",False,"center",font=("Times",18,"bold"))
print(sq())
t2.write("[나]\n지도가 없으니 답답하네...",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]\n......!? ",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[수상한 고양이]   \n.....길, 알려줄까?",False,"center",font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n 네!!! 제발 알려주세요!!!!!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[수상한 고양이]   \n그렇다면 내가 내는 문제를 맞혀라!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[수상한 고양이]   \n목적지까지 가는 지름길을 알려주지!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n 좋아요!!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[수상한 고양이]   \n그럼 문제를 풀어보도록!",False,"center", font=("Times",18,"bold"))
print(sq())


#문제1-수상한 고양이
while True:
    n=textinput("문제", "not 10>5 \n위 식을 출력시 답이\nTrue일지 False일지 고르세요\n(ex: True(앞글자 대문자로 쓸 것 ))")
    if n=="False":
        t2.write("[수상한 고양이]   \n정답이다! \n지름길은 왼쪽에서 세번째 길이다!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    elif n!="False":
        t2.write("[수상한 고양이]   \n다시 풀어보도록!",False,"center", font=("Times",18,"bold"))
        print(sq())

while True:
    n=numinput("길을 선택하세요", "왼쪽부터 몇 번째 길로 갈지 선택하세요.\n(ex: 1(숫자만 입력할 것))")
    if n==3:
        t2.write("[수상한 고양이]   \n잘 했어! 행운을 빌어주지!!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    if n!=3:
        t2.write("[수상한 고양이]   \n 이 길이 아닐 텐데?",False,"center", font=("Times",18,"bold"))
        print(sq())


#문제 1->2 브릿지



screen = turtle.Screen()
image1 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\검은고양이.gif"
screen.addshape(image1)
image2 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\수상한사람.gif"
screen.addshape(image2)
image3 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\하얀고양이.gif"
screen.addshape(image3)
t3.shape(image2)#이미지변환
t3.stamp()

t2.write("[나]   \n또 세 갈림길이네....첨성대는 어디로 가야하는걸까..?",False,"center",font=("Times",18,"bold"))
print(sq())
t2.write("[신비로운 사람]   \n.....첨성대까지 가는 길을 찾는 모양이군",False,"center",font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n 네!!! 제발 알려주세요!!!!!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[신비로운 사람]   \n그렇다면 가위바위보 결투를 신청한다!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[신비로운 사람]   \n네가 이긴다면 목적지까지 가는 지름길을 알려주지!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n 좋아요!!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[신비로운 사람]   \n그럼 결투를 시작한다!",False,"center", font=("Times",18,"bold"))
print(sq())




#가위바위보

import random
rpcop=["가위","바위","보"]
while True:
    rpc2=random.choice(rpcop)
    print(rpc2)
    rpc1=textinput("가위바위보", "가위/바위/보 중 하나를 입력하세요\n(비긴 것도 패배 처리)")
    if rpc1=="가위" and rpc2=="보":
        t2.write("[수상한 사람] \n보를 내지 말 걸 그랬어.\n 나의 패배군.... 지름길은 왼쪽부터 첫 번째 길이다!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    elif rpc1=="가위" and rpc2=="가위":
        t2.write("[신비로운 사람] \n가위를 내길 잘 했군.\n비겼지만 나의 승리다! 재도전을 받아주지!",False,"center", font=("Times",18,"bold"))
        print(sq())
    elif rpc1=="가위" and rpc2=="바위":
        t2.write("[신비로운 사람] \n 바위를 내길 잘 했군.\n나의 승리다! 재도전을 받아주지!",False,"center", font=("Times",18,"bold"))
        print(sq())
    elif rpc1=="바위" and rpc2=="가위":
        t2.write("[신비로운 사람] \n가위를 내지 말 걸 그랬어.\n나의 패배군.... 지름길은 왼쪽부터 첫 번째 길이다!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    elif rpc1=="바위" and rpc2!="바위":
        t2.write("[신비로운 사람] \n바위를 내길 잘 했군.\n비겼지만 나의 승리다! 재도전을 받아주지!",False,"center", font=("Times",18,"bold"))
        print(sq())
    elif rpc1=="바위" and rpc2!="보":
        t2.write("[신비로운 사람] \n보를 내길 잘 했군.\n나의 승리다! 재도전을 받아주지!",False,"center", font=("Times",18,"bold"))
        print(sq())
    elif rpc1=="보" and rpc2=="바위":
        t2.write("[신비로운 사람] \n바위를 내지 말 걸 그랬어.\n나의 패배군.... 지름길은 왼쪽부터 첫 번째 길이다!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    elif rpc1=="보" and rpc2!="가위":
        t2.write("[신비로운 사람] \n가위를 내길 잘 했군.\n나의 승리다! 재도전을 받아주지!",False,"center", font=("Times",18,"bold"))
        print(sq())
    elif rpc1=="보" and rpc2!="보":
        t2.write("[신비로운 사람] \n보를 내길 잘 했군.\n비겼지만 나의 승리다! 재도전을 받아주지!",False,"center", font=("Times",18,"bold"))
        print(sq())

while True:
    n=numinput("길을 선택하세요", "왼쪽부터 몇 번째 길로 갈지 선택하세요.\n(ex: 1(숫자만 입력할 것))")
    if n==1:
        t2.write("[신비로운 사람]   \n좋은 결투였다. 제법이더군. \n행운을 빌어주겠네.",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    if n!=1:
        t2.write("[신비로운 사람]   \n 내가 알려준 길은 이 길이 아닐 텐데.",False,"center", font=("Times",18,"bold"))
        print(sq())

#문제 2->3


screen = turtle.Screen()
image1 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\검은고양이.gif"
screen.addshape(image1)
image2 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\수상한사람.gif"
screen.addshape(image2)
image3 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\하얀고양이.gif"
screen.addshape(image3)
t3.shape(image3)#이미지변환
t3.stamp()

t2.write("[나]   \n계속 세 갈림길이네..",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n첨성대까지 가는 길이 맞긴 한 걸까?",False,"center",font=("Times",18,"bold"))
print(sq())
t2.write("[행복한 고양이]   \n첨성대라면 내가 길을 알고 있다냥!",False,"center",font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n 헉!!! 제발 알려주세요!!!!!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[행복한 고양이]   \n그렇다면 냥냥이의 수수께끼를 맞혀보라냥!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[행복한 고양이]   \n만약 맞힌다면 목적지까지 가는 지름길을 알려주겠다냥!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n 좋아요!!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[행복한 고양이]   \n그럼 문제 나간다냥!",False,"center", font=("Times",18,"bold"))
print(sq())


#수수께끼 문제
while True:
    n=numinput("문제", "다음 문제에 대한 답을 보기에서 고르세요\n▶대학생이 가장 좋아하는 동네는?\n 1.마장동\n 2.서교동\n 3.명동\n 4.방학동\n 5.역곡동\n(ex: 1(숫자만 입력할 것))")
    if n==4:
        t2.write("[행복한 고양이]   \n정답이다냥! \n지름길은 왼쪽에서 두번째 길이다냥!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    elif n!=4:
        t2.write("[행복한 고양이]   \n다시 풀어봐라냥!",False,"center", font=("Times",18,"bold"))
        print(sq())

while True:
    n=numinput("길을 선택하세요", "왼쪽부터 몇 번째 길로 갈지 선택하세요.\n(ex: 1(숫자만 입력할 것))")
    if n==2:
        t2.write("[행복한 고양이]   \n잘 했다냥! \n행운을 빌어주겠다냥!!",False,"center", font=("Times",18,"bold"))
        print(sq())
        break
    if n!=2:
        t2.write("[행복한 고양이]   \n 내가 알려준 길은 이 길이 아니다냥!!!",False,"center", font=("Times",18,"bold"))
        print(sq())


screen = turtle.Screen()
image1 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\검은고양이.gif"
screen.addshape(image1)
image2 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\수상한사람.gif"
screen.addshape(image2)
image3 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\하얀고양이.gif"
screen.addshape(image3)
image4 = "C:\\Users\\수정\\Desktop\\플젝\\우수정\\점.gif"
screen.addshape(image4)
t3.shape(image4)#이미지변환
t3.stamp()

#갈림길->노을들판
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgpic("C:\\Users\\수정\\Desktop\\플젝\\우수정\\들판1.gif")
screen.update()   #노을이 배경으로 뜸
t1.speed(10) #나중에 speed 삭제하기

#엔딩 최종본
import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
tt1=turtle.Turtle()

t2.pencolor("white")    
t2.write("......!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("지금 시각은 6시 50분...",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("무사히 도착했다....!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("아름다운 노을을 볼 수 있게 되어서 다행이야!",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("오늘은 행운이 많이 따른 기분좋은 하루였어.",False,"center", font=("Times",18,"bold"))
print(sq())



screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgpic("C:\\Users\\수정\\Desktop\\플젝\\우수정\\들판1.gif")
screen.update()   #노을이 배경으로 뜸
tt1.speed(10) #속도를 빠르게!

def bd1():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(80)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(80)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(80)
    tt1.hideturtle()
    t2.hideturtle()
def bd2():
    tt1.down()
    tt1.color('black','gray')
    tt1.begin_fill()
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(40)
    tt1.hideturtle()
    t2.hideturtle()
def bd3():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(16)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(8)
    tt1.left(75)
    tt1.forward(40)
    tt1.left(105)
    tt1.end_fill()
    tt1.up()
    tt1.forward(16)
    tt1.hideturtle()
    t2.hideturtle()
def bd4():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(16)
    tt1.left(105)
    tt1.forward(40)
    tt1.left(75)
    tt1.forward(8)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(16)
def bd5():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(80)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(80)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(80)
    tt1.hideturtle()
    t2.hideturtle()
def bd6():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(89)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(89)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(89)
    tt1.hideturtle()
    t2.hideturtle()
def bd7():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(98)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(98)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(98)
    tt1.hideturtle()
    t2.hideturtle()
def bd8():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(107)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(107)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(107)
    tt1.hideturtle()
    t2.hideturtle()
def bd9():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(116)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(116)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(116)
    tt1.hideturtle()
    t2.hideturtle()
def bd10():
    tt1.down()
    tt1.color('black','darkgray')
    tt1.begin_fill()
    tt1.forward(20)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.forward(20)
    tt1.left(90)
    tt1.forward(40)
    tt1.left(90)
    tt1.end_fill()
    tt1.up()
    tt1.forward(20)
    tt1.hideturtle()
    t2.hideturtle()



tt1.up()
tt1.goto(-290,300)
tt1.down()
print(bd1())
tt1.down()
tt1.color('black','gray')
tt1.begin_fill()
tt1.forward(280)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.forward(280)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.end_fill()
tt1.up()
tt1.forward(280)
print(bd1())


tt1.up()
tt1.goto(-290,260)
tt1.down()
print(bd1())
tt1.down()
tt1.color('black','gray')
tt1.begin_fill()
tt1.forward(280)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.forward(280)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.end_fill()
tt1.up()
tt1.forward(280)
print(bd1())

tt1.up()
tt1.goto(-290,220)
tt1.down()
print(bd2(),bd1(),bd1(),bd2(),bd1(),bd1(),bd2())
tt1.up()
tt1.goto(-290,180)
tt1.down()
print(bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1())
tt1.up()
tt1.goto(-290,140)
tt1.down()
print(bd2(),bd1(),bd1(),bd2(),bd1(),bd1(),bd2())
tt1.up()
tt1.goto(-290,100)
tt1.down()
print(bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1())

tt1.up()
tt1.goto(-302,60)
tt1.down()
print(bd3(),bd5(),bd2(),bd1(),bd2(),bd1(),bd2(),bd5(),bd4())

tt1.up()
tt1.goto(-310,20)
tt1.down()
print(bd3(),bd6(),bd2(),bd1(),bd2(),bd1(),bd2(),bd6(),bd4())

tt1.up()
tt1.goto(-316,-20)
tt1.down()
print(bd3(),bd7(),bd2(),bd1(),bd2(),bd1(),bd2(),bd7(),bd4())

tt1.up()
tt1.goto(-324,-60)
tt1.down()
print(bd3(),bd8(),bd2(),bd1(),bd2(),bd1(),bd2(),bd8(),bd4())

tt1.up()
tt1.goto(-328,-100)
tt1.down()
print(bd3(),bd9(),bd2(),bd1(),bd2(),bd1(),bd2(),bd9(),bd4())


tt1.up()
tt1.goto(-328,-140)
tt1.down()
print(bd10(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2())

tt1.up()
tt1.goto(-328,-180)
tt1.down()
print(bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd10())

tt1.up()
tt1.goto(-328,-220)
tt1.down()
print(bd10(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2())

tt1.up()
tt1.goto(-328,-260)
tt1.down()
print(bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd10())

tt1.up()
tt1.goto(-328,-300)
tt1.down()
print(bd10(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2())

tt1.up()
tt1.goto(-328,-340)
tt1.down()
print(bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd10())

tt1.up()
tt1.goto(-328,-380)
tt1.down()
print(bd10(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2())

tt1.up()
tt1.goto(-328,-420)
tt1.down()
print(bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd1(),bd2(),bd10())


tt1.up()
tt1.goto(-120,60)
tt1.down()
tt1.color('black')
tt1.begin_fill()
tt1.forward(100)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.forward(100)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.end_fill()
tt1.up()
tt1.forward(40)
tt1.up()
tt1.goto(-120,20)
tt1.down()
tt1.color('black')
tt1.begin_fill()
tt1.forward(100)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.forward(100)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.end_fill()
tt1.up()
tt1.forward(40)


tt1.up()
tt1.goto(-290,300)
tt1.down()
print(bd1())
tt1.down()
tt1.color('black','gray')
tt1.begin_fill()
tt1.forward(280)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.forward(280)
tt1.left(90)
tt1.forward(40)
tt1.left(90)
tt1.end_fill()
tt1.hideturtle()
t2.hideturtle()

t1.speed(1)
t2.reset()
t2.pencolor("white")
t2.write("[나]   \n노을 지는 풍경 속의 다보탑은 정말 아름다워",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n이 광경을 놓치지 않게 되어서 다행이야",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]   \n정말이지, 오늘은 행운이 많이 따른 기분좋은 하루였어.",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]는 눈앞의 풍경을 기억 속에 온전히 새겨넣고 싶었다.",False,"center", font=("Times",18,"bold"))
print(sq())
t2.write("[나]는 눈앞의 풍경을 마음 속에 한껏 담고는 눈을 감았다.",False,"center", font=("Times",18,"bold"))
print(sq())
tt1.clear() 
t2.clear()
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgpic("C:\\Users\\수정\\Desktop\\플젝\\우수정\\검정1.gif")
screen.update()   #노을이 배경으로 뜸

tt1.speed(1)
t1.speed(1)
t2.pencolor("white")
t2.write("THE\nEND",False,"center", ("Times",18,"bold"))
print(sq())


