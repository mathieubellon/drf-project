def main():
    fake: Faker = Faker()

    for i in range(3000):
        idea = Idea.objects.create(
            name=fake.paragraph(nb_sentences=1),
            content=fake.text(),
        )
        print(f"Created todo. Name: {idea.name}  Content: {idea.content}")

    idea_count = Idea.objects.count()

    print(f"There are {idea_count} ideas in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "decide.settings")
    application = get_wsgi_application()

    import random

    from faker import Faker
    from ideas.models import Idea

    main()


    