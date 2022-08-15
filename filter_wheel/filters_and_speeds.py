filters = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "0101", 6: "0110", 7: "0111", 8: "1000", 9: "1001"}
speeds = {0: "000", 1: "001", 2: "010", 3: "011", 4: "100", 5: "101", 6: "110", 7: "111"}

filterList = []
speedList = []

for filter in filters.keys():
	filterList.append(str(filter))

for speed in speeds.keys():
	speedList.append(str(speed))