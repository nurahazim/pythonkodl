#print ex:

print("merhaba", "dunya!", sep="//", end="! \n")
print("python ogreniyorum!")
print("bu \nalt satir gecer.")
print("tab\tbosluk birakir")

#renkli yazi yazma

print("\033[31mbu kirmizii renkte!\033[0m")
print("\033[32mbu yesil renkte!\033[0m")

#input ex:

ad = input("adinizi girin: ")
yas = input("yasinizi girin: ")
print(f"merhaba {ad}, {yas} yasindasin!")

#string-slicing

kelime = "programlama"
print(kelime[:5]) #ilk bes harfi alir
print(kelime[-4:]) #son 4 harfi alir
print(kelime[::-1]) #ters cevirir

#ascii-art

print("\033[36m ascii sanati \033[0m")
print("  *   ")
print(" ***  ")
print("******")
print("  !   ")
