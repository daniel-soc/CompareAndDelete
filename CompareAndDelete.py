#!/usr/bin/env python3
####################################################################################
# Compare strings between two files, and deletes those repeated lines in the 2nd file
# Receives as input the names of those two files
####################################################################################
__AUTHOR__ = 'Galford'
__VERSION__ = "0.0.1 May 2020"

# Import required functions and libraries
import sys

print(r"""
   _____                                                          _   _____       _      _       
  / ____|                                         /\             | | |  __ \     | |    | |      
 | |     ___  _ __ ___  _ __   __ _ _ __ ___     /  \   _ __   __| | | |  | | ___| | ___| |_ ___ 
 | |    / _ \| '_ ` _ \| '_ \ / _` | '__/ _ \   / /\ \ | '_ \ / _` | | |  | |/ _ \ |/ _ \ __/ _ \
 | |___| (_) | | | | | | |_) | (_| | | |  __/  / ____ \| | | | (_| | | |__| |  __/ |  __/ ||  __/
  \_____\___/|_| |_| |_| .__/ \__,_|_|  \___| /_/    \_\_| |_|\__,_| |_____/ \___|_|\___|\__\___|
                       | |                                                                       
                       |_|                                                                       

By Galford
""")

# Main menu
def main():
	while (True):
		MenuString = r"""
[1] Choose input lists and start
[2] Exit
		"""
		# Displays CLI menu options
		print(MenuString)
		MenuInput = input("[*] Please type the number of the action you want to perform: ")
		while MenuInput not in ("1","2"):
			print ("[!] Option not recognized")
			MenuInput = input("[*] Please type the number of the action you want to perform: ")
		if MenuInput == "1":
			print("[!] IMPORTANT: Repeated lines will be deleted ON THE SECOND FILE you provide.")
			FileOrder = ["first", "second"]
			Targets = []
			Data = []
			
			for order in FileOrder:
				FileName = input("[*] Type the %s file's name: " %(order))
				CheckStatus = fileChecker(FileName)
				while CheckStatus[0] == False:
					FileName = input("[*] Type the %s file's name: " %(order))
					CheckStatus = fileChecker(FileName)
				Targets.append(FileName)
				Data.append(CheckStatus[1])
			CompareDelete(Data, Targets[1])
			print ("[+] Job Finished")		
		else:
			print ("[!] Shutting CompareAndDelete down")
			sys.exit()

# Opens file and retrieves data
def fileChecker(filepath):
	filedata = []
	try:
		with open(filepath, 'r') as file:
			filedata = [line.rstrip() for line in file.readlines()]
			print ("[+] Detected %i lines." %(len(filedata)))
			file.close()
			return True, filedata
			pass
	except FileNotFoundError:
		print ("[!] File does not exist")
		return False, None

# Compares data from files and deletes repeated lines
def CompareDelete(data, file):
	NewFileName = "Filtered_"+file
	RepeatedCounter = 0

	for i in range(len(data[0])):
		for j in range(len(data[1])):
			if data[0][i] == data[1][j]:
				print ("[!] Repeated line found!\n[!] %s\n[!] %s" %(data[0][i], data[1][j]))
				data[1][j] = ""
				RepeatedCounter += 1
	
	if RepeatedCounter == 0:
		print ("[+] Zero repeated lines between those files. No new file will be generated.")
	else:
		with open(NewFileName, "w") as output:
			data[1] = list(filter(None, data[1]))
			for item in data[1]:
				output.write("%s\n" % item)
			output.close()
		print ("[+] Results written on "+NewFileName+", with a new total of "+str(len(data[1]))+" lines")
	

# Initializes main routine
if __name__ == '__main__':
    main()