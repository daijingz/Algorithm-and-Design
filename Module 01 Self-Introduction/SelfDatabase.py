# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Self database 1: SQL database
import mysql.connector

# Username: root
# password: 20000517
# port number: 127.0.0.1 (3306)
connection1 = mysql.connector.connect(user='root', password='20000517',
                                      host='127.0.0.1',
                                      database='jingzedai')

cursor1 = connection1.cursor(buffered=True)

delete1 = "DELETE FROM basic_info "

record1 = ("INSERT INTO basic_info "
           "VALUES ('0', 'Jingze', 'Dai', '3658885882', 1, 'China', 'Canada', "
           "'McMaster University', 'Mathematics', '3.41')")
record2 = ("INSERT INTO basic_info "
           "VALUES ('1', 'Jingze', 'Dai', '9055984864', 1, 'China', 'Canada', "
           "'McMaster University', 'Computer Science', '3.41')")
record3 = ("INSERT INTO basic_info "
           "VALUES ('2', 'Jingze', 'Dai', '4168417893', 1, 'China', 'Canada', "
           "'McMaster University', 'Computer Science', '3.41')")

cursor1.execute(delete1)

connection1.commit()

cursor1.execute(record1)

connection1.commit()

cursor1.execute(record2)

connection1.commit()

cursor1.execute(record3)

connection1.commit()

delete2 = "DELETE FROM edu_info "

cursor1.execute(delete2)

connection1.commit()

record4 = ("INSERT INTO edu_info "
           "VALUES ('0', 'McMaster University', 'Honors Computer Science Coop')")

cursor1.execute(record4)

connection1.commit()

delete3 = "DELETE FROM basic_program_skills "

cursor1.execute(delete3)

connection1.commit()

record5 = ("INSERT INTO basic_program_skills "
           "VALUES ('0', 'Python', '3.0')")

cursor1.execute(record5)

connection1.commit()

record6 = ("INSERT INTO basic_program_skills "
           "VALUES ('1', 'Java', '3.0')")

cursor1.execute(record6)

connection1.commit()

record7 = ("INSERT INTO basic_program_skills "
           "VALUES ('2', 'C++', '2.0')")

cursor1.execute(record7)

connection1.commit()

record8 = ("INSERT INTO basic_program_skills "
           "VALUES ('3', 'C', '1.0')")

cursor1.execute(record8)

connection1.commit()

delete4 = "DELETE FROM assem_program_skills "

cursor1.execute(delete4)

connection1.commit()

record9 = ("INSERT INTO assem_program_skills "
           "VALUES ('0', 'MIPS32', '1.0')")

cursor1.execute(record9)

connection1.commit()

record10 = ("INSERT INTO assem_program_skills "
            "VALUES ('1', 'NASM', '1.0')")

cursor1.execute(record10)

connection1.commit()

delete5 = "DELETE FROM pro_tools "

cursor1.execute(delete5)

connection1.commit()

record11 = ("INSERT INTO pro_tools "
            "VALUES ('0', 'Git', 1)")

cursor1.execute(record11)

connection1.commit()

record12 = ("INSERT INTO pro_tools "
            "VALUES ('1', 'JSON', 1)")

cursor1.execute(record12)

connection1.commit()

record13 = ("INSERT INTO pro_tools "
            "VALUES ('2', 'Linux', 1)")

cursor1.execute(record13)

record14 = ("INSERT INTO pro_tools "
            "VALUES ('3', 'Unix', 1)")

cursor1.execute(record14)

connection1.commit()

record15 = ("INSERT INTO pro_tools "
            "VALUES ('4', 'Jupyter Hub', 1)")

cursor1.execute(record15)

connection1.commit()

delete6 = "DELETE FROM web_program_skills "

cursor1.execute(delete6)

connection1.commit()

cursor1.close()

connection1.close()