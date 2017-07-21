import csv

from django.core.management.base import BaseCommand, CommandError

from ...models import Organization, Person, Assignment


class Command(BaseCommand):
    help = 'Import cdr address book'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)




    def handle(self, *args, **options):

        organizations = Organization.objects.all()

        with open(options['csv_file_path']) as f_csv:
            reader = csv.reader(f_csv, delimiter=',')

            organizations = Organization.objects.all()

            for row in reader:
                name = row[1].strip().lower().title().split()
                # print(name, len(row[13]))
                if ((len(name) == 2 and row[13] == '')
                        or (len(name) > 2 and row[13] == 'si')):
                    # print(name)

                    if len(name) == 2:
                        first_name = name[1]
                        last_name = name[0]
                    else:
                        nc = int(row[14])
                        first_name = ' '.join(name[nc:])
                        last_name = ' '.join(name[:nc])
                        # print(first_name, "--", last_name)

                    person = Person.objects.filter(
                        last_name__iexact=last_name,
                        first_name__iexact=first_name).first()



                    if person is None:
                        print("{} {} --> person {} --> org {}".format(
                            last_name, first_name, person, row[4]))
                        person = Person.objects.create(
                            first_name=first_name, last_name=last_name,
                            cdr_ab_id=row[0])

#                    print(person, person.pk)

                    try:
                        organization = organizations.get(title=row[4])
                    except Organization.DoesNotExist:
                        organization = organizations.get(
                            title='Casalecchio di Reno')
                        #print("**** {}".format(row[4]))

                    t_assignment = Assignment.objects.get_or_create(
                        organization=organization, person=person)

                    print(person, organization, t_assignment)


                    # if person:
                    #     if person.cdr_ab_id != row[0]:
                    #         person.cdr_ab_id = row[0]
                    #         person.save()


