import os, requests

def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)
