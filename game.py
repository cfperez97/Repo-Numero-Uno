import sys
def loop1() :
	print  3 #">You have entered a hallway with two doors. Which do you choose? Door 1 or Door 2? (hint: you will die if you choose Door 1)"
	def loop2() :
		door = raw_input(">")
		if door == "Door 1." or door =="Door 1" or door == "door 1." or door == "door 1" or door == "Door1." or door =="Door1" or door == "door1." or door == "door1" or door == "1." or door == "1":
			print ">You died. (I told you so)"
		elif door == "Door 2." or door == "Door 2" or door == "door 2." or door == "door 2" or door == "Door2." or door == "Door2" or door == "door2." or door == "door2" or door == "2." or door == "2":
			print ">You still died. (I'm not sorry)"
		elif door == "Neither." or door == "Neither" or door == "neither." or door ==  "neither" or door == "Niether." or door == "Niether" or door == "niether." or door == "niether":
			print ">You lived! Clever..."
		else:
			print ">I'm sorry. I couldn't understand that. What was that?"
			loop2()
		def loop3() :
			print ">Want to try again?"
			ans = raw_input(">")
			if ans == "YES." or ans == "YES" or ans == "Yes." or ans == "Yes" or ans == "yes." or ans == "yes" or ans == "Sure." or ans == "Sure" or ans == "sure." or ans == "sure" or ans == "Yeah." or ans == "Yeah" or ans == "yeah." or ans == "yeah" or ans == "OK." or ans == "OK" or ans == "Ok." or ans == "Ok" or ans == "ok." or ans == "ok":
				loop1()
			elif ans == "NO." or ans == "NO" or ans == "No." or ans == "No" or ans == "no." or ans == "no" or ans == "Nah." or ans == "Nah" or ans == "nah." or ans == "nah":
				print ">Yeah right. Like you have more important things to do."
				sys.exit()
			else:
				print ">I'm sorry. I couldn't understand that."
				loop3()
		loop3()
	loop2()
loop1()
