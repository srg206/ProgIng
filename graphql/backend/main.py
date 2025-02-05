import datetime
from ariadne import  graphql_sync
from fastapi import FastAPI, Request, HTTPException
from starlette.responses import JSONResponse
import uvicorn
from resolvers.resolvers import schema



from datetime import datetime

app = FastAPI()

@app.post("/graphql")
async def graphql_server(request: Request):
    data = await request.json()

    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=True  # Можно заменить на переменную окружения или конфиг
    )

    if not success:
        raise HTTPException(status_code=400, detail=result)

    return JSONResponse(result, status_code=200)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")