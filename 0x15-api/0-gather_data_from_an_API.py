#!/usr/bin/python3
"""
A script that interacts with REST API to retrieve information
about the progress of tasks in the TODO List of a given
employee ID.
"""
import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_info = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    # retrieve the TODO list for the specified employee
    completed_tasks = [title.get("title") for title in to_do if
                       title.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(usr_info.get("name"),
                                                          len(completed_tasks),
                                                          len(to_do)))
    [print("\t{}".format(title)) for title in completed_tasks]
