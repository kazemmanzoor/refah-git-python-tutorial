def vowel_count(str):
    	count = 0
	vowel = set("aAeEiIoOuU")
	for alphabet in str:
		if alphabet in vowel:
			count = count + 1
	print("Total number of vowels:", count)
	



str = "MOhadEseh"
vowel_count(str)
