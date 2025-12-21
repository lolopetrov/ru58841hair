
from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
import smtplib
from email.mime.text import MIMEText
import os

app = FastAPI()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

@app.post("/send")
def send_order(
    product: str = Form(...),
    qty: str = Form(...),
    delivery: str = Form(...),
    address: str = Form(...),
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    nft: str = Form("no"),
    wallet: str = Form("")
):
    # 📩 Email para ti
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
""")

    admin_msg["Subject"] = "🧾 Нова поръчка RU58841"
    admin_msg["From"] = SMTP_USER
    admin_msg["To"] = SMTP_USER

    # 📬 Email para el cliente
    user_msg = MIMEText(f"""
Здравей {name},

Получихме твоята поръчка успешно.

Продукт: RU58841 5%
Количество: {qty}
Доставка: {delivery}

Ще се свържем с теб за потвърждение.

Благодарим ти.
""")

    user_msg["Subject"] = "✅ Потвърждение на поръчка — RU58841"
    user_msg["From"] = SMTP_USER
    user_msg["To"] = email

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(admin_msg)
        server.send_message(user_msg)

    return RedirectResponse(
        "https://ru58841hair.com/thanks.html",
        status_code=303
    )
