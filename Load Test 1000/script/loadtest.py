from locust import HttpUser, task, between
import json

class Test(HttpUser):
    wait_time = between(1,2)
    host = "https://reqres.in"
    
    @task
    def userRegister(self):
        self.client.post("/api/register", json={"username":"eve.holt@reqres.in", "password":"pistol"})

    @task
    def userLogin(self):
        self.client.post("/api/login", json={"email":"eve.holt@reqres.in", "password":"cityslicka"})

    @task
    def userCreate(self):
        self.client.post("/api/users", json={"name":"morpheus", "job":"leader"})
        
      