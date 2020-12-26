import sys

def readInput():
	with open('day21Input.txt', 'r') as f:
		data = [[x.split('(')[0].strip().split(' '), x.split('(')[1].strip(')')[9:].split(', ')] for x in f.read().splitlines()]
	return data


def part1():
	data = readInput()

	allergenMap = {}

	for recipe, allergens in data:
		for allergen in allergens:
			if allergen in allergenMap.keys():
				allergenMap[allergen] = allergenMap.get(allergen).intersection(set(recipe))
			else:
				allergenMap[allergen] = set(recipe)

	#count allergens
	allergenCount = len(allergenMap.keys())

	#the allergenMap now contains 1:1 mappings -- remove the identified allergens from other sets

	allergicIngredients = {}

	while len(allergicIngredients.keys()) < allergenCount: #mapping is not 1:1 for all items:
		#identify 1:1 mappings
		for allergen, ingredients in allergenMap.items():
			if len(list(ingredients)) == 1:
				#this is a known allergen ingredient
				allergicIngredients[allergen]=list(ingredients)[0]

		#now go through all the recipes that still have multiple ingredients and remove the known allergen
		for allergicIngredient in allergicIngredients.values():
			for allergen, ingredients in allergenMap.items():
				if len(list(ingredients)) > 1 and allergicIngredient in ingredients:
					#remove it
					ingredients.remove(allergicIngredient)
					#put it back in the dictionary
					allergenMap[allergen] = ingredients

	print(allergicIngredients)
	#all allergens identified
	#count the number of times the non-allergen ingredients appear

	nonAllergenCount = 0
	for recipe, allergens in data:
		nonAllergenCount += len(set(recipe).difference(set(allergicIngredients.values())))

	print(nonAllergenCount)

	print(','.join([x[1] for x in sorted([(key, value) for key, value in allergicIngredients.items()], key=lambda x: x[0])]))

if __name__ == '__main__':
	part1()