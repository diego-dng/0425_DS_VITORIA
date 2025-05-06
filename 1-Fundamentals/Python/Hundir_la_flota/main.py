import utils
import variables as vr



tablero_main = utils.crear_tablero()
print(tablero_main)
print("_________________________")
tablero_modificado = utils.colocar_barco(tablero_main, vr.barco_1)
tablero_modificado = utils.colocar_barco(tablero_main, vr.barco_2)
print(tablero_modificado)