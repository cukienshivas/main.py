
def boi_toan_tinh_duyen(ten_nam, ten_nu):
    ten_nam=ten_nam.lower()
    ten_nu=ten_nu.lower()
    dem=0
    for chu_cai in range(ord('a'),ord('z')+1):
        if (chr(chu_cai) in ten_nam) and (chr(chu_cai) in ten_nu):
            dem=dem+1

        if dem == 0:
            ket_qua= "nguoi dung nuoc la"
        elif dem <3:
            ket_qua= "friend zone"
        else:
            ket_qua="Khit nhau"
            
            return ket_qua
        
        print("Nhap_ten_nam: ")
        ten_nam=input()
        print("Nhap_ten_nu: ")
        ten_nu=input()
        print(boi_toan_tinh_duyen(ten_nam,ten_nu))    
        print(ket_qua)  

