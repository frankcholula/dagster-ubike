from dagster import repository
from youbike_pipeline import simple

@repository
def repo():
    return [simple]