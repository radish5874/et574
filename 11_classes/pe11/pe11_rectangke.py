class Rectangke:
    def __intit__(rec,rec_L,rec_W):
        rec.rec_L=rec_L
        rec.rec_W=rec_W
        
    def setWidth(rec,width):
        rec.rec_W=width
    
    def setLength(rec,length):
        rec.rec_L=length
    
    def getWidth(rec):
        print(rec.rec_W)

    def getLength(rec):
        print(rec.rec_L)

    def area(rec):
        print(rec.rec_L*rec.rec_W)
    
def main():
    newREC=Rectangke(12,6)
    newREC.getLength()
    newREC.getWidth()
    newREC.area()

main()
