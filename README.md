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

### Show one band by id
**Endpoint**

`GET /api/v1/resources/band/<id>`

**Repsonse**
- `200 OK` on success
```json
[
    {
        "active": 1,
        "albums": [],
        "id": 1,
        "name": "The dead south"
    }
]
```
- `404 NOT FOUND` Band with id: 39 couldn't be found. On fail

### Add a new band
**Endpoint**

`POST /api/v1/resources/bands`

**Arguments**

-`"name": string` name of the music group

-`"albums": string` name of a album

-`"active": boolean` true if the group is actively playing. False otherwise

```json
{
    "name": "Dead south",
    "albums": "Good company",
    "active": true
}
```
**Response**

- `201 CREATED` on success. Response body: Band with id: 3 successfully added to the SQLite database

- `400 BAD REQUEST` on fail

### Delete a band
**Endpoint**

`DELETE /api/v1/resources/bands/<id>`

**Response**

- `200 OK` on success. Response body: Band with id: 1 deleted




