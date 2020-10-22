import requests
# from concurrent import 

urls = [
    'https://www.newsmth.net/nForum/#!board/Python?p={}'.format(num+1) for num in range(30)
]

print(urls)