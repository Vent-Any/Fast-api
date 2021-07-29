from __future__ import print_function
from __future__ import unicode_literals
import logging 
import os
import sys
import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")   # 在应用开启之前要执行的函数
async def startup()-> FastAPI:
    
    return app

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(router,tags=[""],prefixf='/test')

if __name__ == "__main__":
    uvicorn.run(
        "service:app",
        host="127.0.0.1",
        port=8080,
        reload=True    
    )

