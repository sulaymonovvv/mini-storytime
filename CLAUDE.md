# mini-storytime: agent uchun qoidalar

Bu repo o'quv labi. Quyidagi qoidalarga amal qiling va har bir o'zgarishni tushuntiring.

## Qoidalar

<!-- Qaror (2026-10-03): 5 ta qoidaning hammasi hozircha qoldi, chunki repoda hali avtomatik tekshiruv yo'q: linter, gitleaks va CI qo'shilmagan. Ular o'rnatilgach, mashina tekshira oladigan qoidalar (1, 2 va 4) shu fayldan olib tashlanadi va faqat fikrlashni talab qiladigan qoidalar qoladi. -->

1. **Fayllar kichik bo'lsin.** Har bir fayl bitta vazifani bajarsin.
   *Nega:* kichik faylni o'qish va tekshirish oson, uni to'liq tushunish mumkin.
2. **Sirlar faqat `.env`da.** Parol, token va kalitlar kodga, logga va commit'ga tushmasin; `.env` `.gitignore`da turadi.
   *Nega:* repo public va sir Git tarixiga tushsa, uni o'chirib bo'lmaydi.
3. **Avval reja, keyin kod.** Kod yozishdan oldin rejani ko'rsating va tasdiq so'rang.
   *Nega:* noto'g'ri yo'nalishni kod yozilguncha to'xtatish arzonroq.
4. **Har o'zgarishdan keyin test.** O'zgartirgach testlarni ishga tushiring va natijani ko'rsating.
   *Nega:* «tayyor» degan gap o'zingiz ko'rmaguningizcha ishonchsiz.
5. **Infra buyruqlari faqat lab klasterida.** `kubectl`, `docker`, `helm` va `terraform`ni faqat lab muhitida (`k3d-` klaster) ishlating.
   *Nega:* noto'g'ri buyruq haqiqiy tizimga zarar yetkazmasin.
