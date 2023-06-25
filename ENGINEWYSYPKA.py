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
            return [start_index + i for i in range(self.size)]
        elif self.orientation == "v":
            return [start_index + i*10 for i in range(self.size)]
        

class Player:
    def __init__(self):
        self.ships = []
        self.search = ["U" for i in range(100)] # u for "unknown"
        self.place_ships(sizes = [5,4,3,3,2])
        lists_of_lists = [ship.indexes for ship in self.ships]
        self.indexes = [index for sublist in lists_of_lists for index in sublist]
    
    def place_ships(self, sizes):
        for size in sizes:
            placed = False
            while not placed:

                #swtórz nowy statek
                ship = Ship(size)

                #sprawdzanie czy umieszczenie jest mozliwe:
                possible = True
                for i in ship.indexes:
                    #indexy muszą być mniejsze niz 100
                    if i >= 100:
                        possible = False
                        break
                    #statki nie mogą zachowywać się jak snake
                    new_row = i // 10
                    new_col = i % 10
                    if (new_row != ship.row and new_col != ship.col) or (new_row >= 10 or new_col >= 10):
                        possible = False
                        break
                    #statki nie mogą na siebie nachodzić
                    for other_ship in self.ships:
                        if i in other_ship.indexes:
                            possible =  False
                            break
                #umieść statek
                if possible:
                    self.ships.append(ship)
                    placed = True

    def show_ships(self):
        indexes = ["-" if i not in self.indexes else "X" for i in range(100)]
        for row in range(10):
            print(" ".join(indexes[(row-1)*10:row*10]))


class Game:
    def __init__(self, human1, human2):
        self.human1 = human1
        self.human2 = human2
        self.player1 = Player()
        self.player2 = Player()
        self.player1_turn = True
        # automatyzacja gry z komuterem True dla komputera kiedy False dla gracza
        self.computer_turn = True if not self.human1 else False
        self.over = False
        self.result = None
        self.n_shots = 0

    def make_move(self, i):
        player = self.player1 if self.player1_turn else self.player2
        opponent = self.player2 if self.player1_turn else self.player1
        hit = False

        # set miss "M" or hit "H"
        if i in opponent.indexes:
            player.search[i] = "H"
            hit = True
            # check if ship is sunk ("S")
            for ship in opponent.ships:
                sunk = True 
                for i in ship.indexes:
                    if player.search[i] == "U":
                        sunk = False
                        break
                if sunk:
                    for i in ship.indexes:
                        player.search[i] =  "S"
        else:
            player.search[i] = "M"

        # check if game over
        game_over = True
        for i in opponent.indexes:
            if player.search[i] == "U":
                game_over = False
        self.over = game_over
        self.result = 1 if self.player1_turn else 2

        # change the active player
        if not hit:
            self.player1_turn = not self.player1_turn

            # switch between human and computer turns
            if (self.human1 and not self.human2) or (not self.human1 and self.human2):
                self.computer_turn = not self.computer_turn
        # add to the number of shots fired
        self.n_shots += 1

    def random_ai(self):
        search = self.player1.search if self.player1_turn else self.player2.search
        unknown = [i for i, square in enumerate(search) if square == "U"]
        if len(unknown) > 0:
            random_index = random.choice(unknown)
            self.make_move(random_index)
   
   
    #Basic ai
    def ai(self):
        #setup
        search = self.player1.search if self.player1_turn else self.player2.search
        niewiadome = [i for i, square in enumerate(search) if square == "U"]
        trafienia = [i for i, square in enumerate(search) if square == "H"]
     #1.search in neighborhood of trafienia 
        niewiadome_z_sasiednimi_trafieniami = []  # lista plytek (te najblizsze) od uderzenia
        niewiadome_z_sasiednimi_trafieniami2 = [] # lista  drugich plytek  od uderzenia
        
      
        for n in niewiadome:
            #wyszukiwanie najblizszych plytek
            if n+1 in trafienia or n-1 in trafienia or n-10 in trafienia or n+10 in trafienia:
                niewiadome_z_sasiednimi_trafieniami.append(n) #kopiowanie plytek do listy (level-1)
            
            #wyszukiwanie co drugiej plytki
            if n+2 in trafienia or n-2 in trafienia or n-20 in trafienia or n+20 in trafienia:
                niewiadome_z_sasiednimi_trafieniami2.append(n) #kopiowanie co drugiej plyteki do listy (level-2)
         
         # 1.1 pick "U" square with direct and level-2 neighbor both marked as"H"
            for n in niewiadome: 
                if n in niewiadome_z_sasiednimi_trafieniami and n in niewiadome_z_sasiednimi_trafieniami2:
                    self.make_move(n) #robi ruchy po plytkach (level-1 ilevel-2 wokol trafienia 
                    return


         # 1.1 pick "U" square that has a level-1 neighbors marked as "H"
            if len(niewiadome_z_sasiednimi_trafieniami) > 0 :  
                self.make_move(random.choice(niewiadome_z_sasiednimi_trafieniami)) #robi ruchy po plytkach wokol (level-1)
                return 
        #2.checker board pattern - sprawdza co dwa - chyba ???
        co_drugi_element_lista = []
        row = n//10 #dzielenie całkowitoliczbowe - np 5 // 2 daje wynik 2, normalnie 2.5. | w tym wypadku chcemy uzyskac numer wiersza w ktorym znajduje sie unknow (pozycja pionowa)

        col = n % 10 #modulo - reszta z dzielenia | kolumna w ktorej jest uknown (pozycja pozioma) Indeksy na planszy o wymiarach 10x10 są liczone od 0 do 99, a dzięki temu obliczeniu można uzyskać numer kolumny od 0 do 9.
        if (row + col) % 2 == 0: #warunkuje zaznaczenie co 2
            co_drugi_element_lista.append(n) #kopiuje co drugi kafel do co_drugi_element_lista
        if len(co_drugi_element_lista)>0: 
            self.make_move(random.choice(co_drugi_element_lista)) #robi ruchy po tej liście
            return
        #3.random move
        self.random_ai()



p = Player()
p.show_ships()

