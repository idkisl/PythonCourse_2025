from data import db_sessions

from data.student import Student
from data.grade import Grade



def main():
    db_sessions.global_init("db/people.db")

    db_sess = db_sessions.create_session()
    st1 = Student()
    st1.name = "Студент 1"
    st1.surname = "1"
    
    db_sess.add(st1)
    db_sess.commit()

    '''person = db_sess.query(Student).first()
    print(person.name)
    '''
    for person in db_sess.query(Student).all():
        print(person.surname, person.name)
    '''
    print()
    for person in db_sess.query(Student).filter(Student.surname == "Кисляков"):
        print(person)'''


    mark1 = Grade()
    mark1.mark = 7
    mark1.student = db_sess.query(Student).filter(Student.id == 1).first()
    db_sess.add(mark1)
    db_sess.commit()


if __name__ == '__main__':
    main()