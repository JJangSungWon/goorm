if __name__ == "__main__":
	

	n = input()
	cnt = 0
	
	for i in range(3, int(n)):
		string = str(i)
		
		for j in range(len(string)):
			if string[j] == "3" or string[j] == "6" or string[j] == "9":
				cnt += 1
	
	print(cnt)