import psycopg2
import json
import sqlalchemy
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

def get_sales():
    # publisher_name = input('Введите имя издателя, факты покупки книг которого вы хотиите получь: ')
    publisher_name = 'P'
    queru = session.query(Publisher, Book, Shop, Sale).join(Book).join(Stock).join(Shop).join(Sale).filter(Publisher.name.like(f'%{publisher_name}%')).all()
    for c in queru:
        print(f'{c.Book.title} | {c.Shop.name} | {c.Sale.price} | {c.Sale.date_sale}')
get_sales()
