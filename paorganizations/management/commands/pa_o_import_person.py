import csv
import os

from django.core.management.base import BaseCommand, CommandError

from ...models import Organization, Person, Assignment


class Command(BaseCommand):
    help = 'Init data of paorganizations app'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)

    def handle(self, *args, **options):

        organizations = Organization.objects.all()

        with open(options['csv_file_path']) as f_csv:
            reader = csv.reader(f_csv, delimiter=',')

            for row in reader:
                first_name = row[2].strip().lower().title()
                last_name = row[1].strip().lower().title()
                t_person = Person.objects.get_or_create(
                    register_number=row[0],
                    defaults={'first_name': first_name,
                              'last_name': last_name})
                print("person: {}".format(t_person))
                t_assignment = Assignment.objects.get_or_create(
                    organization=organizations.get(title=row[3]),
                    person=t_person[0])
                print("assignment: {}".format(t_assignment))
