print("python", "java", sep=",", end="?")  #end는 출력의 마지막 줄을 " "안에 있는 것으로 설저아겠다는 뜻 



#시험 성적 
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():         #items 하면 튜플의 key, value 값들로  나오게 된다 
    print(subject.ljust(8), str(score).rjust(4), sep=":")



#은행 대기순번표 
#001, 002, 003 ...

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))     #zfill(3) 크기가 3인만큼 하는데 남은 빈 공간은 0으로 채우라는뜻 
