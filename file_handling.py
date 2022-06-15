import os,json

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

def get_text():
    # Open a file 
    # adding to the end of the content...creates a new file if it dosent exsisit
    text_file = open('./assets/text.txt','a')
    # Open a file for reading
    txt = text_file.read()
    # Close the file
    print(txt)
    text_file.close()


def write_txt():
    # replaces file content...creates a new file if it dosent exsisit
    text_file = open('./assets/text.txt','w')
    text_file.write('This is a new line')
    print(text_file.read())
    text_file.close()

# delete file
def delete():
    try:
        os.remove('./assets/del.txt')
    except:
        print('err file not found')
        
# delete()
# write_txt()

# changing json to dictionary
# import the json moduletop
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dict = json.loads(person_json)

# changing dictionary to json
change_back = json.dumps(person_dict, indent=2) # indent could be 2, 4, 8. It beautifies the json