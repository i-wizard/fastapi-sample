from database import BaseClass, engine
from models import Item

print("Creating database tables")

BaseClass.metadata.create_all(engine)
