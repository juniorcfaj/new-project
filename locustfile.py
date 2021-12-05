from locust import HttpUser, task, TaskSet, HttpLocust

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

class MyLocust(HttpLocust):
    task_set = UserBehavior
    
    min_wait = 1000
    max_wait = 4000
    
    host = http://localhost:8000
