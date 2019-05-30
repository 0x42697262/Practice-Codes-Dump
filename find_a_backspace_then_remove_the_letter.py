bcksp = "[<-]"
word1 = "whs[<-]at tre[<-][<-]he f?"


def findAll(file, str):
  initial = 0
  while True:
    initial = file.find(str, initial)
    if initial == -1: return
    yield initial
    initial += len(str)
	
wIndex = list(findAll(words, bcksp))
def repText():
  for i in wIndex:
  # === I stop here === #
    nexx = words[:i-1] + words[i:]  # wrong
