
inventar = {
            "rope" : 1,
            "gold coin" : 42,
            "dagger" : 1,
            "arrow" : 12,
            "torch" : 6,
            }

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

class SpielFigur():
    def __init__(self, invent) -> None:
        self.invent = invent
    
    def displayInventory(self):
        print("Inventar-Inhalt:")
        summe = 0
        for k, v in self.invent.items():
            print(str(v)+ " " + k)
            summe = summe + v
        print(f"Summe Gegenstände: {summe}")
    
    def add_to_inventar(self,loot):
        for i in loot:
            self.invent[i] = self.invent.get(i, 0) +1
                
            
player1 = SpielFigur(inventar)
player1.add_to_inventar(dragonLoot)
player1.displayInventory()