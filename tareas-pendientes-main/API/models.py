#https://docs.sqlalchemy.org/en/14/orm/quickstart.html
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import Table

class Base(DeclarativeBase):
   pass

class Usuario(Base):
    __tablename__ = "user_account"
    nombre_usuario = Column(String(30), primary_key = True)
    numero_whatsapp = Column(String(8), nullable=True)
    correo_electronico = Column(String(8), nullable=False)
    tareas = relationship(
        "Tarea",back_populates="Usuario", cascade ="all, delete-orphan"
)
###

association_table = Table(
    "association",
    Base.metadata,
    Column("left_id", ForeignKey("tarea.id")),
    Column("right_id", ForeignKey("tipo_tarea.nombre")),
    
)

class Tarea(Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(30))#, primary_key = True)
    fecha_inicio = Column(String(30))
    fecha_entrega = Column(String(30))
    referencia_usuario = Column(String(30), ForeignKey("user_account.nombre_usuario"), nullable=False)
    usuario = relationship("User", back_populates="tareas")
    tipo = relationship("Tipo", secondary=association_table)


class Tipo_tarea(Base):
     __tablename__ = "tipo_tarea"
     #id = Column(Integer, primary_key=True)
     fecha_creacion = Column(Date)
     nombre = Column(String(30),primary_key=True)


