# -*- coding: utf-8 -*-

import json
import TextDTO as tdto

"""
 Created by IntelliJ IDEA.
 Project: conn
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-20
 Time: 오후 5:00
"""

"""
{
   "TextDetections": [ 
      { 
         "Confidence": number,
         "DetectedText": "string",
         "Geometry": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Polygon": [ 
               { 
                  "X": number,
                  "Y": number
               }
            ]
         },
         "Id": number,
         "ParentId": number,
         "Type": "string"
      }
   ]
}
"""


def __text_handling(response):
    # json_val = json.loads(response)
    # text_detections = json_val["TextDetections"]

    text_detections = response["TextDetections"]

    text_dtos = list()
    for text_detection in text_detections:
        polygons = list()

        confidence = text_detection["Confidence"]
        detected_test = text_detection["DetectedText"]
        geometry = text_detection["Geometry"]
        id_ = text_detection["Id"]
        if "ParentId" in text_detection:
            parentid = text_detection["ParentId"]
        else:
            parentid = None
        type_ = text_detection["Type"]

        bounding_box = geometry["BoundingBox"]

        height = bounding_box["Height"]
        left = bounding_box["Left"]
        top = bounding_box["Top"]
        width = bounding_box["Width"]

        polygons_list = geometry["Polygon"]
        for polygon in polygons_list:
            x = polygon["X"]
            y = polygon["Y"]
            polygons.append((x, y))

        # Making DTO
        text_dto = tdto.TextDTO(
            confidence=confidence,
            detected_test=detected_test,
            height=height,
            left=left,
            top=top,
            width=width,
            polygons=polygons,
            id_=id_,
            parentid=parentid,
            type_=type_
        )

        text_dtos.append(text_dto)
    return text_dtos


def get_dtos(response):
    return __text_handling(response)
