class Ninja:

    weapon_list = ["sword", "stick", "star"]

    def __init__( self , name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate, tool ):
        if tool == "sword":
            pirate.health -= self.strength + 10
        return self



