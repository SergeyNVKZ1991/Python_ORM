import psycopg2

import json

import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = "postgresql://postgres:arinaegor@localhost:5432/postgres"
engine = sqlalchemy.create_engine(DSN)

# создаем все наши таблицы
create_tables(engine)

# создаем сессию
Session = sessionmaker(bind=engine)
session = Session()


with open('test_date.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

# publisher_name = input("Введите название издательства: ")
publisher_name = "R"

subq = session.query(Publisher).filter(Publisher.name.like(f'%{publisher_name}%')).subquery()
book = session.query(Book).join(subq, Book.id == subq.c.id).all()
shop = session.query(Shop).join(subq, Shop.id == subq.c.id).all()

# stock = session.query(Stock).join(subq, Stock.id == subq.c.id).all()
sale = session.query(Sale).join(subq, Sale.id == subq.c.id).all()

print(sale)

# date = {"book": [], "shop": [], }
# for b in book:
#     date["book"].append(b.title)
#
# for s in shop:
#     date["shop"].append(s.name)
# for v in date:
#
# print(date)

session.close()

# # заполняем наши таблицы
# publisher = Publisher(name='Python')
# session.add(publisher)
# session.commit()





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