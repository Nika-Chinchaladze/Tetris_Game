def check_close(concrete, basic_list):
    for item in basic_list:
        if (concrete.ycor() - 40 == item.ycor()) and (concrete.xcor() == item.xcor()):
            return True


def delete_row(list_trash, list_grid, empty_list):
    empty_list.clear()
    variable = 0
    for trash in list_trash:
        for grid in list_grid:
            if trash.position() == grid:
                variable += 1
                empty_list.append(trash)
    return variable


grid_system = {
    "first": [(-180, -240), (-140, -240), (-100, -240), (-60, -240), (-20, -240), (20, -240), (60, -240), (100, -240),
              (140, -240), (180, -240)],
    "second": [(-180, -200), (-140, -200), (-100, -200), (-60, -200), (-20, -200), (20, -200), (60, -200), (100, -200),
               (140, -200), (180, -200)],
    "third": [(-180, -160), (-140, -160), (-100, -160), (-60, -160), (-20, -160), (20, -160), (60, -160), (100, -160),
              (140, -160), (180, -160)],
    "fourth": [(-180, -120), (-140, -120), (-100, -120), (-60, -120), (-20, -120), (20, -120), (60, -120), (100, -120),
               (140, -120), (180, -120)],
    "fifth": [(-180, -80), (-140, -80), (-100, -80), (-60, -80), (-20, -80), (20, -80), (60, -80), (100, -80),
              (140, -80), (180, -80)],
    "sixth": [(-180, -40), (-140, -40), (-100, -40), (-60, -40), (-20, -40), (20, -40), (60, -40), (100, -40),
              (140, -40), (180, -40)],
    "seventh": [(-180, 0), (-140, 0), (-100, 0), (-60, 0), (-20, 0), (20, 0), (60, 0), (100, 0), (140, 0), (180, 0)],
    "eighth": [(-180, 40), (-140, 40), (-100, 40), (-60, 40), (-20, 40), (20, 40), (60, 40), (100, 40), (140, 40),
               (180, 40)],
    "ninth": [(-180, 80), (-140, 80), (-100, 80), (-60, 80), (-20, 80), (20, 80), (60, 80), (100, 80), (140, 80),
              (180, 80)],
    "tenth": [(-180, 120), (-140, 120), (-100, 120), (-60, 120), (-20, 120), (20, 120), (60, 120), (100, 120),
              (140, 120), (180, 120)]
}


def go_down_first(basic_list):
    for item in basic_list:
        x_point = item.xcor()
        y_point = item.ycor()
        item.goto(x_point, y_point - 40)


def go_down_second(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > -200:
            item.goto(x_point, y_point - 40)


def go_down_third(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > -160:
            item.goto(x_point, y_point - 40)


def go_down_fourth(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > -120:
            item.goto(x_point, y_point - 40)


def go_down_fifth(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > -80:
            item.goto(x_point, y_point - 40)


def go_down_sixth(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > -40:
            item.goto(x_point, y_point - 40)


def go_down_seventh(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > 0:
            item.goto(x_point, y_point - 40)


def go_down_eighth(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > 40:
            item.goto(x_point, y_point - 40)


def go_down_ninth(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > 80:
            item.goto(x_point, y_point - 40)


def go_down_tenth(whole_list):
    for item in whole_list:
        x_point = item.xcor()
        y_point = item.ycor()
        if y_point > 120:
            item.goto(x_point, y_point - 40)
