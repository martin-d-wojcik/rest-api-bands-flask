# Bands Api

## Usage

### List all bands
**Endpoint**
`GET /api/v1/resources/bands`

**Repsonse**
- `200 OK` on success
```json
[
  {
    "id": 1,
    "name": "iron maiden",
    "active": true,
    "albums": [
      {
        "name": "somewhere in time",
        "record_company": "some guys records"
      } 
    ] 
  }
]
```
### Add a new band
**Endpoint**
`POST /api/v1/resources/bands`



