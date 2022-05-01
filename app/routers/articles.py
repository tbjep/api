from fastapi import APIRouter, Depends
from OSINTmodules.OSINTelastic import searchQuery
from .. import config_options

router = APIRouter(
    prefix="/articles",
    responses={404: {"description": "Not found"}},
)

@router.get("/overview/newest")
async def get_newest_articles():
    return config_options.esArticleClient.queryDocuments(searchQuery(limit = 50, complete = False), return_object = False)["documents"]
