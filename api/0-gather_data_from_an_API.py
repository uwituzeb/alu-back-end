#!/usr/bin/python3

import requests
from sys import argv


def todo(userid):
    name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{userid}').json().get('name')

    tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{userid}/todos').json()
    tasksDone = [f'\t {dic.get("title")}\n' for dic in tasks if dic.get('completed')]
    if name and tasks:
        print(f"Employee {name} is done with tasks({len(tasksDone)}/{len(tasks)}):")
        print(''.join(tasksDone), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))