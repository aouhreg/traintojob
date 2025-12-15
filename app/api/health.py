from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

"""
我把APi拆成獨立的router module，讓main.py只負責application組裝，避免它隨著功能增加變成god file，這在production服務的可維護性與可擴展性上非常關鍵。

main.py的角色應該是組裝，而不是是做
在一個成熟的服務中
# main.py 應該長這樣
app = FastAPI()
app.include_router(...)
app.add_middleware(...)

如果把實際api寫進main.py，後果是
API數量一多，檔案爆炸
不同domain混在一起
merge conflict 頻繁
code review 困難

router拆分是爲了separation of concerns


我現在做的是把main.py定位成application composition layer，
API implementation則分散在各自的router中，這樣服務在規模擴展時仍然可讀，可測，可運維
"""