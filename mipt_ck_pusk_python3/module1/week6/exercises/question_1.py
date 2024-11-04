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

# Блок ниже нужен только для проверки работы функции, вставлять в ответ его не нужно
p = Player(1, 'Bilbo')
print(p.id)
print(p.name)
print(p.scores)
print(p.games)
p.add_result(15, 10)
p.add_result(21, 5)
print(p.scores)
print(p.games)
print(p.get_mean())