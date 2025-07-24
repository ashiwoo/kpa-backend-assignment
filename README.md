# KPA Backend Assignment

This is a Django REST Framework-based backend implementation for the **KPA Wheel Specification Form API**.

---

## 🔧 Tech Stack

- **Backend**: Django 5.2, Django REST Framework
- **Database**: PostgreSQL
- **API Testing**: Postman

---

## 📁 API Endpoints

### 🔸 POST `/api/forms/wheel-specifications`

Creates a new wheel specification form.

#### 📥 Sample Request Body:
```json
{
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "condemningDia": "825 (800-900)",
    "intermediateWWP": "20 TO 28",
    "lastShopIssueSize": "837 (800-900)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "treadDiameterNew": "915 (900-1000)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelDiscWidth": "127 (+4/-0)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness"
  },
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03"
}
✅ Success Response (201):
{
  "message": "Wheel specification form submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "fields": { ... }
  },
  "success": true
}
```
###  GET /api/forms/wheel-specifications
Fetch submitted forms using optional query filters.

Query Parameters:
formNumber (optional)

submittedBy (optional)

submittedDate (optional)
🧪 Sample Request:
GET /api/forms/wheel-specifications?formNumber=WHEEL-2025-001&submittedBy=user_id_123&submittedDate=2025-07-03

✅ Success Response (200):
{
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "condemningDia": "825 (800-900)",
        "lastShopIssueSize": "837 (800-900)",
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ],
  "success": true
}

### 🚀 How to Run Locally:
1. Clone the repo
git clone https://github.com/ashiwoo/kpa-backend-assignment.git
cd kpa-backend-assignment

2. Configure PostgreSQL
Set DB name, user, and password in settings.py

3. Run migrations
python manage.py migrate

4. Start development server
python manage.py runserver

#### 📬 Submission
GitHub Repo: https://github.com/ashiwoo/kpa-backend-assignment

Postman Collection: 
[Click to Download](KPA_backend_collection.postman_collection.json)

#### 🙋 Author
Ashish Vishwakarma
Email: ashish.vishwakarma.avk@gmail.com
GitHub: https://github.com/ashiwoo
