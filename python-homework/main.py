print("1. megoldás")
from bmodul import my_variable          # egy konkrét változó importálása egy másik modulból
print(my_variable)



print("2. megoldás")
import bmodul                           # a teljes modul importálása
print(bmodul.my_variable)               # ahol a modulból használandó változó elé be kell hivatkozni az eredeti/importált modul nevét
