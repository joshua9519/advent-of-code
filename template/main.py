from jinja2 import Environment, FileSystemLoader
import sys
import os


environment = Environment(loader=FileSystemLoader("day/"))
template = environment.get_template("main.py.tmpl")

year = sys.argv[1]
day = sys.argv[2]
filepath = "../{}/{}".format(year, day)

os.mkdir(filepath)

files = ["__init__.py", "input.txt"]
for f in files:
    with open("{}/{}".format(filepath, f), "w"):
        pass

with open("{}/main.py".format(filepath), mode="w", encoding="utf-8") as results:
    results.write(template.render({
        "year": year,
        "day": day,
    }))
