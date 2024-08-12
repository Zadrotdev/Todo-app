from fastapi import FastAPI

import models
from database import engine
from routers import assignments, auth, admin

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO APP")
app.include_router(assignments.router)
app.include_router(auth.router)
app.include_router(admin.router)


