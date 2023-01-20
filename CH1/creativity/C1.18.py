#list ciprehension shit

#using loop
seq = []
ans =0
for i in range(10):
    ans = ans + (i*2)
    seq.append(ans)
print(seq)

#one liner w/ list comprehension
summary = [i*(i-1) for i in range(1, 11)]
print(summary)




