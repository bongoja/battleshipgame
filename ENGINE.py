
import random
class Ship:
    def __init__(self, size):
        self.row = random.randrange(0,9)
        self.col = random.randrange(0,9)
        self.size = size
        self.orientation = random.choice(["h", "v"])
        self.indexes = self.compute_indexes()
    
    def compute_indexes(self):
        start_index = self.row * 10 + self.col
        if self.orientation == "h":
            #zwracamy listę, jezeli size jest rowny 3, dodalibyśmy 0,1,2 do indexu początkowego a to byłaby lista indexow, które określają gdzie znajduje się statek
            return [start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start_index + i * 10 for i in range(self.size)]
        
class Player:
    def __init__(self):
        self.ships = []
        self.search = ["U" for i in range(100)] #u for unknown
        self.place_ships(sizes = [5,4,3,3,2])
        lists_of_lists_of_indexes = [ship.indexes for ship in self.ships]
        print(lists_of_lists_of_indexes)

    def place_ships(self, sizes):
        for size in sizes:
            placed = False
            while not placed:
                #utwórz nowy statek
                ship = Ship(size)
            #sprawdź czy umieszczenie jest mozliwe
                possible = True
                for i in ship.indexes: 
                #indexy muszą być mniejsze od 100
                    if i >= 100:
                        possible = False
                    break
            #statki nie mogą się zachowywać jak Snake
                new_row = i // 10
                new_col = i % 10
                if new_row != ship.row and new_col != ship.col:
                    possible == False
                    break
            #statki nie mogą się przecinać:
            for other_ship in self.ships:
                #wiemy ze jest zajety przez inny statek
                    if i in other_ship.indexes:
                        possible = False
                        break
            #umieść statek
        if possible:
            self.ships.append(ship)
            placed = True
    
    def show_ships(self):
        indexes = []


            
p=Player()
print(p.lists_of_lists_of_indexes)






