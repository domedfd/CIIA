import os
from PIL import Image
import easyocr

pasta = './fotos/'

def convert_Text(argument, filename):
	print(filename)
	reader = easyocr.Reader(lang_list=['es'], gpu=False)
	try:
		simple_output = reader.readtext(argument, detail=0)
	except:
		print("===========================================================================\ndeu error!===========================================================================\n")
		simple_output = 'error!'
	valido = 0
	for tamanho in simple_output:
    		valido += len(tamanho)

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
for _, _, files in os.walk(pasta):
	for file in files:
		im = Image.open(pasta + file)
		im = im.rotate(80, expand=True)
		im.save("im80.jpeg")
		convert_Text("im80.jpeg", file)

		im = im.rotate(180, expand=True)
		im.save("im180.jpeg")
		convert_Text("im180.jpeg", file)

		convert_Text(pasta + file, file)
