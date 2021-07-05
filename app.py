if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=5000, log_level="info", reload=False, lifespan="on")
