from sqlalchemy import create_engine, text
#from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://admin:admin@localhost:5432/po_db')
#Session = sessionmaker(bind=engine)
#session = Session()


with engine.connect() as con:
    query = """
    SELECT * FROM users;
    """

    statement = text(query)

    result = con.execute(statement)
    print(result.fetchall())
