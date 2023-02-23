import psycopg2

import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:arinaegor@localhost:5432/postgres"
engine = sqlalchemy.create_engine(DSN)

# создаем все наши таблицы
create_tables(engine)

# создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# заполняем наши таблицы
publisher = Publisher(name='Python')
session.add(publisher)
session.commit()



session.close()

# course1 = Course(name='Python')
# print(course1.id)
#
# session.add(course1)
# session.commit()
#
# print(course1.id)
# print(course1)
#
# hw1 = Homework(number=1, description='Простая домашняя работа', course=course1)
# hw2 = Homework(number=2, description='Сложная домашняя работа', course=course1)
# session.add_all([hw1, hw2])
# session.commit()
#
# #Выводим на экран все элементы таблицы
# for c in session.query(Homework).all():
#     print(c)
#
# #Выводим на экран отфильтрованные элементы таблицы
# for c in session.query(Homework).filter(Homework.number > 1).all():
#     print(c)
#
# for c in session.query(Homework).filter(Homework.description.like('%сложн%')).all():
#     print(c)
#
# for c in session.query(Homework).filter(Homework.description.like('%ост%')).all():
#     print(c)
#
# c2 = Course(name='Java')
# session.add(c2)
# session.commit()
#
# subq = session.query(Homework).filter(Homework.description.like('%сложн%')).subquery()
# for c in session.query(Course).join(subq, Course.id == subq.c.course_id).all():
#     print(c)
#
# session.query(Course).filter(Course.name == 'Java').update({'name': 'JavaScript'})
# session.commit()
#
# # session.query(Course).filter(Course.name == 'JavaScript').delete()
# # session.commit()
#
# for c in session.query(Course).all():
#     print(c)


session.close()



# # создание объектов
# js = Course(name="JavaScript")
# print(js.id)
# hw1 = Homework(number=1, description="первое задание", course=js)
# hw2 = Homework(number=2, description="второе задание (сложное)", course=js)
#
# session.add(js)
# print(js.id)
# session.add_all([hw1, hw2])
# session.commit()  # фиксируем изменения
# print(js.id)
#
#
# # запросы
# q = session.query(Course).join(Homework.course).filter(Homework.number == 1)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)
#
# # вложенный запрос
# subq = session.query(Homework).filter(Homework.description.like("%сложн%")).subquery("simple_hw")
# q = session.query(Course).join(subq, Course.id == subq.c.course_id)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)
#
#
# # обновление объектов
# session.query(Course).filter(Course.name == "JavaScript").update({"name": "NEW JavaScript"})
# session.commit()  # фиксируем изменения
#
#
# # удаление объектов
# session.query(Homework).filter(Homework.number > 1).delete()
# session.commit()  # фиксируем изменения