import requests
def get_image_from_url(url, file_name):
    with open(file_name,"wb") as fichero:
        rq = requests.get(url)
        fichero.write(rq.content)
        

