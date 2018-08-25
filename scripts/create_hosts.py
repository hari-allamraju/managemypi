name_universe = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet",\
				"kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango",\
				"uniform","victor","whiskey","xray","yankee","zulu"]

with open("/usr/local/etc/ansible/hosts","w") as h:
	f=open("pis.txt","r")
	h.write("[rpi]\n")
	for i,ip in enumerate(f.readlines()):
		h.write(name_universe[i]+" ansible_host="+ip)
