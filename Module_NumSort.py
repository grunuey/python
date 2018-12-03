def Random_Num_Create():
	import random
	Num = int(random.randint(0,65535))
	return Num

def List_Sort_Add(Len,Num,NList):
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