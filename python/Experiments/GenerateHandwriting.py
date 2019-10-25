


hand = Hand()

# usage demo
lines = [
    "1234567890",
]
biases = [.95 for i in lines]
styles = [9 for i in lines]
stroke_colors = ['black']
stroke_widths = [1]

hand.write(
    filename='img/AccNo.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)

