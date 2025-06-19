from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api", response_class=PlainTextResponse)
def get_country_outline(country: str):
    try:
        # 1. Generate Wikipedia URL
        wiki_url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        
        # 2. Fetch Wikipedia Page
        response = requests.get(wiki_url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Wikipedia page not found")

        # 3. Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")
        headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        # 4. Generate Markdown Outline
        outline = ["## Contents", ""]
        for heading in headings:
            level = int(heading.name[1])
            text = heading.get_text(strip=True)
            if text.lower() != "jump to navigationjump to search":
                outline.append(f"{'#' * level} {text}")

        return "\n".join(outline)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
