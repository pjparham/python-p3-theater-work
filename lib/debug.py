#!/usr/bin/env python3


import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Role, Audition



if __name__ == '__main__':
    
    engine = create_engine('sqlite:///migrations_test.db')  
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Role).delete()
    session.query(Audition).delete()

    cinderella = Role(character_name="Cinderella", id=1)
    belle = Role(character_name="Belle", id=2)

    margot = Audition(id=1, actor="Margot Robbie", location="LA", phone=123, hired=False, role_id=1)
    lisa = Audition(id=2, actor="Lisa", location="NYC", phone=456, hired=False, role_id=1)
    shelia = Audition(id=3, actor="Shelia", location="Arizona", phone=984, hired=False, role_id=2)
    mary = Audition(id=4, actor="Mary", location="Hawaii", phone=93248, hired=False, role_id=2)

    session.add_all([cinderella, belle, margot, lisa, shelia, mary])
    session.commit()

    import ipdb; ipdb.set_trace()


