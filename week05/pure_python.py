f = open("scores.csv", "r",
         encoding="utf-8")
lines = f.readlines()
f.close()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0
total = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        continue
    category = parts[cat_idx]
    if category not in total:
        total[category] = 0
        counts[category] = 0
    total[category] += score
    counts[category] += 1

    count += 1

for c in sorted(total.keys()):
    avg = total[c] / counts[c]
    print(c, round(avg,2))

