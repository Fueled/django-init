# Standard Library
import os
from os.path import dirname, abspath

parent_dir = dirname(dirname(abspath(__file__)))
os.system(f"python {parent_dir}/manage.py graph_models -a > db.dot  && dot -Tsvg db.dot -o db.svg")
os.system(f"mv db.svg {parent_dir}/docs/backend/database-schema.svg")
os.system("rm db.dot")
