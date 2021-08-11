import os
import pytesseract
from PIL import Image
import easyocr

#path1 = 'ci4.jpeg'

#im = Image.open(path1)
#im = im.rotate(80, expand=True)
#im.save("im80.jpeg")

#im = im.rotate(180, expand=True)
#im.save("teste.jpeg")

#path2 = "im80.jpeg"
#path3 = "teste.jpeg"

def convert_Text(argument, filename):
	print(filename)
	reader = easyocr.Reader(lang_list=['es'])
	try:
		simple_output = reader.readtext(argument, detail=0)
	except:
		print("===========================================================================\ndeu error!===========================================================================\n")
		simple_output = 'error!'
	valido = 0
	for tamanho in simple_output:
    		valido += len(tamanho)

	valid = (len(simple_output[0]) + len(simple_output[1]) +len(simple_output[2]) + len(simple_output[3]) + len(simple_output[4]) + len(simple_output[5]) + len(simple_output[6]) + len(simple_output[7]) + len(simple_output[8]) + len(simple_output[9]) + len(simple_output[10]) + len(simple_output[11]))
	print(valid)
	print(valido)
	print(simple_output)

	if valido > 180:
		with open("output.txt", "a") as txt_file:
		    txt_file.write(filename + '\n')
		    for line in simple_output:
		        txt_file.write("".join(line) + "\n")
		    txt_file.write('=================================\n\n')
		    txt_file.close()

## pega todos arquivos da pasta indicada e joga para a funcao
for _, _, files in os.walk('./fotos/'):
	for file in files:
		im = Image.open('./fotos/' + file)
		im = im.rotate(80, expand=True)
		im.save("im80.jpeg")
		convert_Text("im80.jpeg", file)

		im = im.rotate(180, expand=True)
		im.save("im180.jpeg")
		convert_Text("im180.jpeg", file)

		convert_Text('./fotos/' + file, file)
