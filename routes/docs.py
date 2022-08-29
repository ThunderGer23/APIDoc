from fastapi import APIRouter

doc = APIRouter()

@doc.get('/')
def home():
    return 'This route from analize the docs with IA'

