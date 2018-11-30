import random

def Create_Sort():
	NList = []
	i = 0

	while i < 50:
		Num = int(random.randint(0,65535))
		Len = int(len(NList))

		if Len <= 1:
			if Len == 0:
				NList.append(Num)
			elif Num < NList[Len-1]:
				NList.insert(Len-1,Num)
			else:
				NList.insert(Len,Num)

		else:
			I = 0
			while I < Len:
				if Num <= NList[I]:
					NList.insert(I,Num)
					break
				else:
					if Num <= NList[I+1]:
						NList.insert(I+1,Num)
						break
					elif Num > NList[-1]:
						NList.append(Num)
						break
					else:
						I += 1
						continue
				I += 1

		i += 1
		print(NList)

Create_Sort()