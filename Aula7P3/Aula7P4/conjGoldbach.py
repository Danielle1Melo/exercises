
def primo (numero):
  for div in range (2, numero//2 + 1):
        if numero % div == 0:
            return False
  return True
  
def goldbac (numero):
    for v1 in range (2, numero):
        v2= numero - v1
        if primo(v1) and primo(v2):
           return v1, v2
        
for num in range(4,100,2):
   primo1, primo2 = goldbac(num)
   print(f"{num:3}: {primo1} + {primo2}")