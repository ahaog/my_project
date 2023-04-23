from datetime import datetime
import create_table as ct

testData = [["user1", 100, 10.1, "2010-10-10 21:16:57.720240", "RUS"],
            ["user2", 200, 20.2, "2020-10-10 21:16:57.720240", "ENG"],
            ["user3", 300, 30.3, "2030-10-10 21:16:57.720240", "RUS"],
            ["user4", 400, 40.4, "2040-10-10 21:16:57.720240", "RUS"],
            ["user5", 500, 50.5, "2050-10-10 21:16:57.720240", "ENG"]]

db_sess = ct.sa.orm.create_session(bind=ct.engine)

data_taken = []


def add_to_table(list_values):
    for index, received_data in enumerate(list_values, start=1):

        stud = ct.Students()
        static = ct.Statistics()

        student_index = 0

        stud.name = received_data[0]
        static.speed = received_data[1]
        static.authenticity = received_data[2]
        static.last_entry_time = datetime.strptime(received_data[3], "%Y-%m-%d %H:%M:%S.%f").date()
        static.print_language = received_data[4]

        for student_ib_base in db_sess.query(ct.Students).filter(ct.Students.name.like(received_data[0])):
            student_index = student_ib_base.id
            break

        if student_index > 0:
            for statistics_in_base in db_sess.query(ct.Statistics).filter(ct.Statistics.user_id == student_index):
                db_sess.delete(statistics_in_base)
                break

        else:
            db_sess.add(stud)

        db_sess.commit()

        if student_index > 0:
            static.user_id = student_index

        else:
            static.user_id = stud.id

        db_sess.add(static)

        db_sess.commit()


# add_to_table(testData)


def taking_data(name_of_student, list_of_values):
    for student_ib in db_sess.query(ct.Students).filter(ct.Students.name.like(name_of_student)):
        id_of_student = student_ib.id
        for statistics_in_base in db_sess.query(ct.Statistics).filter(ct.Statistics.user_id == id_of_student):
            list_of_values.append(statistics_in_base.speed)
            list_of_values.append(statistics_in_base.authenticity)
            list_of_values.append(statistics_in_base.last_entry_time)
            list_of_values.append(statistics_in_base.print_language)


taking_data("user2", data_taken)
print(data_taken)

"""
for i in db_sess.query(ct.Statistics).all():
     db_sess.delete(i)
     db_sess.commit()

for i in db_sess.query(ct.Students).all():
     db_sess.delete(i)
     db_sess.commit()
     
     
     
    stud = ct.Students()
    stud.name = testData[0][0]
    static = ct.Statistics()
    static.speed = testData[0][1]
    static.authenticity = testData[0][2]
    static.last_entry_time = datetime.strptime(testData[0][3], "%Y-%m-%d %H:%M:%S.%f").date()
    static.print_language = testData[0][4]
    
    
    
    
    for students_in_base in db_sess.query(ct.Students).filter(ct.Students.name.like(testData[0])):
    student_index = students_in_base.id
    break

    if student_index > 0:
        for statistics_in_base in db_sess.query(ct.Statistics).filter(ct.Statistics.user_id == student_index):
            db_sess.delete(statistics_in_base)
            db_sess.commit()
    
    else:
        db_sess.add(stud)
        db_sess.commit()
        student_index = stud.id
    
    static.user_id = student_index
    db_sess.add(static)
    db_sess.commit()
"""
