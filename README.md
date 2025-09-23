# HS Code Classification Service

This project is a web-based HS Code search service that uses text similarity to match descriptions to relevant HS codes. It provides both:

- A **web-based user interface (UI)** for interactive searching
- A **RESTful API** for programmatic queries

---

## Deployment Info

The service is deployed at:

- **UI Access (Web App)**: [http://au2sp-ssql-409a.sand.wtg.zone:8080](http://au2sp-ssql-409a.sand.wtg.zone:8080)  
- **API Endpoint**: [http://au2sp-ssql-409a.sand.wtg.zone:8081/query](http://au2sp-ssql-409a.sand.wtg.zone:8081/query)

---

## Usage

### 1. API Usage (Port 8081)

#### 1. `Query` API
Sample Req
```
GET http://au2sp-ssql-409a.sand.wtg.zone:8081/query?query=steel|hollow knight
```

Sample Resp
```
[
  {
    "query": "steel",
    "predictions": [
      {
        "hscode": "7208.39.00",
        "description": "Flat-rolled products of iron or non-alloy steel...",
        "confidence_score": 0.9271
      },
      {
        "hscode": "7210.70.00",
        "description": "Flat-rolled iron or non-alloy steel, painted, varnished or coated...",
        "confidence_score": 0.8124
      },
      ...
    ]
  },
  {
    "query": "hollow knight",
    "predictions": [
      {
        "hscode": "9504.50.00",
        "description": "Video game consoles and machines...",
        "confidence_score": 0.8423
      },
      {
        "hscode": "9504.90.90",
        "description": "Other game consoles and machines, not specified elsewhere.",
        "confidence_score": 0.7916
      },
      ...
    ]
  }
]
```

#### 2. `Download` API

Sample Req
```
GET http://au2sp-ssql-409a.sand.wtg.zone:8081/download/datasets.zip
```

---

## Local Test

Need to download `datasets.zip` / `models.zip` / `vectors.zip (optional)` firstly then unzip each one to the project's root directory:

- **Datasets**: [http://au2sp-ssql-409a.sand.wtg.zone:8081/download/datasets.zip](http://au2sp-ssql-409a.sand.wtg.zone:8081/download/datasets.zip)  
- **Models**: [http://au2sp-ssql-409a.sand.wtg.zone:8081/download/models.zip](http://au2sp-ssql-409a.sand.wtg.zone:8081/download/models.zip)  
- **Vectors** (optional): [http://au2sp-ssql-409a.sand.wtg.zone:8081/download/vectors.zip](http://au2sp-ssql-409a.sand.wtg.zone:8081/download/vectors.zip)

---



