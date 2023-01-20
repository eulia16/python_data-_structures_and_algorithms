#Same as R1.6 but w/ list comperhension

print(sum([k**2 for k in range(0, 20) if k & 1 == True]))
print(sum([k**2 for k in range(0, 7) if k & 1 == True]))

