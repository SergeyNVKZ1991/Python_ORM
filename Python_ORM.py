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
    publisher_name = 'Reilly'
    for c in session.query(Publisher.name, Book.title, Sale.price, Sale.date_sale).join(Book.publisher).join(Sale.stock).filter(Publisher.name.like(f'%{publisher_name}%')).all():
        print(f'{c[0]} | {c[1]} | {c[2]} | {c[3]}')
get_sales()
