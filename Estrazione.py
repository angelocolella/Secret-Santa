import random
p = []  #array di partecipanti che varia
p2 = [] #array di partecipanti
 
def main (num):
   for i in range (num):
       print(int(i+1), end ="")
       nome = input( "° partecipante: ")
       p.append(nome)
       p2.append(nome)
       
 
def estrazione(p,p2, num):
   i=0
   while True:
       estratto = random.choice(p)
       print(i)
       if i == (num-2):
           if estratto != p2[i] :
               p.remove(estratto)
               estratto1 = random.choice(p)
               if estratto1 != p2[i+1]:
                   with open(p2[i] + ".txt" , "w") as file:
                       file.write(estratto)
                   with open(p2[i+1] + ".txt" , "w") as file:
                       file.write(estratto1)    
           break

       if estratto != p2 [i]:
           with open(p2[i] + ".txt" , "w") as file:
               file.write(estratto)
           p.remove(estratto)
           i+=1



num = int(input ("Quanti partecipanti? "))
 
main(num)
estrazione(p,p2 ,num)

