#打开网页
def open_url(url):
    pass

#获取response的图片url
def get_picture_url(http_response):
    pass

#url 构建
def url_join(picture_url):
    pass

#保存 url
def save_image(url,addr):
    pass

def main():
    http_response=open_url("urlAddress")
    temp_picture_url=get_picture_url(http_response)
    picture_url=url_join(temp_picture_url)
    save_image(picture_url," Address")


if __name__=='__main__':
    main()
