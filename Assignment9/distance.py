class Distance:
    def get_distance(self):
        dist=int(input("Enter the distance in km: "))
        self.dist=dist
    def print_distance(self):
        print("distance in metres: ",self.dist*1000)

d=Distance()
d.get_distance()
d.print_distance()






