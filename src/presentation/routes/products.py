from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from urllib.parse import parse_qs

from config.directory import TEMPLATE_BASE_DIR
from factory.products_factory import create_product, get_product_by, list_products, drop_product, update_product_by


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

@router.post("/update/{id}", response_class=HTMLResponse)
async def get_products(request: Request):
    body_bytes = await request.body()
    body_str = body_bytes.decode('utf-8')
    form_dict = parse_qs(body_str)
  
    id = request.path_params["id"]
    name = form_dict.get('name', [""])[0]
    price = form_dict.get('price', [""])[0]
    stock_total = form_dict.get('total', [""])[0]
    
    await update_product_by().execute({
      "id": id,
      "name": name,
      "price": price,
      "stock_total": stock_total,
    })
    
    return RedirectResponse(url="/", status_code=301)

@router.get("/update/{id}", response_class=HTMLResponse)
async def get_products(request: Request):
    id = request.path_params["id"]
    
    response = await get_product_by().execute(id)
    
    return templates.TemplateResponse("update_product.html", {
      "request": request,
      "id": response["id"],
      "name": response["name"],
      "price": response["price"],
      "total": response["stock_total"]
    })
  