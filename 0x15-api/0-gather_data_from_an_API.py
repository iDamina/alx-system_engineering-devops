#!/usr/bin/python3
"""
A script that interacts with REST API to retrieve information
about the progress of tasks in the TODO List of a given
employee ID.
"""
import requests
import sys

if __name__ == '__main__':

    userId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + userId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    totalTasks = []
    completed = 0

    for task in tasks:
        if task.get('completed'):
            totalTasks.append(tasks)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, completed, len(tasks)))

    for task in totalTasks:
        print("\t {}".format(task.get('title')))
