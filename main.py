from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import sumtostr

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def ms(money):
    if (money >0):
        moneyToStr = sumtostr.MoneyToStr("UAH", "UKR", "NUMBER")
        return moneyToStr.convertValue(money)
    else: return ''
#
@app.get("/")
async def get_endpoints(request: Request):
    context = {
        "request": request,
        "title": "Сума прописом",
        "str_num": ""
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/json")
async def get_endpoints(request: Request):
    result_num = request.query_params.get('num')
    value = 0
    if result_num:
        value = ms(float(result_num.replace(',', '.')))
    return {"num": result_num,"str":value}


@app.post("/post")
async def handle_form_data(request: Request,
                           # user_data: str = Form(...),
                           user_data: Optional[str] = Form(None),
                           switch_value: Optional[str] = Form(None)
                           ):

    str_value = ms(float(user_data.replace(',', '.')))

    is_active_mode = switch_value is not None

    if is_active_mode:
        print("Активний режим УВІМКНЕНО")
    else:
        print("Активний режим ВИМКНЕНО")

    data ={
        "request": request,
        "is_active_mode": is_active_mode,
        "title": "Сума прописом",
        "num_value": user_data,
        "str_value": str_value
    }
    return templates.TemplateResponse("index.html",data)
