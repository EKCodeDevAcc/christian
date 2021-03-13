import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index_page(self):
        self.client.get(url="")

    @task
    def detail_page_one(self):
        self.client.get(url="product/705071")

    @task
    def detail_page_two(self):
        self.client.get(url="product/08790")
