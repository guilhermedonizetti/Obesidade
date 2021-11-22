def ler_dados():
	dados = []
	linhas = open("teste_obesidade.txt").readlines()
	
	for i in linhas:
		dados.append(i.split(","))

	for i in range(len(dados)):
		x = dados[i][16].split("\n") #eliminando o "\n" do final
		dados[i][16] = x[0]
	
	return dados

def testar_j48(dados):
	acerto = 0

	for i in dados:
		if float(i[3]) <= 99.530971:
			if float(i[3]) <= 60:
				if float(i[2]) <= 1.66:
					if float(i[3]) <= 46.655622:
						if float(i[2]) <= 1.513202:
							obesidade = "Normal_Weight"
						else:
							if float(i[3]) <= 44.918255:
								obesidade = "Insufficient_Weight"
							else:
								if float(i[2]) <= 1.58:
									obesidade = "Normal_Weight"
								else:
									obesidade = "Insufficient_Weight"
					else:
						if float(i[2]) <= 1.53777:
							if i[5] == "yes":
								if i[11] == "yes":
									obesidade = "Overweight_Level_I"
								else:
									if float(i[3]) <= 56.307019:
										obesidade = "Normal_Weight"
									else:
										obesidade = "Overweight_Level_I"
							else:
								obesidade = "Normal_Weight"
						else:
							if float(i[3]) <= 50.664459:
								if float(i[2]) <= 1.605404:
									obesidade = "Normal_Weight"
								else:
									obesidade = "Insufficient_Weight"
							else:
								obesidade = "Normal_Weight"
				else:
					if float(i[3]) <= 54.997374:
						obesidade = "Insufficient_Weight"
					else:
						if float(i[2]) <= 1.750384:
							obesidade = "Normal_Weight"
						else:
							if float(i[12]) <= 1.330519:
								obesidade = "Normal_Weight"
							else:
								obesidade = "Insufficient_Weight"
			else:
				if float(i[3]) <= 76:
					if float(i[2]) <= 1.5891:
						if i[5] == "yes":
							if float(i[3]) <= 70:
								obesidade = "Overweight_Level_I"
							else:
								obesidade = "Obesity_Type_I"
						else:
							obesidade = "Overweight_Level_II"
					else:
						if float(i[2]) <= 1.734832:
							if float(i[3]) <= 72:
								if float(i[2]) <= 1.648143:
									if float(i[3]) <= 64.4:
										obesidade = "Normal_Weight"
									else:
										obesidade = "Overweight_Level_I"
								else:
									if float(i[1]) <= 27.474245:
										obesidade = "Normal_Weight"
									else:
										if float(i[6]) <= 2.805533:
											obesidade = "Overweight_Level_I"
										else:
											obesidade = "Normal_Weight"
							else:
								if float(i[1]) <= 20.438478:
									if float(i[1]) <= 18.48207:
										obesidade = "Overweight_Level_I"
									else:
										obesidade = "Overweight_Level_II"
								else:
									obesidade = "Overweight_Level_I"
						else:
							if float(i[2]) <= 1.85:
								if float(i[3]) <= 75.306702:
									obesidade = "Normal_Weight"
								else:
									if float(i[1]) <= 28.493397:
										obesidade = "Normal_Weight"
									else:
										obesidade = "Overweight_Level_I"
							else:
								if float(i[3]) <= 65.423942:
									obesidade = "Insufficient_Weight"
								else:
									obesidade = "Normal_Weight"
				else:
					if float(i[2]) <= 1.729177:
						if float(i[2]) <= 1.64639:
							if float(i[3]) <= 92:
								obesidade = "Obesity_Type_I"
							else:
								obesidade = "Obesity_Type_II"
						else:
							if float(i[3]) <= 85.316199:
								if float(i[2]) <= 1.665199:
									if float(i[3]) <= 81.384224:
										obesidade = "Overweight_Level_II"
									else:
										obesidade = "Obesity_Type_I"
								else:
									obesidade = "Overweight_Level_II"
							else:
								if float(i[3]) <= 88.675503:
									if float(i[2]) <= 1.694997:
										obesidade = "Obesity_Type_I"
									else:
										obesidade = "Overweight_Level_II"
								else:
									obesidade = "Obesity_Type_I"
					else:
						if float(i[3]) <= 91:
							if float(i[2]) <= 1.799779:
								if float(i[3]) <= 83.26312:
									if float(i[1]) <= 30.163408:
										obesidade = "Overweight_Level_I"
									else:
										obesidade = "Overweight_Level_II"
								else:
									if float(i[7]) <= 3.054899:
										obesidade = "Overweight_Level_II"
									else:
										obesidade = "Overweight_Level_I"
							else:
								if float(i[3]) <= 84.49798:
									obesidade = "Normal_Weight"
								else:
									if i[8] == "no":
										obesidade = "Overweight_Level_I"
									if i[8] == "Sometimes":
										obesidade = "Overweight_Level_I"
									if i[8] == "Frequently":
										obesidade = "Normal_Weight"
									if i[8] == "Always":
										obesidade = "Overweight_Level_I"
						else:
							if float(i[2]) <= 1.794827:
								obesidade = "Obesity_Type_I"
							else:
								obesidade = "Overweight_Lavel_II"
		else:
			if i[0] == "Female":
				obesidade = "Obesity_Type_III"
			else:
				if float(i[1]) <= 22.524036:
					if float(i[6]) <= 2.571274:
						obesidade = "Obesity_Type_I"
					else:
						if float(i[12]) <= 0.967627:
							obesidade = "Obesity_Type_II"
						else:
							obesidade = "Obesity_Type_I"
				else:
					if float(i[3]) <= 109.599453:
						if float(i[2]) <= 1.750384:
							if float(i[10]) <= 1.768111:
								obesidade = "Obesity_Type_II"
							else:
								obesidade = "Obesity_Type_I"
						else:
							if float(i[2]) <= 1.86516:
								obesidade = "Obesity_Type_I"
							else:
								obesidade = "Overweight_Level_II"
					else:
						obesidade = "Obesity_Type_II"

		if obesidade == i[16]:
			acerto = acerto + 1
	
	return acerto

def iniciar_j48():
	valores = ler_dados()
	acertos = testar_j48(valores)
	precisao = (acertos / len(valores)) * 100
	print("PRECISAO: {}%".format(precisao))

#Rodar o programa
iniciar_j48()




"""
ATRIBUTO | POSICAO NO VETOR i

Gender 0
Age 1
Height 2
Weight 3
family_history_with_overweight 4
FAVC 5
FCVC 6
NCP 7
CAEC 8
SMOKE 9
CH2O 10
SCC 11
FAF 12
TUE 13
CALC 14
MTRANS 15
NObeyesdad 16
"""