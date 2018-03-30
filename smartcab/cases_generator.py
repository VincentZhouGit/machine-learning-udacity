#(1) ignore the waypoint
#(2) in our abstraction, it always facing situation in an intersection

data = {
 "waypoint":["forward", "left", "right"],
 "light": ["red"],#["green", "red"],
 "left": ["None","forward", "left", "right"],
 "right": ["None","forward", "left", "right"],
 "oncoming": ["None","forward", "left", "right"],
}


text_file = open("cases.txt", "w")

for waypoint in data["waypoint"]:
	for light in data["light"]:
		for left in data["left"]:
			for right in data["right"]:
				for oncoming in data["oncoming"]:
					text_file.write("| {} | {} | {} | {} | {} |  |\n".format(waypoint, light,left,right,oncoming))


text_file.close()
