filepath = "data.txt"
main = "INSERT INTO `garena` (`id`, `username`, `email`, `password`, `phone`, `security`, `date_added`, `action`) VALUES "
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		i = line.strip()
		u = i.split(":")[0]
		p = i.split(":")[1]
		
		main += "(NULL, '{}', '', '{}', '', '', '', ''),".format(u,p)
		
		line = fp.readline()
		cnt += 1

main = main[:-1]

wri = "final.txt"

wo = open(wri, "w")
wo.write(main)
wo.close()
print("saved as final.txt")
