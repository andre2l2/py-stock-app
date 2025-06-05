from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from config.directory import TEMPLATE_BASE_DIR
from factory.products_factory import list_products, drop_product


router = APIRouter()

templates = Jinja2Templates(directory=str(TEMPLATE_BASE_DIR / "templates"))

@router.get("/", response_class=HTMLResponse)
async def get_products(request: Request):
    items = await list_products().execute()
  
    return templates.TemplateResponse("list_products.html", {
      "request": request,
      "items": items
    })


@router.delete("/{id}", response_class=HTMLResponse)
async def delete_product(request: Request):
    id = request.path_params["id"]
    await drop_product().execute(id)
  
    return RedirectResponse(url="/")