##### Insert line after a specific position #####

# for i in range(1,8):
# 	with open("data_hp%d.txt" % i,"r+") as in_file:
# 		buf = in_file.readlines()

# 	with open("data_hp%d.txt" % i,"w") as out_file:
# 		for line in buf:
# 			if(line == "Draco\n"):
# 				line = line + "Malfoy\n"
# 			out_file.write(line)



###### Append at the end of the file #####

for i in range(1,8):
	with open("data_hp%d.txt" % i,"a+") as f:
		f.write("\Professor Albus Dumbledore\n")


##### Replace into same line #####

# for i in range(5,8):
# 	with open("data_hp%d.txt" % i,"r+") as in_file:
# 		buf = in_file.readlines()

# 	with open("data_hp%d.txt" % i,"w") as out_file:
# 		for line in buf:
# 			if(line == "Draco\n"):
# 				line = "Draco Malfoy\n"
# 				out_file.write(line)

# 			elif(line != "Malfoy\n"):
# 				out_file.write(line)

# for i in range(2,8):
# 	with open("data_hp%d.txt" % i,"r+") as in_file:
# 		buf = in_file.readlines()

# 	with open("data_hp%d.txt" % i,"w") as out_file:
# 		for line in buf:
# 			if(line == "McGonagall\n"):
# 				line = "Professor McGonagall\n"
# 				out_file.write(line)

# 			elif(line != "McGonagall\n"):
# 				out_file.write(line)

# for i in range(3,8):
# 	with open("data_hp%d.txt" % i,"r+") as in_file:
# 		buf = in_file.readlines()

# 	with open("data_hp%d.txt" % i,"w") as out_file:
# 		for line in buf:
# 			if(line == "Professor Albus Dumbledore\n"):
# 				continue
# 				# line = "Professor Albus Dumbledore\n"
# 				# out_file.write(line)
# 			out_file.write(line)

			
