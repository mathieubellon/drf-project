from fastapi import FastAPI, Body, Cookie, File, Form, Header, Path, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from supabase import create_client, Client, ClientOptions
import os

url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_ANON_KEY"]
baseURL = os.environ.get("BASE_URL", "http://127.0.0.1:8000")

supabase: Client = create_client(url, key, options=ClientOptions(flow_type="pkce"))

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World de wow"}

@app.get("/sign_out")
def sign_out():
  res = supabase.auth.sign_out()
  return "success"

def login_page():
    html_content = """
    <html>
        <head>
            <title>Login - Decide</title>
        </head>
        <body>
            <h1>Login</h1>
            <form>
                <button>Github</button>
            </form>
            <form>
                <button>Gitlab</button>
            </form>
            You don't have an account ? <a href="/create_account/">Create account</a>
        </body>

    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

def create_account():
    html_content = """
    <html>
        <head>
            <title>Create account - Decide</title>
        </head>
        <body>
            <h1>Create account with Github</h1>
            <form>
                <button>Github</button>
            </form>
            <form>
                <button>Gitlab</button>
            </form>
            Already have an account? <a href="/login/">Login</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/login/")
async def login():
    res = supabase.auth.sign_in_with_oauth({
        "provider": 'github',
        "options": {
            "redirect_to": baseURL+"/callback",
        }
    })
    print(res.url)
    return RedirectResponse(url=res.url, status_code=302)

@app.get("/callback")
async def callback(request: Request):
    #data = supabase.auth.get_session()
    return {}
