resposta = []
for u in range(1,10):
    for d in range(10,100):
            a= d//10
            b= d%10
            s= u+a+b
            dv= d/u
            if s == dv:
                resposta.append((u,d))
print(resposta)  