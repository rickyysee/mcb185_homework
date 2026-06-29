# 11oligo.py by Ricky Cantua

def oligo_Tm(a, t, c, g):
	total = a + t + c + g
	if total <= 13: return (a+t)*2 + (g+c)*4
	return 64.9 + 41*(g+c-16.4)/(total)

print('Melting temps of the following oligos:')
print('A , T , C , G : Tm')
print('13, 25, 7 , 40:', oligo_Tm(13, 25, 7, 40))
print('5 , 4 , 7 , 3 :', oligo_Tm(5, 4, 7, 3))
print('3 , 1 , 5 , 2 :', oligo_Tm(3, 1, 5, 2))