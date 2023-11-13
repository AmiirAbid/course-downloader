import os
import wget
import json

# Function to format file names
def file_name_format(file_name):
    # Remove special characters from file name
    new_name = file_name.replace('/', '')
    for c in ['?', '*', ':', '|', '>', '<', '']:
        new_name = new_name.replace(c, '')
    return new_name

# Read data from Courses.json
with open('Courses.json') as f:
    data = json.load(f)

    # Loop through subjects in the data
    for subject in data:
        subject_name = subject["designation"]
        courses = subject["courses"]
        
        # Set the download path
        download_path = "C:/Users/amira/OneDrive/Bureau/LSI/3LSI/" + subject_name.split(" /")[0]
        os.mkdir(download_path)  # Create a directory for each subject

        # Loop through courses in the subject
        for course in courses:
            course_name = course["title"]
            file_name = file_name_format(course_name)  # Format the file name
            course_url = "https://issatso.rnu.tn/bo/storage/app/public/courses/" + course["folder"].split("/")[1]
            
            # Download the course PDF
            wget.download(course_url, download_path + "/" + file_name + ".pdf")
            print(download_path)  # Print the download path
