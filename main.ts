input.onButtonPressed(Button.A, function () {
    Tall = randint(0, 1000)
    sevenSegment.writeNumber(Tall)
})
let Tall = 0
sevenSegment.startSevenSegPin0()
basic.pause(100)
sevenSegment.clear()
