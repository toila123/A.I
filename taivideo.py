import pytube
while True:
    a  = str(input("nhập link vào đây: "))
    b = str(input("nhập tên file: "))
    pytube.YouTube(url= a ).streams.get_highest_resolution().download(b)
    print('xong rồi đó')
    