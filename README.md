# Django REST API with JWT Authentication

این پروژه یک API بر پایه Django و Django REST Framework (DRF) است که امکانات زیر را ارائه می‌دهد:

* احراز هویت با JSON Web Token (JWT)
* مدل `TitleRecord` با فیلدهای متنوع و تولید خودکار کلید ۳۲ رقمی یونیک
* کنترل دسترسی: کاربران فقط توان CRUD روی رکوردهای خود را دارند و سوپرادمین دسترسی کامل
* محدودیت در ویرایش فیلدهای مدیریتی (`final_status`، `base_code`، `father_code`)
* پنل ادمین سفارشی برای مدیریت مدل‌ها

---

## نصب و راه‌اندازی

1. کلون کردن مخزن و ورود به دایرکتوری پروژه:

   ```bash
   git clone https://github.com/EhnNoz/metadata.git
   cd myproject
   ```
2. ایجاد و فعال‌سازی محیط مجازی:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # لینوکس / مک
   venv\Scripts\activate    # ویندوز
   ```
3. نصب وابستگی‌ها:

   ```bash
   pip install -r requirements.txt
   ```
4. تنظیمات پایگاه داده در `settings.py` (به‌صورت پیش‌فرض SQLite است). برای PostgreSQL:

   ```bash
   pip install psycopg2-binary
   ```
5. اعمال مهاجرت‌ها و ایجاد سوپرادمین:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. اجرای سرور :

   ```bash
   python manage.py runserver
   ```

---

## مسیرها (Endpoints)

| مسیر                  | متد    | توضیحات                                      |
| --------------------- | ------ | -------------------------------------------- |
| `/api/token/`         | POST   | دریافت توکن دسترسی و رفرش                    |
| `/api/token/refresh/` | POST   | تمدید توکن دسترسی                            |
| `/api/titles/`        | GET    | لیست رکوردهای کاربر جاری (یا همه برای ادمین) |
| `/api/titles/`        | POST   | ایجاد رکورد جدید                             |
| `/api/titles/{id}/`   | GET    | جزییات رکورد خاص                             |
| `/api/titles/{id}/`   | PUT    | به‌روزرسانی رکورد (تمام فیلدها)              |
| `/api/titles/{id}/`   | PATCH  | به‌روزرسانی جزئی رکورد                       |
| `/api/titles/{id}/`   | DELETE | حذف رکورد (در صورت `final_status=False`)     |

---

## نمونه درخواست

### دریافت توکن

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"youruser","password":"yourpass"}'
```

### ایجاد رکورد جدید

```bash
curl -X POST http://localhost:8000/api/titles/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "organ": 1,
    "MetaTitle": "نمونه تیتر محتوا",
    "MetaShowDate": "2025-05-03",
    "Title": "عنوان اصلی",
    ... سایر فیلدها ...
}'
```

---

## پنل ادمین

* آدرس: `http://localhost:8000/admin/`
* مدیریت مدل‌های `YourOrganModel` و `TitleRecord`
* سوپرادمین می‌تواند فیلدهای مدیریتی را تنظیم کند.

---

## نکات تکمیلی

* فیلدهای `final_status`، `base_code` و `father_code` فقط توسط سوپرادمین قابل تنظیم هستند.
* پس از ایجاد رکورد توسط کاربر، مقدار `new_title_code` در پاسخ JSON برگردانده می‌شود و در پنل ادمین readonly است.
* کاربران تنها رکوردهای متعلق به خود را مشاهده و ویرایش می‌کنند.

---

