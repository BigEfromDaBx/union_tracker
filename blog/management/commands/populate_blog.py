from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Post, Comment
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Populate the database with fake blog posts and comments'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate fake users (authors)
        if User.objects.count() == 0:
            self.stdout.write(self.style.WARNING('No users found. Creating a default user.'))
            User.objects.create_user('admin', 'admin@example.com', 'password')
        
        users = User.objects.all()

        # Generate fake blog posts
        for _ in range(20):  # Adjust the range for the number of fake posts
            title = fake.sentence(nb_words=6)
            slug = fake.slug()
            content = fake.paragraph(nb_sentences=10)
            author = random.choice(users)
            published = random.choice([True, False])

            post = Post.objects.create(
                title=title,
                slug=slug,
                content=content,
                author=author,
                published=published,
            )

            # Generate fake comments for each post
            for _ in range(random.randint(1, 5)):  # Adjust range for the number of comments per post
                Comment.objects.create(
                    post=post,
                    name=fake.name(),
                    email=fake.email(),
                    body=fake.paragraph(nb_sentences=3),
                    active=random.choice([True, False]),
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake blog posts and comments.'))