# outfile = open("C:\\Users\\kcj30\\Desktop\\chEmployement\\pythonStudy\\phones.txt", "w",encoding="utf8")
# outfile.write("김창주 010-7755-3054\n")
# outfile.write("장채영 010-7755-3054\n")
# outfile.write("장채돌이 010-7755-3054\n")

# outfile.close()


# append 값을 덭붙여서 사용하기 
# outfile = open("out.txt", "a", encoding="utf8")
# outfile.write("과학 : 80\n")
# outfile.write("코딩 : 100")
# outfile.close()


# 읽기 

# outfile = open("out.txt", "r", encoding="utf8")
# print(outfile.read())   #전체 내용 읽기로 출력하기
# outfile.close()


from pygame import PixelArray


outfile = open("out.txt", "r", encoding="utf8")
print(outfile.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동  
print(outfile.readline(), end="")
print(outfile.readline(), end="")
print(outfile.readline(), end="")
outfile.close()



#파일이 몇줄인지 모른느 상태에서 리스트 형태로 담고 출력하기 
outfile = open("out.txt", "r", encoding="utf8")
lines = outfile.readlines()  # list형태로 저장 
for line in lines:
    print(line, end="")

outfile.close()

