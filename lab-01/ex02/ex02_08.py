#Vương Zen-2380602639
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
chuoiso_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")