import json

def readconstant():
	f = open('constant.json')
	constant = json.load(f)
	return constant


def writeconstant(constant):
	json_object = json.dumps(constant, indent=4)
	with open("constant.json", "w") as outfile:
		outfile.write(json_object)

def get_highest_level():
	const = readconstant()
	cnt = 0
	is_cheated = False

	for i in range(len(const["finished_level"])):
		if is_cheated == True:
			const["finished_level"][i] = 0
			continue
		if const["finished_level"][i] == 0:
			is_cheated = True
		elif const["finished_level"][i] == 1:
			cnt += 1
	
	writeconstant(const)
	return cnt
	


if __name__=="__main__":
	constant=readconstant()
	print(constant)
	constant["FPS"]=60
	print(constant)
	writeconstant(constant)
	print(readconstant())