from datetime import datetime
import create_table as ct

testData = ["user2", 88888, 333333, "2030-10-10 21:16:57.720240", "EN"]

student_index = 0

db_sess = ct.sa.orm.create_session(bind=ct.engine)

stud = ct.Students()
stud.name = testData[0]
static = ct.Statistics()
static.speed = testData[1]
static.authenticity = testData[2]
static.last_entry_time = datetime.strptime(testData[3], "%Y-%m-%d %H:%M:%S.%f").date()
static.print_language = testData[4]

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
for i in db_sess.query(ct.Statistics).all():
     db_sess.delete(i)
     db_sess.commit()

for i in db_sess.query(ct.Students).all():
     db_sess.delete(i)
     db_sess.commit()

"""
