#Vương Zen-2380602639
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dòng đã nhập khi chuyển thành chữ in hoa là: ")
for line in lines:
    print(line.upper())