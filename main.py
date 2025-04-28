from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

allowed_names = [
    "kai", "ken jinx", "spacez", "lucian",
    "andy dawson", "andy", "riyoshi iro",
    "spector heedz", "arthur maniac"
]

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/validate", response_class=HTMLResponse)
async def post_validate(username: str = Form(...)):
    username = username.strip().lower()
    if username in allowed_names:
        return RedirectResponse(url="/gate", status_code=303)
    else:
        return RedirectResponse(url="/join", status_code=303)


@app.get("/gate", response_class=HTMLResponse)
async def get_gate(request: Request):
    return templates.TemplateResponse("gate.html", {"request": request})


@app.get("/join", response_class=HTMLResponse)
async def get_join(request: Request):
    return templates.TemplateResponse("join.html", {"request": request})
