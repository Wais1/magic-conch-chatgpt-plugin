from fastapi import FastAPI, responses
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from random import choice

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/ask")
async def ask():
    # List of possible responses from the magic conch shell
    responses = [
        "Maybe someday.",
        "Nothing.",
        "Neither.",
        "I don't think so.",
        "No.",
        "Yes.",
        "Try asking again."
    ]

    # Choose a random response
    response = choice(responses)

    return JSONResponse(content={"response": response})

@app.get("/.well-known/ai-plugin.json")
async def get_plugin_info():
    return FileResponse('ai-plugin.json', media_type='application/json')
