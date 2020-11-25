# from turtle import *
# from random import *
# from colorgram import *
# jimmy = Turtle()
# screen = Screen()
# screen.setup()

# # print(colors_project)
# #
# # def random_color ():
# #     a = randint(1, 255)
# #     b = randint(1, 255)
# #     c = randint(1, 255)
# #     color = (a, b, c)
# #     return color

# colormode(255)
# # for _ in range(4):
# #     jimmy.forward(100)
# #     jimmy.left(90)
# #
# #
# # for _ in range(20):
# #     jimmy.forward(10)
# #     jimmy.color("White")
# #     jimmy.forward(10)
# #     jimmy.color("Black")
# #
# # colors = ["red", "blue", "green","orange", "purple", "grey"]
# # def draw (angles):
# #     # if angles == 4 or angles == 7:
# #     #     jimmy.color("red")
# #     # elif angles == 5 or angles ==8:
# #     #     jimmy.color("blue")
# #     # else:
# #     #     jimmy.color("black")
# #     corner = 360/angles
# #     for _ in range(angles):
# #         jimmy.forward(100)
# #         jimmy.left(corner)

# #
# # for shapes in (range (3,10)):
# #     jimmy.color(choice(colors))
# #     draw(shapes)
# # #
# # for _ in range(20):
# #     jimmy.forward(10)
# #     jimmy.penup()
# #     jimmy.forward(10)
# #     jimmy.pendown()

# # # direction=[0,90,180,270]
# # #
# # jimmy.speed("fastest")
# # jimmy.pensize(3)
# # turn = [jimmy.left(90), jimmy.right(90), jimmy.forward(15) ]
# # jimmy.pensize(10)
# # # print(colors1)
# # while True:
# #     colors1 = random_color()
# #     jimmy.forward(30)
# #     jimmy.setheading(choice(direction))
# #     jimmy.pencolor(colors1)
# #
# #
# #
# # def draw_spirograph(size):
# #     for _ in (range(int(360/size))):
# #         colors=random_color()
# #         jimmy.circle(100)
# #         jimmy.setheading(jimmy.heading()+10)
# #         jimmy.color(colors)
# #
# # draw_spirograph(5)
# # rgb_colors=[]
# # colors_project = extract("20120116-141025.jpg", 30)
# # for color in colors_project:
# #     red = color.rgb.r
# #     blue = color.rgb.b
# #     green = color.rgb.g
# #     new_color = (red, green, blue)
# #     rgb_colors.append(new_color)
# #
# # print (rgb_colors)

# color_list = [(199, 145, 108), (53, 102, 128), (170, 78, 41), (120, 165, 195), (108, 77, 97), (38, 116, 85),
#               (181, 141, 159), (178, 151, 21), (68, 28, 37), (87, 29, 17), (133, 169, 122), (108, 31, 47),
#               (122, 40, 27), (112, 117, 172), (224, 214, 131), (86, 148, 161), (229, 175, 169), (164, 108, 133),
#               (43, 47, 50), (66, 172, 118), (174, 203, 179), (32, 91, 82), (198, 93, 65), (59, 61, 60), (207, 181, 190), (181, 189, 209)]
# jimmy.speed("fastest")
# jimmy.penup()
# start_postion_x= -150
# start_position_y = -250
# jimmy.setposition(start_postion_x, start_position_y)
# jimmy.pendown()

# jimmy.setposition(start_postion_x, start_position_y)

#     # if _%10 == 0:
#     #     jimmy.penup()
#     #     jimmy.setposition(start_postion_x, start_position_y )
#     #     jimmy.pendown()
# for _ in range (10):
#     jimmy.penup()
#     start_position_y +=50
#     jimmy.setposition(start_postion_x, start_position_y)
#     jimmy.pendown()
#     for _ in range (9):
#         jimmy.color(choice(color_list))
#         jimmy.begin_fill()
#         jimmy.circle(20)
#         jimmy.end_fill()
#         jimmy.penup()
#         jimmy.forward(50)
#         jimmy.pendown()



# screen.exitonclick()
