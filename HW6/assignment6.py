import fileinput
import sys

def list_printer(string_list):
	final_string = ""

	for string in string_list:
		final_string += string + " "

	return final_string


def iterSplitter(word, split_string):
	placeHolder = [[False for i in range(len(word)+1)] for i in range(len(word)+1)]
	wordChecker = [[False for i in range(len(word)+1)] for i in range(len(word)+1)]
	

	counter = 0
	for i in range(len(word)):
		for j in range(len(word)):
			counter = i+j

			if counter < len(word):
				if word[j:counter+1] in dictionary:
					wordChecker[j][counter] = True
					placeHolder[j][counter] = j

				for k in range(j+1, counter+1):
					if wordChecker[j][k-1] is True and wordChecker[k][counter] is True:
						wordChecker[j][counter] = True
						placeHolder[j][counter] = k
						break

	i = 0
	#This while loop will store the split strings
	while i < len(word)-1:
		k = placeHolder[i][len(word)-1]

		if i == k:
			split_string.append(word[i:(len(word)-1)+1])
			break
		split_string.append(word[i:k])
		i = k

	return wordChecker[0][len(word)-1]


def recSplitter(word, index, store_list, visited_set):
	if word[index:] in dictionary:
		store_list.append(word[index:])
		return True

	#This checks to make sure that there aren't reocurring strings
	if index in visited_set:
		return False

	j = index
	while j < len(word):
		if string[index:j+1] in dictionary:
			if recSplitter(word, j+1, store_list, visited_set):
				store_list.append(word[index:j+1])
				return True
		j += 1

	#This will add strings that are already looked at 
	visited_set.add(index)
	return False 


if __name__ == "__main__":
	##Used sampleHash.pdf as a good reference to help 
	dictionary = set() #This will be used as the dictionary set that will put all of the words from diction10k.txt into a set
	dictionary_file = open('diction10k.txt', 'r') #reads the file 
	
	for line in dictionary_file:
		dictionary.add(line.strip()) #This for loops puts the words in the dictionary list into the set

	file_lines = []
	for line in fileinput.input():
		if len(line) > 1:
			file_lines.append(line.strip())


	#This will go through every line in the file and run it through the recursive and iterative
	#functions then let you know if it can or can't be split.
	length = int(file_lines[0])
	for i in range(1, length+1):
		string = file_lines[i]

		print("Phrase number: ", i)
		print(string, "\n")

		split_string = []
		visited_list = set()

		print("Iterative attempt:")
		if iterSplitter(string, split_string) is True:
			print("YES, can be split.")
			print(list_printer(split_string))
		else:
			print("NO, cannot be split.")

		split_string = []
		print("\nMemoized attempt:")
		if recSplitter(string, 0, split_string, visited_list) is True:
			print("YES, can be split.")
			split_string.reverse()
			print(list_printer(split_string))
		else:
			print("NO, cannot be split.")
		print("\n")