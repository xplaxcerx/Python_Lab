from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# создаем движок базы данных и сессию
engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()

# создаем базовый класс для моделей
Base = declarative_base()

# модель "Дисциплины"
class Discipline(Base):
    __tablename__ = 'disciplines'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    lectures = Column(Integer)
    practices = Column(Integer)
    labs = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship('Department', back_populates='disciplines')

    def __repr__(self):
        return f"<Discipline(name='{self.name}', lectures='{self.lectures}', practices='{self.practices}', labs='{self.labs}')>"

# модель "Кафедры"
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    disciplines = relationship('Discipline', back_populates='department')

    def __repr__(self):
        return f"<Department(name='{self.name}')>"

# создаем таблицы в базе данных
Base.metadata.create_all(engine)

# заполняем базу данных тестовыми данными
department1 = Department(name='Department of Mathematics')
department2 = Department(name='Department of Physics')

discipline1 = Discipline(name='Algebra', lectures=30, practices=20, labs=10, department=department1)
discipline2 = Discipline(name='Analysis', lectures=40, practices=10, labs=5, department=department1)
discipline3 = Discipline(name='Quantum Mechanics', lectures=50, practices=15, labs=20, department=department2)

session.add_all([department1, department2, discipline1, discipline2, discipline3])
session.commit()
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///university.db', echo=True)
Base = declarative_base()

class Discipline(Base):
    __tablename__ = 'discipline'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lectures = Column(Integer)
    practices = Column(Integer)
    labs = Column(Integer)
    department = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

discipline1 = Discipline(name='Math', lectures=30, practices=15, labs=20, department='Mathematics')
discipline2 = Discipline(name='Physics', lectures=20, practices=10, labs=15, department='Physics')
discipline3 = Discipline(name='Chemistry', lectures=25, practices=20, labs=25, department='Chemistry')

session.add_all([discipline1, discipline2, discipline3])
session.commit()


print('База данных успешно создана и заполнена тестовыми данными.')
