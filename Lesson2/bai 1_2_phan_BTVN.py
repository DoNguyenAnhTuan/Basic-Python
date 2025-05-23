import random
def game_vui():
	while True:
		so_luot_doan = 0
		print("Xin chào!Bạn tên là gì: ")
		ten_nguoi_choi = input()
		so = random.randint(1, 100)
		print("Ok," + ten_nguoi_choi + ",tôi đang nghĩ một con số giữa 1 và 100.")
		print("Bạn có 20 lần để đoán số tôi đang nghĩ")
		while so_luot_doan < 21:
			print("Bạn hãy đoán đi.")
			doan = input()
			doan = int(doan)
			so_luot_doan += 1
			if doan < so:
				print("Bạn đoán thấp hơn con số đó rồi")
			elif doan > so:
				print("Bạn đoán cao hơn con số đó rồi ")
			elif doan == so:
				break
		if doan == so:
                        so_luot_doan = str(so_luot_doan) 
			print("Tốt lắm" + ten_nguoi_choi + "Bạn đã đoán được số của tôi trong" + so_luot_doan + "lần đoán")
			print("Bạn có muốn chơi lại hay không hả" + ten_nguoi_choi + "(có hay không)")
			again1 = str()
			if again1 == "có":
				continue
			elif again1 == "không":
				break
		elif doan != so:
			so = str(so)
			print("Sai hết rồi" + ten_nguoi_choi + "!" + "Số tôi đang nghĩ là số" + so)
			print("Bạn có muốn chơi lại hay không hả" + ten_nguoi_choi + "(có hay không)")
			again2 = str()
			if again2 == "có":
				continue
			elif again2 == "không":
				break
game_vui()
