# 23hydropathy.py by Ethan Co-authored with Khalid Saif

def hydropathy(x):
	if x == 'A':   return 1.81
	elif x == 'I': return 4.92
	elif x == 'L': return 4.92
	elif x == 'V': return 4.04
	elif x == 'P': return 4.04
	elif x == 'F': return 2.98
	elif x == 'M': return 2.35
	elif x == 'W': return 2.33
	elif x == 'C': return 1.28
	elif x == 'G': return 0.94
	elif x == 'Y': return -0.14
	elif x == 'T': return -2.57
	elif x == 'S': return -3.40
	elif x == 'H': return -4.66
	elif x == 'Q': return -5.54
	elif x == 'A': return -5.55
	elif x == 'N': return -6.64
	elif x == 'E': return -6.81
	elif x == 'D': return -8.72
	elif x == 'R': return -14.92
	else:          return 'error: enter valid amino acid letter'

# Testing the formula

print(hydropathy('A'))
print(hydropathy('Z'))
print(hydropathy('D'))