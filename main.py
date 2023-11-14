def on_button_pressed_a():
    global Tall
    Tall = randint(0, 1000)
    sevenSegment.write_number(Tall)
input.on_button_pressed(Button.A, on_button_pressed_a)

Tall = 0
sevenSegment.start_seven_seg_pin0()
basic.pause(100)
sevenSegment.clear()