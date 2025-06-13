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

async def update_note(note_id: str, note: NoteUpdate, user_id: str):
    update_fields = note.model_dump(exclude_unset=True)
    update_fields["user_id"] = user_id

    result = await notes_collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": update_fields}
    )

    if result.modified_count == 0:
        return False
    return True

async def delete_note(note_id: str):
    print(note_id)
    result=await notes_collection.delete_one(
        {"_id":ObjectId(note_id)}
    )
    if result.deleted_count == 0:
        return False
    return True