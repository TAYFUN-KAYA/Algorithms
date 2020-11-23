print("sayıyı ters çevirme ")

ters=int(input("ters sayıyı giriniz :"))
sama=ters
tsay=0
adet=0
while(ters != 0):
	ters=ters//10
	adet+=1
print("adet : ",adet)
while(sama != 0):
	temp=1
	sayi=sama-(sama//10)*10
	for i in range(1,adet):
		temp=temp*10
	temp=temp*sayi
	print("temp durum : ",temp)
	if(sama//10 != 0):
		tsay += temp
	else:
		tsay+=sayi
	sama=sama//10
	adet-=1
print("ters çevrilmiş hali : ",tsay)


print("ikinci yöntem")

ttsay=123456789
ttersi=0
while ttsay > 0:
	kalan=ttsay % 10
	ttersi=(ttersi*10)+kalan
	ttsay = int(ttsay / 10)
print("ters hali : ",ttersi)