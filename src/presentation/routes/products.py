from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from urllib.parse import parse_qs

from config.directory import TEMPLATE_BASE_DIR
from factory.products_factory import create_product, list_products, drop_product


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
  
    return RedirectResponse(url="/", status_code=301)
  
  
@router.get("/create", response_class=HTMLResponse)
async def get_products(request: Request):
    return templates.TemplateResponse("create_product.html", {
      "request": request,
    })
    

@router.post("/create", response_class=HTMLResponse)
async def create(request: Request):
    body_bytes = await request.body()
    body_str = body_bytes.decode('utf-8')
    form_dict = parse_qs(body_str)
    
    name = form_dict.get('name', [""])[0]
    price = form_dict.get('price', [""])[0]
    total = form_dict.get('total', [""])[0]
        
    await create_product().execute({
      "name": name,
      "price": "$ " + price,
      "stock_total": total
    })

    return RedirectResponse(url="/", status_code=301)
