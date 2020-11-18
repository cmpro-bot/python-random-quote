import random
def primary():
  #print("Keep it logically awesome.")
  f = open("quotes.txt","a")
  for i in range(2):
    f.write("Appended line %d\r\n"%(i+1))
  f.close()
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])
  rnd = random.randint(0, last)
  print(quotes[rnd])
if __name__== "__main__":
  primary()
