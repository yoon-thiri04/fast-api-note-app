from fastapi import APIRouter, HTTPException, status,Depends
from app.models.note import NoteCreate, NoteResponse,NoteUpdate
from app.utils.authentication import get_current_user
from app.crud.note import create_note, get_note, get_notes, update_note, delete_note
router = APIRouter(prefix="/notes", tags=["Note CRUD"])

@router.post("/", response_model=dict)
async def create_note_app(note:NoteCreate, current_user=Depends(get_current_user)):
    note_data =note.model_dump()
    note_data['user_id']=current_user["id"]
    new_note = NoteCreate(**note_data)
    await create_note(new_note)
    return {"message":"note created"}

@router.get("/{note_id}",response_model=NoteResponse)
async def get_note_api(note_id: str, current_user=Depends(get_current_user)):
    note = await get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found!")
    
    return NoteResponse.from_mongo(note)

@router.get("/", response_model=list[NoteResponse])
async def get_notes_api( current_user=Depends(get_current_user)):
    notes =await get_notes(current_user["id"])
    return  [NoteResponse.from_mongo(note) for note in notes]

@router.put("/{note_id}",response_model=dict)
async def update_note_api(note_id:str,note:NoteUpdate,current_user=Depends(get_current_user)):
    updated = await update_note(note_id,note, current_user["id"])

    if not updated:
        raise HTTPException(status_code=404, detail="Note not found!")
    
    return {"message":"note updated"}
@router.delete("/{note_id}",response_model=dict)
async def delete_note_api(note_id:str,current_user=Depends(get_current_user)):
    print(note_id)
    delected = await delete_note(note_id)
    if not delected:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return {"message":"Note delected"}