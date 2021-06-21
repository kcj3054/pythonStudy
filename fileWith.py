# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")


# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# with를 사용하면 매번 close를 안해줘서 상관없다 



# 파일을 읽어 단어 별로 출력하기 
# split -> 띄어쓰기 단위로 split해준다 잘라준다,,,,,,,,,,,  

infile = open("study.txt", "r")
for line in infile:
    line = line.strip()    # strip 전달된 문자를 string의 왼쪽과 오른쪽에서 제거합니다. 
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()
