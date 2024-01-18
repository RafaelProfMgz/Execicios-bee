def calcula(arr):
  n1 = int(arr[0])
  n2 = int(arr[1])

  homens = geraMatriz(n1)

  mata(n2, homens)

def geraMatriz(homens):
  matriz = []
  for x in range(homens):
    matriz.append(False)
  return matriz

def mata(num, homens):
  contador = 1
  volta = 0

  while not restaUm(homens):
    if(not homens[volta]):
      if contador % num == 0: 
        homens[volta] = True
      contador = contador + 1
    
    volta = volta + 1

    if volta + 1 == len(homens)+1:
      volta = 0

  
  for i in range(len(homens)):
    if(not homens[i]):
      global caseNumber
      print('Case {}: {}'.format(caseNumber, i+1))
      caseNumber = caseNumber + 1

def restaUm(homens):
  resta = 0
  for homem in range(len(homens)):
    if(not homens[homem]):
      resta = resta + 1
  if(resta > 1):
    return False
  else:
    return True

solutions = input()

cases = []

caseNumber = 1

for x in range(0, int(solutions)):
  cases.append(input())

def separa(n):
  return n.split()

x = list(map(separa, cases))

for y in range(0, len(x)):
  calcula(x[y])