# pedramoura-delivery-route

## Requirements
### Python modules
* ``flask`` and ``flask_restful``: framework for running a HTTP web service
* ``googlemaps``: Google Directions API for retrieving route information
* ``folium``: Maps framework
```bash
pip install flask flask_restful googlemaps folium
```

### Cloning the repository
```bash
git clone https://github.com/marcelozilio/pedramoura-delivery-route
```

## Usage
### Running web service
```bash
cd pedramoura-delivery-route/
python main.py
```
The output must show the IP address:
```console
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## API

### Inserting route into database

Request to create map
```bash
curl -X POST
\ -H "Content-Type: application/json" 
\ -d '{"enderecos": ["Rua José Bonifácio 544 Gravataí", ""]}' 
\ URL 'http://127.0.0.1:5000/delivery-route'
```
Response success:

```bash
{
    "id": "99b90b23-a4f7-4c3d-9ab6-5f9c576ac547",
    "route": [
        {
    ...
}
```
The ``id`` field may be used to retrieve route information.

### Getting route from database by ID
Request to get map
```bash
curl -X GET
\ -H "Content-Type: application/json" 
\ URL 'http://127.0.0.1:5000/delivery-route/99b90b23-a4f7-4c3d-9ab6-5f9c576ac547'
```
Response success:

```bash
[
    {
        "bounds": {
            "northeast": {
                "lat": -29.6300501,
                "lng": -50.57674429999999
            },
            "southwest": {
                "lat": -29.7634869,
                "lng": -51.15344160000001
            }
        },
     ...
]```
