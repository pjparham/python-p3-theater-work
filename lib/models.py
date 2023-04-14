from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean(), default=False)
    role_id = Column(Integer(), ForeignKey('roles.id'))

    def __repr__(self):
        return f'Audition(id={self.id}, ' + \
            f'actor={self.actor}, ' + \
            f'hired={self.hired}, ' + \
            f'location={self.location})'
    
    def call_back(self):
        self.hired = True

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    character_name = Column(String())

    auditions = relationship('Audition', backref=backref('role'))

    def __repr__(self):
        return f'Role(id={self.id}, ' + \
            f'character={self.character_name}) ' 
    
    def actors(self):
        actor_names = [audition.actor for audition in self.auditions]
        return actor_names
        # result = list()
        # for actor in self.auditions:
        #     result.append(actor.actor)
        # return result
        # result = map(lambda x: x.actor, self.auditions)
        # return result

    def locations(self):
        all_locations = [audition.location for audition in self.auditions]
        return all_locations

    def lead(self):
        for actor in self.auditions:
            if actor.hired == True:
                return actor
            else:
                return "no actor has been hired for this role."
            
    def understudy(self):
        cast = list()
        for actor in self.auditions:
            if actor.hired == True:
                cast.append(actor)
        if len(cast) > 1:
            return cast[1]
        else:
            return 'no actor has been hired for understudy for this role.'