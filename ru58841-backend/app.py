from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
import smtplib
from email.mime.text import MIMEText
import os
import re

app = FastAPI()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

ALLOWED_ORIGINS = {
    "https://ru58841hair.com",
    "https://www.ru58841hair.com",
}

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_REGEX = re.compile(r"^[0-9+\-\s()]{6,25}$")
WALLET_REGEX = re.compile(r"^[A-Za-z0-9]{20,120}$")


def is_suspicious_email(email: str) -> bool:
    bad_patterns = [
        "mailinator",
        "tempmail",
        "guerrillamail",
        "10minutemail",
        "sharklasers",
    ]
    e = email.lower()
    return any(p in e for p in bad_patterns)


def clean(value: str, max_len: int = 200) -> str:
    value = (value or "").strip()
    return value[:max_len]


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/send")
def send_order(
    request: Request,
    product: str = Form(...),
    qty: str = Form(...),
    delivery: str = Form(...),
    address: str = Form(...),
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    nft: str = Form("no"),
    wallet: str = Form(""),
    company: str = Form("")  # honeypot: este campo debe ir vacío
):
    origin = request.headers.get("origin", "")
    referer = request.headers.get("referer", "")

    # 1) Honeypot: si viene relleno, casi seguro es bot
    if company.strip():
        raise HTTPException(status_code=400, detail="Spam detected")

    # 2) Permitir solo desde tu dominio
    if origin and origin not in ALLOWED_ORIGINS:
        raise HTTPException(status_code=403, detail="Origin not allowed")

    if referer and not any(referer.startswith(o) for o in ALLOWED_ORIGINS):
        raise HTTPException(status_code=403, detail="Referer not allowed")

    # 3) Limpiar y validar
    product = clean(product, 100)
    qty = clean(qty, 10)
    delivery = clean(delivery, 50)
    address = clean(address, 200)
    name = clean(name, 100)
    phone = clean(phone, 25)
    email = clean(email, 120)
    nft = clean(nft.lower(), 10)
    wallet = clean(wallet, 120)

    allowed_products = {"RU58841 5%", "RU58841"}
    if product not in allowed_products:
        raise HTTPException(status_code=400, detail="Invalid product")

    if qty not in {"1", "2", "3", "4", "5"}:
        raise HTTPException(status_code=400, detail="Invalid quantity")

    if delivery not in {"office", "address"}:
        raise HTTPException(status_code=400, detail="Invalid delivery")

    if len(name) < 2:
        raise HTTPException(status_code=400, detail="Invalid name")

    if not EMAIL_REGEX.match(email) or is_suspicious_email(email):
        raise HTTPException(status_code=400, detail="Invalid email")

    if not PHONE_REGEX.match(phone):
        raise HTTPException(status_code=400, detail="Invalid phone")

    if nft not in {"yes", "no"}:
        raise HTTPException(status_code=400, detail="Invalid nft value")

    if nft == "yes":
        if not wallet or not WALLET_REGEX.match(wallet):
            raise HTTPException(status_code=400, detail="Invalid wallet")
    else:
        wallet = ""

    # 4) Crear emails
    admin_msg = MIMEText(f"""
🧾 НОВА ПОРЪЧКА — RU58841 5%

Продукт: {product}
Количество: {qty}
Доставка: {delivery}
Адрес / офис: {address}

Клиент:
Име: {name}
Телефон: {phone}
Email: {email}

NFT: {nft}
Wallet: {wallet}
""".strip())

    admin_msg["Subject"] = "🧾 Нова поръчка RU58841"
    admin_msg["From"] = SMTP_USER
    admin_msg["To"] = SMTP_USER

    user_msg = MIMEText(f"""
Здравей {name},

Получихме твоята поръчка успешно.

Продукт: {product}
Количество: {qty}
Доставка: {delivery}

Ще се свържем с теб за потвърждение.

Благодарим ти.
""".strip())

    user_msg["Subject"] = "✅ Потвърждение на поръчка — RU58841"
    user_msg["From"] = SMTP_USER
    user_msg["To"] = email

    # 5) Enviar
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(admin_msg)
        server.send_message(user_msg)

    return RedirectResponse(
        "https://ru58841hair.com/thanks.html",
        status_code=303
    )
