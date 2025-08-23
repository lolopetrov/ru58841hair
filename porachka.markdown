
---
layout: page
title: Поръчка
permalink: /porachka/
---


<section id="order" style="max-width:600px;margin:auto;padding:2rem;background:#f9f9f9;border-radius:12px;box-shadow:0 0 10px rgba(0,0,0,0.1);">
  <h2 style="text-align:center;">Поръчай Minoxidil 5%</h2>
  <p style="text-align:center;">Плащане: <b>наложен платеж</b> – без риск за Вас ✅</p>

  <form id="orderForm" action="https://script.google.com/macros/s/AKfycbx3LACEr89UZYfGbTGkmTX9hSDCMktPCOau_LoiZkbwEO84aYtWhFGHf8WI06bWSyNk/exec" method="POST" style="display:flex;flex-direction:column;gap:1rem;">
    <label>Име и фамилия:
      <input type="text" name="name" required style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
    </label>

    <label>Телефон:
      <input type="tel" name="phone" required style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
    </label>

    <label>Email (за потвърждение):
      <input type="email" name="email" required style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
    </label>

    <label>Адрес за доставка:
      <textarea name="address" required rows="3" style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;"></textarea>
    </label>

    <label>Количество:
      <select name="quantity" style="width:100%;padding:10px;border:1px solid #ccc;border-radius:8px;">
        <option value="1">1 бр. – 47 лв</option>
        <option value="2">2 бр. – 94 лв</option>
        <option value="3">3 бр. – 141 лв (безплатна доставка)</option>
        <option value="5">5 бр. – 235 лв</option>
      </select>
    </label>

    <button type="submit" style="background:#28a745;color:white;padding:15px;border:none;border-radius:8px;font-size:18px;cursor:pointer;">
      ✅ Поръчвам сега
    </button>
  </form>

  <p id="successMsg" style="text-align:center;font-size:16px;color:green;display:none;margin-top:1rem;">
    ✅ Благодарим за поръчката! Ще получите потвърждение по имейл.
  </p>
</section>

<script>
  document.getElementById("orderForm").addEventListener("submit", function(e) {
    e.preventDefault();
    var form = e.target;
    fetch(form.action, {
      method: "POST",
      body: new FormData(form)
    }).then(response => {
      if (response.ok) {
        form.reset();
        document.getElementById("successMsg").style.display = "block";
      } else {
        alert("⚠️ Възникна грешка. Моля, опитайте отново.");
      }
    }).catch(err => alert("⚠️ Грешка в мрежата."));
  });
</script>
