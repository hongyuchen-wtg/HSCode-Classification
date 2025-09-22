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
GET http://au2sp-ssql-409a.sand.wtg.zone:8081/query?query=steel%26hollow knight
```

Sample Resp
```
{
  "query": "steel&hollow knight",
  "result": [
    {
      "query": "steel",
      "predictions": [
        {
          "hscode": "8307.10.00.00E",
          "description": "h0Description:Of iron or steel\nh1Description:Flexible tubing of iron or steel",
          "confidence_score": 0.8349
        },
        {
          "hscode": "8202.31.00    ",
          "description": "h0Description:With working part of steel\nh1Description:nan",
          "confidence_score": 0.8322
        },
        {
          "hscode": "7224.90.00.00B",
          "description": "h0Description:Other\nh1Description:Semi-finished of alloy steel",
          "confidence_score": 0.8306
        }
      ]
    },
    {
      "query": "hollow knight",
      "predictions": [
        {
          "hscode": "9504.10.00.00J",
          "description": "h0Description:VIDEO GAMES ETC\nh1Description:Video games etc",
          "confidence_score": 0.779
        },
        {
          "hscode": "0307.43.00.19G",
          "description": "h0Description:Heads and tentacles\nh1Description:Frozen squid heads and tentacles",
          "confidence_score": 0.7771
        },
        {
          "hscode": "0307.49.00.29A",
          "description": "h0Description:FROZEN SQUID HEADS AND TENTACLES\nh1Description:Frozen squid heads and tentacles",
          "confidence_score": 0.7736
        }
      ]
    }
  ]
}
```


