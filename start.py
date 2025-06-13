import uvicorn
from server.config.env import PORT, HOST_IP

if __name__ == "__main__":
    uvicorn.run ("server.main:app", host=str(HOST_IP), port=int(PORT), reload=True)