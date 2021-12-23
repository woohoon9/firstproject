import os


# print(os.getcwd())

# os.chdir("RPA_Basic") # RPA-Basic으로 작업 공간 이동
# print(os.getcwd())

# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())


# os.chdir("../..") # 조부모 폴더로 이동  ../../../../../
# print(os.getcwd())

# os.chdir("c:/")
# print(os.getcwd())


# 파일 경로  만들기
# open("c:/Users/../.../")
# file_path=os.path.join(os.getcwd(), "my_file.txt") #절대 경로 생성
# print(file_path)


# #파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\jwoo\Desktop\PythonWorkspace\my_file.txt"))

# 파일 정보 가져 오기
# import time
# import datetime
#파일 생성 날짜

# file_path = "RPA_Basic/2_Desktop/11_file_system.py"
# ctime = os.path.getctime(file_path)
# print(ctime)
# #날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))


# 파일 크기
# size= os.path.getsize(file_path)
# print(size)


# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("RPA_Basic")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일목록 가져오기(하위 폴더 모두 포함)
# # result = os.walk("RPA_Basic")
# result = os.walk(".") # 현재 폴더에 있는 파일을 가지고 오고 싶으면 "." 찍으면 된다. 
# print(result)

# # for root, dirs, files in result:
# #     print(root, dirs, files)

# # 만약 폴더 내에서 특정 파일들을 찾으려면?
# name ="11_file_system.py"
# result=[]

# for root, dirs, files in os.walk("RPA_Basic"):
#     #[a.text, b.text,c.text, 11_file_system.py. ....]
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
#*.xlsx, *.txt, 자동화*.png... 
# import fnmatch
# pattern = "file*.png"
# result = []

# for root, dirs, files in os.walk("."):
#     #[a.text, b.text,c.text, 11_file_system.py. ....]    
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))
# print(result)


# 주어진 경로가 피일인지? 폴더인지?
# print(os.path.isdir("RPA_Basic"))
# print(os.path.isfile("RPA_Basic"))

# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))

# 만약에 지정된 경로레 해당하는 파일/폴더가 없다면?
# print(os.path.isdir("run_bttnnn.png"))

# # 주어진 경로가 존재하는지?
# if os.path.exists("run_btn.png"):
#     print("A file or folder exists.")
# else:
#     print("Any of them does not exist.")

# 파일 만들기
# open("new_file.txt", "a").close() #빈 파일 생성

# # 파일명 바꾸기
# os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt -> new_file_rename.txt

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# # 폴더 만들기
# os.mkdir("new_folder")
# os.mkdir("c:/Users/jwoo/Desktop/PythonWorkspace") # 절대 경로 기준으로 폴더 생성
# os.mkdir("new_folders/a/b/c") # 실패: 하위 폴더를 가지는 폴더 생성 시도 실패
# os.makedirs("new_folders/a/b/c") # 성공 : 하위 폴더를 가지는 폴더 생성 시도

# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folders") # 폴더 안이 비었을때만 삭제 가능
import shutil # shell utilities
# shutil.rmtree("new_folders") # 폴더 안이 비어 있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의!!!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png", "test_folder")# 원본 경로, 대상 폴더 경로
# 어떤 파일을 폴더안 에 새로운 파일 이름으로 복사하기
# shutil.copy("run_btn.png", "test_folder/copied_run_btn.png")# 원본 파일 경로, 대상

# shutil.copyfile("run_btn.png","test_folder\copied_run_btn_2.png") # 원본 파일 경로 및 파일 경로를 모두 써야 함

# shutil.copy2("run_btn.png", "test_folder/copied.png") # 원본 파일 경류, 대상 폴더 (파일)

# os.chdir("c:/Users/jwoo/Desktop/PythonWorkspace")

# copy, copyfile: 메타 정보복사 X
# copy2: 메타 정보 포함













