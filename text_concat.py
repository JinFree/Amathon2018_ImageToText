# -*- coding: utf-8 -*-

"""
 Created by IntelliJ IDEA.
 Project: ec2-user
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-20
 Time: 오후 9:20
"""


def text_concat(text_dto):
    string = ""

    if "WORD" == text_dto.type_:
        if text_dto.detected_test[-1] == ".":
            string += (text_dto.detected_test + "\n")
        else:
            string += (text_dto.detected_test + " ")

    return string


def text_line_concat(text_dto):
    string = ""
    if "LINE" == text_dto.type_:
        string += (text_dto.detected_test + "\n")
    return string
