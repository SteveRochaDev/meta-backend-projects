from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from LittleLemonAPI.models import Category, MenuItem


class Command(BaseCommand):
    help = 'Seed initial data for Little Lemon project'

    def handle(self, *args, **options):
        # Create groups
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        delivery_group, _ = Group.objects.get_or_create(name='Delivery crew')

        # Create superuser if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            self.stdout.write(self.style.SUCCESS('Created superuser admin/adminpass'))

        # Create example users
        if not User.objects.filter(username='manager').exists():
            manager = User.objects.create_user('manager', password='managerpass')
            manager_group.user_set.add(manager)
            self.stdout.write(self.style.SUCCESS('Created manager/managerpass'))

        if not User.objects.filter(username='delivery').exists():
            delivery = User.objects.create_user('delivery', password='deliverypass')
            delivery_group.user_set.add(delivery)
            self.stdout.write(self.style.SUCCESS('Created delivery/deliverypass'))

        if not User.objects.filter(username='customer').exists():
            User.objects.create_user('customer', password='customerpass')
            self.stdout.write(self.style.SUCCESS('Created customer/customerpass'))

        # Helper to get or create category safely if duplicates exist
        def ensure_category(slug, title):
            qs = Category.objects.filter(slug=slug)
            if qs.exists():
                return qs.first()
            return Category.objects.create(slug=slug, title=title)

        # Create categories
        cat1 = ensure_category('starters', 'Starters')
        cat2 = ensure_category('mains', 'Mains')
        cat3 = ensure_category('desserts', 'Desserts')

        # Create menu items (avoid duplicates by using get_or_create with title and category)
        MenuItem.objects.get_or_create(title='Bruschetta', defaults={'price': '6.50', 'featured': False, 'category': cat1})
        MenuItem.objects.get_or_create(title='Greek salad', defaults={'price': '5.50', 'featured': False, 'category': cat1})
        MenuItem.objects.get_or_create(title='Grilled Salmon', defaults={'price': '15.00', 'featured': True, 'category': cat2})
        MenuItem.objects.get_or_create(title='Lemon Cake', defaults={'price': '4.00', 'featured': False, 'category': cat3})

        self.stdout.write(self.style.SUCCESS('Seed data created'))
