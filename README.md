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
    "active": true
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
    "active": true
}
```
**Response**

- `201 CREATED` on success. Response body: Band with id: 3 successfully added to the SQLite database

- `400 BAD REQUEST` on fail

### Delete a band
**Endpoint**

`DELETE /api/v1/resources/band/<id>`

**Response**

- `200 OK` on success. Response body: Band with id: 1 deleted

### Update an band
**Endpoint**

`PUT /api/v1/resources/band/<id>`

**Arguments**

-`"id": int` id of an existing band in the database

-`"name": string` name of the band

-`"active": boolean` true if the group is actively playing. False otherwise

```json
{
    "id": 100,
    "name": "Gorefest",
    "active": false
}
```
**Response**

- `201 CREATED` on success. Response body: 
```json
{
    "active": false,
    "id": 2,
    "name": "Scorpions"
}
```

- `400 BAD REQUEST` on fail

### Add a new album
**Endpoint**

`POST /api/v1/resources/albums`

**Arguments**

-`"band_id": string` id of an existing band in the database

-`"name": string` name of a album

-`"record_company": string` name of the record company 

```json
{
    "band_id": 3,
    "name": "tiny tunes",
    "record_company": "tosser records"
}
```
**Response**

- `201 CREATED` on success. Response body: Album with id: 4 successfully added to the SQLite database

- `400 BAD REQUEST` on fail

### Show one album by id
**Endpoint**

`GET /api/v1/resources/album/<id>`

**Repsonse**
- `200 OK` on success
```json
[
    {
        "id": 2,
        "name": "good company",
        "record_company": "six shooter records"
    }
]
```
- `404 NOT FOUND` Album with id: 299 couldn't be found. On fail

### Delete an album
**Endpoint**

`DELETE /api/v1/resources/album/<id>`

**Response**

- `200 OK` on success. Response body: Band with id: 1 deleted

### Update an album
**Endpoint**

`PUT /api/v1/resources/album/<id>`

**Arguments**

-`"name": string` name of the album

-`"record_company": string` name of the record company

```json
{
    "name": "Gorefest",
    "record_company": false
}
```
**Response**

- `201 CREATED` on success. 

- `400 BAD REQUEST` on fail




