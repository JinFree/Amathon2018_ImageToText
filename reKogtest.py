# -*- coding: utf-8 -*-

import boto3
import imgtotxt
import json


def main(img):
    # client=boto3.client('rekognition')
    # bucket="amathon2018"
    # photo="input.png"
    # response = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

    # img = "book_input_1.png"
    data_dict = imgtotxt.img2txt(img)

    # imageFile="book_input_2.png"
    # imageFile="book_input_1.png"
    # print(data_dict["text"])

    # write in html
    #f = open("./board/trans/trans_text.html", 'w')

    # text = "<html><head></head><body>" + data_dict["text"] + "</body></html>"
    # f.write(text)
    # f.close()

    return data_dict["text"]


    ###############################################
    # 되면 할 것.
    # 이후 data_dict 의 결과를 json 으로 바꾸어서 jquery 로 수행
    # json_val = json.dumps(data_dict)
