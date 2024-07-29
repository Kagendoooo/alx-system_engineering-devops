#!/usr/bin/python3
"""Gather data from REST API & export it to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    file_name = "{}.json".format(sys.argv[1])

    t = []
    for task in todos:
        t.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })
    data = {str(sys.argv[1]): t}
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)

    print(f"Data exported to {file_name}")
