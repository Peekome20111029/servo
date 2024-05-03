def on_button_pressed_a():
    global oislkdncrhyseiu
    oislkdncrhyseiu += 25
    servos.P0.set_angle(oislkdncrhyseiu + 10)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global oislkdncrhyseiu
    oislkdncrhyseiu += -25
    servos.P0.set_angle(oislkdncrhyseiu - 10)
input.on_button_pressed(Button.B, on_button_pressed_b)

oislkdncrhyseiu = 0
oislkdncrhyseiu = 90