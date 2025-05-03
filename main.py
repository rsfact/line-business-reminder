from fastapi import FastAPI, APIRouter
import webhooks
import settings

app = FastAPI(
    title="LINE Business Reminder",
    root_path=settings.BASE_PATH
)

api_router = APIRouter(prefix="/api")
api_router.include_router(webhooks.router, prefix="/webhook", tags=["Webhook"])

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.HOT_RELOAD)
