def on_button_pressed_a():
    led.plot(0, 0)
    led.set_brightness(255)
    radio.set_group(64)
    for index in range(4):
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_number(1)

def on_forever():
    pass
basic.forever(on_forever)
