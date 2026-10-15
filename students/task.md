#C-> Create R -> Read U -> Update D -> Delete
Create two new students: Gopal, Harry
Update the age of Gopal
Update the email of Harry
Filter the collection


```
Student.objects.create(
    name="Harry",
    email="hari@example.com",
    age=18,
    address="Dhankuta"
)
```

Create Model : 
Course : name
Subject: name

Run command:
`uv run python manage.py makemigrations`
`uv run python manage.py migrate`

Go into shell: `uv run python manage.py shell`
import: `from students.models import Course, Subject`

task: Add 4 courses and 4 subjects using ORM 
Try CRUD operation for course and subject


View Page:
- if there is not course/subject the course/subject label should not be seen
- subject should be in list <li> form

All page:
- create a navbar to link all the pages