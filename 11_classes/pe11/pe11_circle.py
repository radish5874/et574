class Circle:
    def __init__(cir,cir_R):
        cir.cir_R=cir_R
    def setRadius(cir,radius):
        cir.cir_R=radius
    def desplay(cir):
        print(cir.cir_R)

def main():
        newCir=Circle(12)
        newCir.desplay()
main()

