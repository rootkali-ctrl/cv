from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

# Create FastAPI app
app = FastAPI(title="Object Detection API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple mock detection
def mock_detect():
    objects = ['person', 'car', 'dog', 'cat', 'bicycle', 'bottle', 'phone', 'laptop']
    detections = []
    
    for _ in range(random.randint(0, 3)):
        detections.append({
            "label": random.choice(objects),
            "confidence": round(random.uniform(0.6, 0.95), 2),
            "box": {
                "x": random.randint(50, 300),
                "y": random.randint(50, 200),
                "width": random.randint(80, 150),
                "height": random.randint(80, 150)
            }
        })
    
    return {"detections": detections}

@app.get("/")
def root():
    return {"message": "Object Detection API is running on Render!", "status": "success"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/detect-base64")
def detect_objects(data: dict):
    try:
        result = mock_detect()
        return result
    except Exception as e:
        return {"error": str(e), "detections": []}
