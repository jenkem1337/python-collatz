def collatz(sayı):
	if sayı%2==0:
		return sayı/2
	elif sayı%2==1:
		return sayı*3+1
	else:
		print("Biryerde hata yaptın herhalde !!!")
		return None
print("Bu sayı collatz sayısı mı programına hoşgeldin !!! ")

while True :
	Sayı = int(input("Sayı giriniz :"))
	print("Girdiğiniz sayı {}".format(Sayı))
	while Sayı!=1:
		colatzSayısı = collatz(Sayı)
		print(colatzSayısı)
		if colatzSayısı == 1:
			print("Bu bir Collatz sayısı") 

