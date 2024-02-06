# 38quiz.py Ethan Djou Coauthored: Khalid Saif, George Mo, Jordan S

def greg(n):
	sign = -1
	end = 0
	for x in range(0, n + 1):
		sign = sign * -1
		equation = (sign)/(2*x + 1)
		end = end + equation
	end = end * 4
	return(end)

print(greg(100))