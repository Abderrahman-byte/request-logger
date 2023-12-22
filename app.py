from fastapi import FastAPI, Request
from loguru import logger

app = FastAPI()


@app.api_route("/{full_path:path}")
async def main(request: Request, full_path:str):
    full_path = "/" + full_path
    body = await request.body()

    logger.debug("{} {}",request.method, full_path)
    
    for k,v in request.headers.items():
        logger.debug("{}='{}'", k, v)

    logger.debug("{}", body)

    return {"success": True}
