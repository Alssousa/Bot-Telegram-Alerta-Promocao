from models import Base
from db_config import new_db


if __name__ == "__main__":
    new_db(Base)
    
