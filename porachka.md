---
layout: page
title: "Поръчка"
permalink: /porachka/
---

<div style="max-width:720px;margin:auto">
  <h2>Поръчай Minoxidil 5%</h2>
  <p>Плащане: наложен платеж – без риск за Вас ✅</p>

  <!-- mensaje de éxito -->
  <div id="successMsg" style="display:none;padding:14px;border:1px solid #28a745;border-radius:8px;margin:12px 0;">
    ✅ Благодарим за поръчката! Ще получите потвърждение по имейл.
  </div>

  <!-- envío en iframe oculto para evitar CORS -->
  <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;"></iframe>

  <form id="orderForm" action="  https://script.google.com/macros/s/AKfycbwn5jkvg5_J6_dZlw8GZnQMD9W3mvo_cVZd10yanUkmj2xngaTpoFE3Obr8wpBseCCW/exec" method="POST" target="hidden_iframe" style="display:block;gap:12px;">
    <label style="display:block;margin:10px 0;">
      Име и фамилия:
      <input type="text" name="full_name" required
             style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
    </label>

    <label style="display:block;margin:10px 0;">
      Телефон:
      <input type="tel" name="phone" required
             pattern="^\+?\d[\d\s\-()]{6,}$"
             placeholder="+359 88 123 4567"
             style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
    </label>

    <label style="display:block;margin:10px 0;">
      Email (за потвърждение):
      <input type="email" name="email" required
             style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
    </label>

    <label style="display:block;margin:10px 0;">
      Адрес за доставка:
      <textarea name="address" required rows="3"
                style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;"></textarea>
    </label>

    <label style="display:block;margin:10px 0;">
      Количество:
      <select name="quantity"
              style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
        <option value="1">1 бр. – 47 лв</option>
        <option value="2">2 бр. – 94 лв</option>
        <option value="3">3 бр. – 141 лв (безплатна доставка)</option>
        <option value="5">5 бр. – 235 лв</option>
      </select>
    </label>

    <!-- honeypot antispam -->
    <input type="text" name="website" style="display:none">

    <button id="submitBtn" type="submit"
            style="background:#28a745;color:white;padding:15px;border:none;border-radius:8px;font-size:18px;cursor:pointer;">
      ✅ Поръчвам сега
    </button>
  </form>
</div>

<script>
  (function () {
    var form = document.getElementById("orderForm");
    var success = document.getElementById("successMsg");
    var btn = document.getElementById("submitBtn");
    var iframe = document.getElementById("hidden_iframe");
    var submitted = false;

    form.addEventListener("submit", function () {
      submitted = true;
      btn.disabled = true;
      btn.textContent = "Изпращане...";
    });

    iframe.addEventListener("load", function () {
      if (!submitted) return; // ignora el primer load
      form.reset();
      success.style.display = "block";
      btn.disabled = false;
      btn.textContent = "✅ Поръчвам сега";
      submitted = false;
    });
  })();
</script>
