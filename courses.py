import os
import wget
import json

def file_name_format(file_name) :
    new_name = file_name.replace('/', '')
    for c in ['?', '*', ':', '|', '>', '<', ''] :
        new_name = new_name.replace(c, '')
    return new_name

with open('Courses.json') as f:
    data = json.load(f)

    for subject in data :
        subject_name = subject["designation"]
        courses = subject["courses"]
        download_path = "C:/Users/amira/OneDrive/Bureau/LSI/3LSI/"+subject_name.split(" /")[0]
        os.mkdir(download_path)

        for course in courses :
            course_name = course["title"]
            file_name = file_name_format(course_name)
            course_url = "https://issatso.rnu.tn/bo/storage/app/public/courses/"+course["folder"].split("/")[1]
            wget.download(course_url, download_path+"/"+file_name+".pdf")
            print(download_path)          
