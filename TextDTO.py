# -*- coding: utf-8 -*-

"""
 Created by IntelliJ IDEA.
 Project: conn
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-20
 Time: 오후 5:01
"""


class TextDTO(object):
    def __init__(self, **kwargs):
        self.confidence = kwargs["confidence"]
        self.detected_test = kwargs["detected_test"]
        self.height = kwargs["height"]
        self.left = kwargs["left"]
        self.top = kwargs["top"]
        self.width = kwargs["width"]
        self.polygons = kwargs["polygons"]
        self.id_ = kwargs["id_"]
        self.parentid = kwargs["parentid"]
        self.type_ = kwargs["type_"]

    def __str__(self):
        return "Confidence : {}\nDetectedTest: {}\nHeight: {}\nLeft: {}" \
               "\nTop: {}\nWidth: {}\nPolygons: {}\nId: {}\nParentId: {}\nType: {}" \
            .format(self.confidence,
                    self.detected_test,
                    self.height,
                    self.left,
                    self.top,
                    self.width,
                    self.polygons,
                    self.id_,
                    self.parentid,
                    self.type_
                    )
