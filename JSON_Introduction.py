import json

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
Information11 = '{ "Machine Learning": "1-year with certificates from taking courses" }'
Information12 = '{ "LinkedIn Webpage": "https://www.linkedin.com/in/jingze-dai/" }'
Information13 = '{ "Github Webpage": "https://github.com/daijingz" }'


def display_Basic_Information():
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
    print("************************************************************************")


display_Basic_Information()
display_Programming_Languages()
display_Assembly_Languages()
display_Professional_Tools()
display_Web_Programming()
display_Computer_Graphics()
display_Data_Science()
display_Other_Skills()