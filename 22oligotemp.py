# 22oligotemp.py by Ethan Djou co-authored with Khalid Saif

def oligo(A, T, G, C):
	if A + T + G + C <= 13:
		return (A + T) * 2 + (G + C) * 4
	else: 
		return 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)

print(oligo(1, 2, 2, 2))
print(oligo(15, 100, 24, 62))
print(oligo(5, 6, 7, 8))