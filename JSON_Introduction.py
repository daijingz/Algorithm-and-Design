import json
import re
import urllib.request

# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Basic Information of Jingze Dai
Information1 = '{ "Name": "Jingze Dai", "School": "McMaster University", "MacID": "daij24" }'
Information2 = '{ "Program": "Honors Computer Science program (co-op)" }'
Information3 = '{ "Student Number": 400201059, "Email Address": "daij24@mcmaster.ca" }'
Information4 = '{ "Programming Languages": [ "Python", "Java", "C", "C++" ] }'
Information5 = '{ "Assembly Languages": [ "MIPS32", "NASM" ] }'
Information6 = '{ "Professional Tools": [ "Git", "JSON", "Unit Testing" ] }'
Information7 = '{ "Web Programming": [ "Javascript", "CSS", "HTML5", "Node.js", "React" ] }'
Information8 = '{ "Computer Graphics": [ "OpenGL", "Unity" ] }'
Information9 = '{ "Database and Data Science": [ "MATLAB", "Oracle", "MySQL" ] }'
Information10 = '{ "Others": [ "Scala", "Ruby", "Haskell" ] }'
Information11 = '{ "Machine Learning": "1-year learning experience with certificates from Stanford University" }'
Information12 = '{ "Data Science": "1-year learning experience with certificates from IBM" }'
Information13 = '{ "LinkedIn Webpage": "https://www.linkedin.com/in/jingze-dai/" }'
Information14 = '{ "Github Webpage": "https://github.com/daijingz" }'


def display_Basic_Information():
    """! Displaying basic information"""
    print("************************************************************************")
    print()
    Output1 = json.loads(Information1)
    print("Name: " + Output1["Name"])
    print()
    print("School: " + Output1["School"])
    print()
    print("MacID: " + Output1["MacID"])
    print()
    Output2 = json.loads(Information2)
    print("Program: " + Output2["Program"])
    print()
    Output3 = json.loads(Information3)
    print("Student Number: " + str(Output3["Student Number"]))
    print()
    print("Email Address: " + str(Output3["Email Address"]))
    print()
    print("************************************************************************")


def display_Programming_Languages():
    """! Displaying interests about high-level programming languages"""
    print("************************************************************************")
    print()
    print("Programming Languages: ")
    Output4 = json.loads(Information4)
    print()
    print(Output4["Programming Languages"][0])
    print()
    print(Output4["Programming Languages"][1])
    print()
    print(Output4["Programming Languages"][2])
    print()
    print(Output4["Programming Languages"][3])
    print()
    print("************************************************************************")


def display_Assembly_Languages():
    """! Displaying interests about assembly programming languages"""
    print("************************************************************************")
    print()
    print("Assembly Languages: ")
    Output5 = json.loads(Information5)
    print()
    print(Output5["Assembly Languages"][0])
    print()
    print(Output5["Assembly Languages"][1])
    print()
    print("************************************************************************")


def display_Professional_Tools():
    """! Displaying interests about professional tools"""
    print("************************************************************************")
    print()
    print("Professional Tools: ")
    Output6 = json.loads(Information6)
    print()
    print(Output6["Professional Tools"][0])
    print()
    print(Output6["Professional Tools"][1])
    print()
    print(Output6["Professional Tools"][2])
    print()
    print("************************************************************************")


def display_Web_Programming():
    """! Displaying interests about web programming languages"""
    print("************************************************************************")
    print()
    print("Web Programming: ")
    Output7 = json.loads(Information7)
    print()
    print(Output7["Web Programming"][0])
    print()
    print(Output7["Web Programming"][1])
    print()
    print(Output7["Web Programming"][2])
    print()
    print(Output7["Web Programming"][3])
    print()
    print(Output7["Web Programming"][4])
    print()
    print("************************************************************************")


def display_Computer_Graphics():
    """! Displaying interests about computer graphics"""
    print("************************************************************************")
    print()
    print("Computer Graphics: ")
    Output8 = json.loads(Information8)
    print()
    print(Output8["Computer Graphics"][0])
    print()
    print(Output8["Computer Graphics"][1])
    print()
    print("************************************************************************")


def display_Data_Science():
    """! Displaying interests about data science"""
    print("************************************************************************")
    print()
    print("Database and Data Science: ")
    Output9 = json.loads(Information9)
    print()
    print(Output9["Database and Data Science"][0])
    print()
    print(Output9["Database and Data Science"][1])
    print()
    print(Output9["Database and Data Science"][2])
    print()
    print("************************************************************************")


def display_Other_Skills():
    """! Displaying interests about other useful skills"""
    print("************************************************************************")
    print()
    print("Other skills: ")
    Output10 = json.loads(Information10)
    print()
    print(Output10["Others"][0])
    print()
    print(Output10["Others"][1])
    print()
    print(Output10["Others"][2])
    print()
    Output11 = json.loads(Information11)
    print("Machine Learning: " + str(Output11["Machine Learning"]))
    print()
    Output12 = json.loads(Information12)
    print("Data Science: " + str(Output12["Data Science"]))
    print()
    print("************************************************************************")


def display_LinkedIn():
    """! Open linkedIn webpage"""
    Output13 = json.loads(Information13)
    return urllib.request.urlopen(str(Output13["LinkedIn Webpage"]))


def display_Github():
    """! Open github webpage"""
    Output14 = json.loads(Information14)
    return urllib.request.urlopen(str(Output14["Github Webpage"]))


def Welcome():
    """! Overall function"""
    username = input("Enter username: ")
    print("Welcome: " + username + "!!!")
    print("Here is David's homepage. What do you want to know about David?")
    information = input("Information you want to know: ")

    if re.search('^Basic.*', information):
        display_Basic_Information()
        Welcome()
    elif re.search('^basic.*', information):
        display_Basic_Information()
        Welcome()
    elif re.search('^Programming.*', information):
        display_Programming_Languages()
        Welcome()
    elif re.search('^programming.*', information):
        display_Programming_Languages()
        Welcome()
    elif re.search('^Assem.*', information):
        display_Assembly_Languages()
        Welcome()
    elif re.search('^assem.*', information):
        display_Assembly_Languages()
        Welcome()
    elif re.search('^Tool.*', information):
        display_Professional_Tools()
        Welcome()
    elif re.search('^tool.*', information):
        display_Professional_Tools()
        Welcome()
    elif re.search('^Web.*', information):
        display_Web_Programming()
        Welcome()
    elif re.search('^web.*', information):
        display_Web_Programming()
        Welcome()
    elif re.search('^end.*', information):
        print()
    else:
        print("Error: Information Category not Founded")
        exitOrNot = input("Do you want to continue searches? ")
        if re.search('^yes.*', exitOrNot) or re.search('^Yes.*', exitOrNot):
            Welcome()
        else:
            print()


Welcome()