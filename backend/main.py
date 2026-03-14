from fastapi import FastAPI

app = FastAPI(
    title="AlphaForge API",
    version="0.1.0",
    description="AI investment committee backend for disruptive growth stocks.",
)

@app.get("/")
def read_root():
    return {"message": "AlphaForge API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}