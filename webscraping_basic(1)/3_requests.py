import requests
# requests.get("http://naver.com")
res=requests.get("http://google.com")
# res=requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
print("response code: ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("Normal")
# else:
#     print("We have a problem. [error code", res.status_code, "]")


print(len(res.text))
print(res.text)
with open("mygoodle.html", "w", encoding="utf8") as f:
    f.write(res.text)