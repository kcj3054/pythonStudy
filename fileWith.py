# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")


with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# with를 사용하면 매번 close를 안해줘서 상관없다 
