input.onButtonPressed(Button.A, function () {
    led.plot(0, 0)
    led.setBrightness(255)
    radio.setGroup(64)
    for (let index = 0; index < 4; index++) {
        music.changeTempoBy(20)
    }
})
basic.showNumber(1)
basic.forever(function () {
	
})
