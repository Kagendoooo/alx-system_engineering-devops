#!/usr/bin/python3
"""Gather data from REST API & export to CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    file_name = "{}.csv".format(sys.argv[1])
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                sys.argv[1],
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])
    print(f"Data exported to {file_name}")
