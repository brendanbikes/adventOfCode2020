import re

def readInput():
	with open('day4input.txt', 'r') as f:
		data = f.read()

	return data

def process():
	data = readInput()
	passports = data.split('\n\n')

	required_keys = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
	optional_keys = set(['cid'])

	validCount=0
	validPassports=[]
	for passport in passports:
		fields_dict = {}
		fields = re.split(' |\n', passport)

		for field in fields:
			key, value = field.split(':')
			fields_dict['{}'.format(key)] = value

		#validate the passport field set
		keys = set(x[0] for x in fields_dict.items())
		if required_keys.issubset(keys):
			print('Passport has the valid number of fields')
		else:
			print('Passport does not have the correct number of fields, and is invalid.')
			continue

		#check the validity of the fields
		value = fields_dict['byr']
		try:
			value = int(value)
		except ValueError as e:
			print('Birth year is not an integer.')
			continue
		if value >=1920 and value <=2002:
			print('Birth year is valid format.')
		else:
			print('Birth year is invalid format.')
			continue

		value = fields_dict['iyr']
		try:
			value = int(value)
		except ValueError as e:
			print('Issue year is not an integer.')
			continue
		if value >=2010 and value <=2020:
			print('Issue year is valid format.')
		else:
			print('Issue year is invalid format.')
			continue

		value = fields_dict['eyr']
		try:
			value = int(value)
		except ValueError as e:
			print('Issue year is not an integer.')
			continue
		if value >=2020 and value <=2030:
			print('Issue year is valid format.')
		else:
			print('Issue year is invalid format.')
			continue

		value = fields_dict['hgt']
		if len(value)==4 and value[-2:]=='in' and int(value[0:2])>=59 and int(value[0:2])<=76:
			print('Height is properly formatted in inches')
		elif len(value)==5 and value[-2:]=='cm' and int(value[0:3])>=150 and int(value[0:3])<=193:
			print('Height is properly formatted in centimeters')
		else:
			print('Height is improperly formatted')
			continue

		value = fields_dict['hcl']
		#identify a hex code
		m = re.fullmatch(r"#[0-9a-z]{6}", value)
		if m:
			print('Hair color is properly formatted.')
		else:
			print('Hair color is not properly formatted.')
			continue

		value = fields_dict['ecl']
		if value in ['amb','blu','brn','gry','grn','hzl','oth']:
			print('Eye color is properly formatted.')
		else:
			print('Eye color is improperly formatted.')
			continue

		value = fields_dict['pid']
		print(value)
		m = re.fullmatch(r"[0-9]{9}", value)
		if m:
			print('Passport ID is properly formatted.')
		else:
			print('Passport ID is improperly formatted.')
			continue

		#If it got all the way here, it's a valid passport
		validCount+=1
		validPassports.append(passport)

	print('There were {} valid passports.'.format(validCount))
	#print(validPassports)

	with open('validPassports.txt', 'w') as f:
		for passport in validPassports:
			f.write(passport)
			f.write('\n\n')

if __name__ == "__main__":
	process()