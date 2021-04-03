from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, sessionmaker
from Audio import Song,PodCast,AudioBook
from Factory import FactoryClass as f
from flask import jsonify

# mysql database

engine = create_engine("sqlite:///E:\Fidel\\Audio.db")
# metadata
metadata = MetaData()

# table
Song_table = Table("Song", metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(100), nullable=False),
                        Column("duration", Integer, nullable=False),
                        Column("uploadTime", String, nullable=False)
                        )
Podcast_table = Table("PodCast", metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String(100), nullable=False),
                        Column("duration", Integer, nullable=False),
                        Column("host", String, nullable=False),
                        Column("uploadTime", String, nullable=False),
                        Column("participants", String, nullable=False)
                        )

AudioBook_table = Table("AudioBook", metadata,
                        Column('id', Integer, primary_key=True),
                        Column('title', String(100), nullable=False),
                        Column("duration", Integer, nullable=False),
                        Column("author", String, nullable=False),
                        Column("uploadTime", String, nullable=False),
                        Column("narrator", String, nullable=False)
                        )

# mapping
mapper(Song, Song_table, properties={
    'id': Song_table.c.id,
    'name': Song_table.c.name,
    'duration': Song_table.c.duration,
    'uploadTime': Song_table.c.uploadTime,
})

mapper(PodCast, Podcast_table, properties={
    'id': Podcast_table.c.id,
    'name': Podcast_table.c.name,
    'duration': Podcast_table.c.duration,
    'uploadTime': Podcast_table.c.uploadTime,
    'host': Podcast_table.c.host,
    'participants': Podcast_table.c.participants,
})

mapper(AudioBook, AudioBook_table, properties={
    'id': AudioBook_table.c.id,
    'title': AudioBook_table.c.title,
    'duration': AudioBook_table.c.duration,
    'uploadTime': AudioBook_table.c.uploadTime,
    'author': AudioBook_table.c.author,
    'narrator': AudioBook_table.c.narrator,
})



# session factory
def getSession():
    Session = sessionmaker()
    Session.configure(bind=engine)
    return Session()



def create_utility(object):
    session=getSession()
    session.add(object)
    session.commit()
    session.close()

def update_utility(type,id,audioFileMetadata):
    session = getSession()
    type=f.getClass(type)
    obj=session.query(type).filter(type.id==id).update(audioFileMetadata)
    session.commit()
    session.close()

def delete_utility(type,id):
    session = getSession()
    type=f.getClass(type)
    obj=session.query(type).filter(type.id==id).one()
    session.delete(obj)
    session.commit()
    session.close()


def get_utility(*kwargs):
    session = getSession()
    param=[]
    for item in kwargs:
        param.append(item)
    type=f.getClass(param[0])
    if(len(param)>1):
        id=param[1]
        obj = session.query(type).filter(type.id == id)
    else:
        obj = session.query(type)
    #obj=session.query(type).filter(type.id==id)
    session.commit()
    session.close()
    data={"item":[]}
    for r in obj:
        obj_info=r.__dict__
        del obj_info['_sa_instance_state']
        data['item'].append(obj_info)

    print(data)
    return   jsonify(data)



#delete_utility('PodCast',5)l
#update_utility('PodCast','4',{"name":"test_updates","duration":"180","uploadTime":"18-03-2021","host":"xyz","participants":"testp"})