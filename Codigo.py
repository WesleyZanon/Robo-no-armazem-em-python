class Robo():
    def __init__(self, origem):
        
        self.bateria = 9
        self.pos = origem
        
        self.limpaMapa()
        
        
    def limpaMapa(self):
        self.matriz = []
        self.matriz.append(list('    +---+---+---+    '))
        self.matriz.append(list('    |   |   |   |    '))
        self.matriz.append(list('    |   |   |   |    '))
        self.matriz.append(list('+---|- -|- -|- -|---+'))
        self.matriz.append(list('|                   |'))
        self.matriz.append(list('|   |---|---|---|   |'))
        self.matriz.append(list('|   |   |   |   |   |'))
        self.matriz.append(list('|   |   |   |   |   |'))
        self.matriz.append(list('|   |- -|- -|- -|   |'))
        self.matriz.append(list('|                   |'))
        self.matriz.append(list('+---+---+---+---+---+'))
        
        self.marcaMapa([1,6], 'A')
        self.marcaMapa([1,10], 'B')
        self.marcaMapa([1,14], 'C')
        self.marcaMapa([6,6], 'D')
        self.marcaMapa([6,10], 'E')
        self.marcaMapa([6,14], 'F')
        self.marcaMapa([8,1], 'T')
        self.marcaMapa(self.pos,  'R')
        
    def criaRota(self):
        
        self.marcaMapa(self.pos, bateria)
        
    def mostraMapa(self):
        for l in self.matriz:
            print(' '.join(l))
            
            
    def marcaMapa(self, pos, letra):
        self.matriz[pos[0]][pos[1]] = letra
        

#######
bateria = 9
r = Robo(origem = [4,18])
r.mostraMapa()



x = 0

while x == 0:
    
    r.mostraMapa()
    destino = input("Digite o destino que pretende chegar ou zero para sair: ")
    
    
    
    #if destino != "A" or destino != "B" or destino != "C" or destino != "D" or destino != "E" or destino != "F" or destino != '0' or destino != "T":
     #   print("Digite uma rota existente. ")
        
    if destino == "0":
        break
        
    else:
        
        while r.pos != destino and bateria != 0:
            
            x = 4
                
            while x != 0:
            
                r.criaRota()
            
                x=x-1
                
            
            bateria = bateria -1
