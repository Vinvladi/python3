import graphics as gr
def build_house (window, upper_left_corner, width):
    height = calculate_height (width)

window = gr.GraphWin ("Russian game",300,100)
build_house (window,gr.Point(100,100),100)

print ("Ура! Дом построен")
#Программа консинстентна