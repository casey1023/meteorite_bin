import json

def readconstant():
	f = open('constant.json')
	constant = json.load(f)
	return constant


def writeconstant(constant):
	json_object = json.dumps(constant, indent=4)
	with open("constant.json", "w") as outfile:
		outfile.write(json_object)


if __name__=="__main__":
	constant=readconstant()
	print(constant)
	constant["FPS"]=30
	print(constant)
	writeconstant(constant)
	print(readconstant())