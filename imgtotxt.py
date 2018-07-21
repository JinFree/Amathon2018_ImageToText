import boto3
import img

import text_handling as th
import text_concat as tc


def img2txt(imageFile):
    client = boto3.client('rekognition')
    print(type(imageFile))
    image_path_list = img.imlist(imageFile)
    test = ''
    data_dict = dict()

    for imageFile in image_path_list:
        with open(imageFile, 'rb') as image:
            response = client.detect_text(Image={'Bytes': image.read()})
        # textDetections=response['TextDetections']
        text_dtos = th.get_dtos(response)
        # test = tc.TextConcat(text_dtos).text_line_concat()

        # for text in textDetections:
        for text_dto in text_dtos:
            test += tc.text_concat(text_dto)

        data_dict["data"] = response

    data_dict["text"] = test

    return data_dict

