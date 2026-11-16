import os 
import time

while True:
    try:
        resultado = []
        u=int(input("Digite o número unitário:"))
        if u < 0 or u > 9:
            print("Unitário Animal")
            print("Limpando a tela em 3,2,1....")
            time.sleep(3)
            os.system()
            continue
        
        d=int(input("Digite o número com dezenas:"))
        if d < 10 or d >99:
            print("Com dezenas animal")
            print("Limpando a tela em 3,2,1.....")
            time.sleep(3)
            os.system()
            continue
        
        a= d//10
        b= d%10
        s= u+a+b
        dv= d/u

        if s == dv:
            resultado.append((f"Unitario {u}, Dezena {d}, Soma {u} + {a} + {b} = {s} e a Divisão {d} / {u} = {dv}"))
            print(f"Parabéns você achou a lógica{resultado}")
            break
        else:
            print("errou animal")
            continue
    except ValueError:
        print("Número Animal")