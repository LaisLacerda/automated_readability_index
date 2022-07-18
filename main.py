import math
import re


def readability():
  recebe_frase = (input('Digite uma frase: '))
  resultado = recebe_frase
  
  qtd_frases = resultado.count(recebe_frase)
  
  
  qtd_palavras = len(re.findall(r'\w+',resultado))
  
  
  qtd_letras = len(resultado.replace(" ",""))
  
  
  formula1 = 4.71 * qtd_letras / qtd_palavras
  
  
  formula2 = 0.5 * qtd_palavras 
  
  
  formula3 = formula1 + formula2 - 21.43
  
  
  valor_arredondado = math.ceil(formula3) 
  
  
  if valor_arredondado < 1:
    valor_arredondado = 1
    
  if valor_arredondado > 14:
    valor_arredondado = 14
    
  print('Resultado do Automated Readability Index: ', valor_arredondado)


readability()