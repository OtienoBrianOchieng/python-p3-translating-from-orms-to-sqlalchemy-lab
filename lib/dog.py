from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)
    

def save(session, dog):
    session =session()
    session.add(dog)
    session.commit()
    

def get_all(session):
    return session().query(Dog).all()
    

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name==name).all()


def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

    

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).all()

def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()
    pass