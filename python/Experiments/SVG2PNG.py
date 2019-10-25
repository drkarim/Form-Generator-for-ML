

from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

CairoSVG.svg2pdf(url='JDoe.svg', write_to='JDoenew.pdf')

drawing = svg2rlg("Images/svgtopng/City.svg")
renderPM.drawToFile(drawing, "JDoenew.png", fmt="PNG")