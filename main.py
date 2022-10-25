from turtle import Screen
from time import sleep
from Locations import check_close, grid_system, delete_row, go_down_first, go_down_second, go_down_third
from Locations import go_down_fourth, go_down_fifth, go_down_sixth, go_down_seventh, go_down_eighth
from Locations import go_down_ninth, go_down_tenth
from Border import SideBorder, BottomBorder, GridLines, CrossLine
from Score_Counter import Tracker
from Figure_class import AvailableFigures


# prepare screen:
screen = Screen()
screen.setup(width=480, height=600)
screen.bgcolor("dark cyan")
screen.title("Tetris Game")
screen.tracer(0)

# create painter and tracker:
border = SideBorder()
border.draw_borders()
tracker = Tracker()
tracker.write_score()

# create bottom line:
bottom = BottomBorder()
bottom.deploy_floor()

# create cross sign:
cross = CrossLine()
cross.draw_sign()

# create grid lines:
grid = GridLines()
grid.draw_verticals()
grid.draw_horizontals()

# create shapes:
figure = AvailableFigures()

# listen commands:
screen.listen()
screen.onkey(figure.move_left, "a")
screen.onkey(figure.move_right, "d")

screen.update()
play = True
while play:
    sleep(0.1)
    screen.update()
    figure.move_down()
    if figure.figure_list[0][0].ycor() - 20 <= -260 or figure.figure_list[0][-1].ycor() - 20 <= -260:
        for item in figure.figure_list[0]:
            figure.trash_list.append(item)
        figure.figure_list = []
        figure.create_figure()

    if check_close(figure.figure_list[0][0], figure.trash_list) or \
            check_close(figure.figure_list[0][1], figure.trash_list) or \
            check_close(figure.figure_list[0][2], figure.trash_list) or \
            check_close(figure.figure_list[0][3], figure.trash_list):
        for item in figure.figure_list[0]:
            figure.trash_list.append(item)
        figure.figure_list = []
        figure.create_figure()

    # check about fill rows and clear it:
    first_row = []
    control_1 = delete_row(figure.trash_list, grid_system["first"], first_row)
    if control_1 == 10:
        for item in first_row:
            item.goto(500, -500)
        go_down_first(figure.trash_list)
        tracker.current_score += 10
    # second: -----------------------------------------------------------
    second_row = []
    control_2 = delete_row(figure.trash_list, grid_system["second"], second_row)
    if control_2 == 10:
        for item in second_row:
            item.goto(500, -500)
        go_down_second(figure.trash_list)
        tracker.current_score += 10
    # third: -----------------------------------------------------------
    third_row = []
    control_3 = delete_row(figure.trash_list, grid_system["third"], third_row)
    if control_3 == 10:
        for item in third_row:
            item.goto(500, -500)
        go_down_third(figure.trash_list)
        tracker.current_score += 10
    # fourth: -----------------------------------------------------------
    fourth_row = []
    control_4 = delete_row(figure.trash_list, grid_system["fourth"], fourth_row)
    if control_4 == 10:
        for item in fourth_row:
            item.goto(500, -500)
        go_down_fourth(figure.trash_list)
        tracker.current_score += 10
    # fifth: -----------------------------------------------------------
    fifth_row = []
    control_5 = delete_row(figure.trash_list, grid_system["fifth"], fifth_row)
    if control_5 == 10:
        for item in fifth_row:
            item.goto(500, -500)
        go_down_fifth(figure.trash_list)
        tracker.current_score += 10
    # sixth: -----------------------------------------------------------
    sixth_row = []
    control_6 = delete_row(figure.trash_list, grid_system["sixth"], sixth_row)
    if control_6 == 10:
        for item in sixth_row:
            item.goto(500, -500)
        go_down_sixth(figure.trash_list)
        tracker.current_score += 10
    # seventh: -----------------------------------------------------------
    seventh_row = []
    control_7 = delete_row(figure.trash_list, grid_system["seventh"], seventh_row)
    if control_7 == 10:
        for item in seventh_row:
            item.goto(500, -500)
        go_down_seventh(figure.trash_list)
        tracker.current_score += 10
    # eighth: -----------------------------------------------------------
    eighth_row = []
    control_8 = delete_row(figure.trash_list, grid_system["eighth"], eighth_row)
    if control_8 == 10:
        for item in eighth_row:
            item.goto(500, -500)
        go_down_eighth(figure.trash_list)
        tracker.current_score += 10
    # ninth: -----------------------------------------------------------
    ninth_row = []
    control_9 = delete_row(figure.trash_list, grid_system["ninth"], ninth_row)
    if control_9 == 10:
        for item in ninth_row:
            item.goto(500, -500)
        go_down_ninth(figure.trash_list)
        tracker.current_score += 10
    # tenth: -----------------------------------------------------------
    tenth_row = []
    control_10 = delete_row(figure.trash_list, grid_system["tenth"], tenth_row)
    if control_10 == 10:
        for item in tenth_row:
            item.goto(500, -500)
        go_down_tenth(figure.trash_list)
        tracker.current_score += 10

    tracker.write_score()
    for item in figure.trash_list:
        if item.ycor() > 190:
            tracker.game_over()
            play = False

screen.exitonclick()
