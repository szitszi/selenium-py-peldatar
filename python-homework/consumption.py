print("Feladat 1.rész - fix adatok")
of = 7
vf = 9
o = 170
v = 35
b = 350
print("oda út fogyasztása: " + str((o/100*of)+(v/100*vf)) + " liter")
print("oda-vissza út fogyasztása: " + str((o/100*of*2)+(v/100*vf)*2) + " liter")
# print("oda út költsége: " + str((o/100*of*b)+(v/100*v*b)) + "Ft")
print("teljes út költsége: " + str(((o/100*of*b)+(v/100*vf*b))*2) + " Ft")

print("")

print("Feladat 2.rész - bekért adatok")
orfogy = input("Hány liter az autód országúti fogyasztása? : ")
varfogy = input("Hány liter az autód városi fogyasztása? : ")
out = input("Hány kilométert mentél országúton? : ")
vut = input("Hány kilométert mentél városban? : ")
ben = input("Mennyibe kerül egy liter benzin amit tankolsz az autódba? : ")
print("oda út fogyasztása: " + str((float(out)/100*float(orfogy))+(float(vut)/100*float(varfogy))) + " liter")
print("oda-vissza út fogyasztása: " + str(((float(out)/100*float(orfogy))+(float(vut)/100*float(varfogy)))*2) + " liter")
# print("oda út költsége: " + str((float(out)/100*float(orfogy)*float(ben))+(float(vut)/100*float(varfogy)*float(ben))) + " Ft")
print("oda-vissza út költsége: " + str(((float(out)/100*float(orfogy)*float(ben))+(float(vut)/100*float(varfogy)*float(ben)))*2) + " Ft")
