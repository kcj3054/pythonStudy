import pickle
# profile_file = open("profile.pickle", "wb")  # pickle에서는 따로 encoding이 필요없다, pickle은 항상 wb로 해야한다 , pickle 프로그램상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장
# profile = {"이름" :"박명수", "나이" : 30}
# pickle.dump(profile, profile_file)
# profile_file.close()


profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profileㅇ ㅔ불러오기 
print(profile)
profile_file.close()
