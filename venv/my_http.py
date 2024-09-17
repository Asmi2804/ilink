
import requests
# get method
get = requests.get("https://jsonplaceholder.typicode.com/posts/")
print(get.status_code)
print(get.text)

# post method
info={"userId":11,
      "title": "Python Programming"}
post=requests.post("https://jsonplaceholder.typicode.com/posts/", data=info)
print(post.text)

# put method
info1={"userId":4,
       "title":"Java Programming"}
put=requests.put("https://jsonplaceholder.typicode.com/posts/10",data=info1)
print(put.text)
print(put.json())
 
# delete method
delete=requests.delete("https://jsonplaceholder.typicode.com/posts/12")
print(delete.text)

