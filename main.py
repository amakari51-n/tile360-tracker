from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TILE_API = "https://production.tile-api.com/api/v1"
HEADERS = {
    "tile_app_id": "com.thetileapp.tile",
    "tile_app_version": "2.31.1.4357",
    "tile_client_uuid": "webapp-proxy",
}


@app.post("/api/login")
async def login(email: str = Form(...), password: str = Form(...)):
    client_uuid = uuid.uuid4().hex
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{TILE_API}/clients/",
            data={
                "email": email,
                "password": password,
                "locale": "en-AU",
                "registration_timestamp": "1000",
                "client_uuid": client_uuid,
                "app_id": "com.thetileapp.tile",
                "app_version": "2.31.1.4357",
            },
            headers=HEADERS,
            timeout=15,
        )
    if res.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    data = res.json()
    token = data.get("result", {}).get("client", {}).get("session_token")
    if not token:
        raise HTTPException(status_code=401, detail=data.get("error", {}).get("message", "Auth failed"))
    return {"session_token": token}


@app.get("/api/tiles")
async def get_tiles(session_token: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{TILE_API}/tiles/",
            headers={**HEADERS, "X-TILE-AUTH": session_token},
            timeout=15,
        )
    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail="Failed to fetch tiles")
    data = res.json()
    tiles = list(data.get("result", {}).get("tiles", {}).values())
    return {"tiles": tiles}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
