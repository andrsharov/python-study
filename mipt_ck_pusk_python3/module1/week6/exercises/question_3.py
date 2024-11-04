class Player:
    id: int
    name: str
    scores: int = 0
    games: list = []

    def __init__(self, id: int, name: str,) -> None:
        self.id: int = id
        self.name: str = name

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores

    def get_mean(self) -> float:
        return self.scores / len(self.games)

class Power:

    def __init__(self, name: str, cost: int) -> None:
        self.name: str = name
        self.cost: int = cost

    def use(self, player):
        ...

class PhysicalPower(Power):

    def __init__(self, name: str, cost: int, count: int) -> None:
        super().__init__(name, cost)
        self.count: int = count

    def use(self, player):
        if self.count >= 1:
            print(f"{player.name} used {self.name}")
        else:
            print(f"{player.name} cannot use {self.name}")
        self.count -= 1

class MagicPower(Power):

    def __init__(self, name: str, cost: int) -> None:
        super().__init__(name, cost)

    def use(self, player):
        print(f"{player.name} used {self.name}")
        player.scores += 1


p = Player(1, 'Bilbo')
t = PhysicalPower('teleport', 10, count=1)
t.use(p)
t.use(p)
print(p.scores)


b = MagicPower('black magic', 200)
b.use(p)
print(p.scores)
b.use(p)
print(p.scores)
