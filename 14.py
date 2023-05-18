from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()
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

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    disciplines = relationship('Discipline', back_populates='department')

    def __repr__(self):
        return f"<Department(name='{self.name}')>"

Base.metadata.create_all(engine)

department1 = Department(name='Department of Mathematics')
department2 = Department(name='Department of Physics')

discipline1 = Discipline(name='Algebra', lectures=30, practices=20, labs=10, department=department1)
discipline2 = Discipline(name='Analysis', lectures=40, practices=10, labs=5, department=department1)
discipline3 = Discipline(name='Quantum Mechanics', lectures=50, practices=15, labs=20, department=department2)

session.add_all([department1, department2, discipline1, discipline2, discipline3])
session.commit()

def execute_user_query():
    user_query = input("Введите запрос в форме Sql: ")
    result = session.execute(text(user_query))
    for row in result:
        print(row)

execute_user_query()

session.close()
