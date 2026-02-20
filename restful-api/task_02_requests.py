#!/usr/bin/python3
"""
Module that fetches posts from a RESTful API and either prints their titles
or saves them to a CSV file.
"""
import requests
import csv
url = "https://jsonplaceholder.typicode.com/posts/"


def fetch_and_print_posts():
    """
    Fetches posts from the API and prints their titles.
    If the request fails, it prints "Status Code: None".
    """
    try:
        request = requests.get(url)
    except requests.RequestException:
        print("Status Code: None")
        return

    print(f"Status Code: {request.status_code}")
    if request.status_code == 200:
        try:
            posts = request.json()
        except ValueError:
            print("Status Code: None")
            return
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from the API and saves them to a CSV file.
    If the request fails, it prints "Status Code: None".
    """
    try:
        request = requests.get(url)
    except requests.RequestException:
        print("Status Code: None")
        return

    print(f"Status Code: {request.status_code}")
    if request.status_code == 200:
        try:
            posts = request.json()
        except ValueError:
            print("Status Code: None")
            return
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body")
                })
