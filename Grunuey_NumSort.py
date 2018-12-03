import Module_NumSort

NList = []
i = 0

while i < 50:
	Num = Module_NumSort.Random_Num_Create()
	Len = int(len(NList))

	Module_NumSort.List_Sort_Add(Len,Num,NList)

	i += 1

	print(NList)