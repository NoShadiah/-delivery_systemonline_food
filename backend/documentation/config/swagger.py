template = {
    "swagger":"2.0",
    "info":{
        "title":"Online food delivery API",
        "description":"An API for an online food delivering restaurant",
        "contact":{
            "responsibleOrganisation":"KP techs",
            "responsibleDeveloper":"KisaProm",
            "email":"kisaprom@gmai.com",
            "url":"https://github.com/NoShadiah"
        },
        "termsOfService":"www.twitter.com.deve",
        "version":"1.0"   
    },
    # This is the base hash for the blue prints registration 
    "basePath":"api/v1", 
    "schemes":[
        "http",
        "https"
    ],
    "securityDefinitions":{
        "Bearer":{
            "type":"apiKey",
            "name":"Authorization",
            "in":"header",
            "description":"JWT Authorization header using the Bearer scheme. Example:\"Authorization:Bearer {token}\""
        }
    }
}

swagger_config = {
    "headers":[
    ],
    "specs":[{
            "endpoint":'apispec',
            "route":'/apispec.json',
            # all in
            "rule_filter":lambda rule:True,
            # all in
            "model_filter":lambda tag: True,  
    }], 
    "static_url_path":"/flasgger_static",
    # use the swagger ui to view things in a good way (the api)
    "swagger_ui": True,
    # helps set a default to be seen at the homepage (documentation)
    "specs_route":"/"

    # this has to be configured directly to the app in the __init__.py
}