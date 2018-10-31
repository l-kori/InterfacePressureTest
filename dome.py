import requests


if __name__ == '__main__':
    url = "http://www.zhihu.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    print(response.text)


    url = "http://httpbin.org/post"
    data = {
        'name': 'jack',
        'age':'24'
    }
    response = requests.post(url,data = data)
    print(response.text)

    response = requests.get("http://www.baidu.com")
    #打印请求页面的状态码
    print(type(response.status_code),response.status_code)
    print(type(response.headers),response.headers)
    print(type(response.cookies),response.cookies)
    print(type(response.url),response.url)
    print(type(response.history),response.history)

    #内置状态码
    response = requests.get("http://www.jianshu.com/404.html")
    if response.status_code != requests.codes.ok:
        print("404")

    response1 =requests.get("http://www.jianshu.com")
    if response1.status_code == 200:
        print("200")
    else:
        print("1111")


    #获取cookies
    response = requests.get("http://www.baidu.com")
    print(response.cookies)
    for key,value in response.cookies.items():
        print(key,"==",value)