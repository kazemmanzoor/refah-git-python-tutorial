
class Planet:
    def __init__(self, name, diameter, dist, year, material, nofmoon):
    
        self.name = name
        self.dia  = diameter
        self.dist = dist
        self.year = year
        self.mat  = material
        self.moon = nofmoon

	def display1(self):
        print("\nPlanet: Name\t", self.name, "Diameter(km)\t", self.dia, "Distance to Sun(km)\t", self.dist, "Year\t", self.year, "Material\t", self.mat, "Number of moons\t", self.moon)

atarod	= Planet("\nAtarod\t", "4879\t", "57909227\t", "88\t", "sangi\t", "0\t")
zohre	= Planet("\nZohre\t", "12104\t", "108209475\t", "225\t", "sangi\t", "0\t")
zamin	= Planet("\nZamin\t", "12742\t", "149598262\t", "365.24\t", "sangi\t", "1\t")
merikh	= Planet("\nMerikh\t", "6779\t", "227943824\t", "1.9\t", "sangi\t", "2\t")
moshtari= Planet("\nMoshtari\t", "139822\t", "778340821\t", "11.9\t", "gazi\t", "84\t")
zohal	= Planet("\nZohal\t", "116464\t", "1426666422\t", "29.5\t", "gazi\t", "83\t")
oranus	= Planet("\nOranus\t", "50724\t", "2870658186\t", "84\t", "gazi\t", "27\t")
nepton	= Planet("\nNepton\t", "49244\t", "4498396441\t", "164.8\t", "gazi\t", "14\t")



        
class Moon(Planet):
    def display2(self):
        print("\n\n\nMoon: Name\t", self.name, "Diameter(km)\t", self.dia, "Distance to Earth(km)\t", self.dist, "Year\t", self.year)

m = Moon("\nMoon\t","3474.8\t", "384400\t", "1 day")


atarod.dosply1()
zohre.dosply1()
zamin.dosply1()
moshtari.dosply1()
zohal.dosply1()
oranus.dosply1()
nepton.dosply1()

m.display2()
