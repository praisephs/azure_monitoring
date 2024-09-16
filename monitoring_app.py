from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Monitoring App"}

@app.get("/metrics/cpu")
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return {"cpu_usage_percent": cpu_usage}

@app.get("/metrics/memory")
def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return {
        "total_memory_gb": memory_info.total / (1024 ** 3),
        "available_memory_gb": memory_info.available / (1024 ** 3),
        "used_memory_percent": memory_info.percent
    }

@app.get("/metrics/disk")
def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    return {
        "total_disk_gb": disk_info.total / (1024 ** 3),
        "used_disk_gb": disk_info.used / (1024 ** 3),
        "free_disk_gb": disk_info.free / (1024 ** 3),
        "used_disk_percent": disk_info.percent
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
