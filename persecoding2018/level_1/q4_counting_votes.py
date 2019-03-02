n = int(input())
votes = []
yes_count = 0
no_count = 0
for i in range(n):
    a = input()
    votes.append(a)
for vote in votes:
    if vote == "YES":
        yes_count += 1
    elif vote == "NO":
        no_count += 1
print("YES {0}".format(yes_count))
print("NO {0}".format(no_count))