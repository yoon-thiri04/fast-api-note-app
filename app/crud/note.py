from app.db import db
from app.models.note import NoteCreate, NoteResponse, NoteUpdate
from bson import ObjectId
notes_collection = db['notes']
#note_create
async def create_note(note:NoteCreate):
    note_data =note.model_dump()
    note_data["user_id"]=ObjectId(note_data['user_id'])
    await notes_collection.insert_one(note_data)
    return True

async def get_note(note_id : str):
    note = await notes_collection.find_one(
        {"_id":ObjectId(note_id)}
    )
    return note

async def get_notes(user_id:str):
    notes =await notes_collection.find(
        {"user_id":ObjectId(user_id)}
    ).to_list()
    
    return notes

async def update_note(noted_id : str, note:NoteUpdate):
    pass

async def delete_note(noted_id: str):
    pass