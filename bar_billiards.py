class score:
    def __init__(self, player_name):
        self.player = player_name
        self.score = 0
        self.score_break = 0
    
    def __repr__(self):
        return f"{self.player}: {self.score}"

    def __lt__(self, other):
        return self.score < other.score

scores = []

while True:
    player_name = input(f"Enter player {len(scores)+1} name: ")
    if not player_name:
        break
    scores.append(score(player_name))

turn = 0

while True:
    cur_turn = turn % len(scores)
    print("Player", scores[cur_turn].player)
    points = input(f"Points ({scores[cur_turn].score_break}): ")
    while points:
        if int(points) == 0:
            scores[cur_turn].score_break = 0
            break
        scores[cur_turn].score_break += int(points)
        points = input(f"Points ({scores[cur_turn].score_break}): ")
    scores[cur_turn].score += scores[cur_turn].score_break
    scores[cur_turn].score_break = 0
    print(scores)
    turn += 1
