<!--
 * @Author: Puffrora
 * @Date: 2025-09-22 15:48:12
 * @LastEditors: Puffrora
 * @LastEditTime: 2025-09-23 09:37:57
-->
# HS Code Search Service

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
