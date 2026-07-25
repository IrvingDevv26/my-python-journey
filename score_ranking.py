# Fifty-second program: Given a list of scores, display them sorted from
# highest to lowest, numbered as a ranking (e.g. "1st place: 92"). sorted with
# reverse=True orders them descending, and enumerate(..., start=1) adds the
# ranking position.

scores = [45, 92, 78, 63, 88, 71]

print("---Ranking---")
for position, score in enumerate(sorted(scores, reverse=True), start=1):
    print(f"Place {position}: {score}")
