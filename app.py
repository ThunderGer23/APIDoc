from fastapi import FastAPI
from routes.docs import doc

app = FastAPI()

app.include_router(doc)