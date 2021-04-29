# Courses
## _The django rest framework test task_



## installation

- download a repository
- For the install a packages you can use the commands: 
```sh
pip install requirements.txt
```

for installation raw date use fixtures
python manage.py loaddata fixtures/fixtures_data.json --courses_app.Course

## features
For classic version use a /courses/ urls
- /courses/ - list of all courses
- /courses/<pk>/ - detail information about course
- /courses/<pk>/update/
- /courses/<pk>/delete/
- /courses/create/

For api version use /api/ urls
- api documentation you can see on /swagger-docs/ url

