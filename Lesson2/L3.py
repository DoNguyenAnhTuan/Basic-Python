def thu_chi_hoc_sinh():
    thu = int(input("Khoản tiền thu nhập của bạn là: "))
    khoan_hoc_tap = int(input("Bạn tốn số tiền cho việc học tập là: "))
    khoan_vui_choi = int(input("Bạn tốn số tiền cho việc vui chơi là: "))
    khoan_an_uong = int(input("Bạn tốn số tiền cho việc ăn uống là: "))
    so_tien_chi = khoan_hoc_tap + khoan_vui_choi + khoan_an_uong
    print("Số tiền chi của bạn là: ",so_tien_chi)
    print("Số tiền còn lại của bạn là: ",thu - so_tien_chi)
    print("Chú thích: 1 KHÚC = 10 nghìn đồng")
    print("Thu:")
    t = int(thu / 10000 + 1)
    for i in range(1, t):
        print("-")
    print("Chi: ")
    o = int(so_tien_chi / 10000 + 1)
    for w in range(1, o):
        print("-")
    print("Cụ thể tiền chi là:")
    print("Học tập: ")
    p = int(khoan_hoc_tap / 10000 + 1)
    for l in range(1, p):
        print("-")
    print("Vui chơi: ")
    n = int(khoan_vui_choi / 10000 + 1)
    for m in range(1, n):
        print("-")
    print("Ăn uống: ")
    k = int(khoan_an_uong / 10000 + 1)
    for g in range(1, k):
        print("-")
    if khoan_vui_choi > khoan_hoc_tap:
        print("Bạn chưa tập trung vào học tập đâu.")
    elif khoan_vui_choi > khoan_an_uong:
        print("Bạn chú ý bồi dưỡng sức khỏe hơn.")
thu_chi_hoc_sinh()
