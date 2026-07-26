# Fifty-fifth program: A player has scores from two rounds. Use zip together
# with enumerate to show, shot by shot: the shot number, each round's score,
# and which round was better (or if it was a tie). At the end, state in how
# many shots the player improved in round 2. The pattern
# "for i, (p1, p2) in enumerate(zip(a, b), start=1)" unpacks the shot number
# and both scores at once.

round1 = [10, 15, 8, 20, 12]
round2 = [12, 10, 15, 18, 20]

improvements = 0
for shot, (score1, score2) in enumerate(zip(round1, round2), start=1):
    if score2 > score1:
        result = "round 2 was better"
        improvements += 1
    elif score1 > score2:
        result = "round 1 was better"
    else:
        result = "tie"
    print(f"Shot {shot}: round 1 = {score1}, round 2 = {score2} -> {result}")

print(f"\nThe player improved in {improvements} shots in round 2")
