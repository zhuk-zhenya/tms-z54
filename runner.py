import uvicorn


uvicorn.run(
    "1:app",
    port=8000,
    host="0.0.0.0",
    log_level="debug",
)
