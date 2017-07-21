import csv

from django.core.management.base import BaseCommand, CommandError

from ...models import (Organization, Person, Assignment, TelephoneNumber)


class Command(BaseCommand):
    help = 'Import cdr address book'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str)




    def handle(self, *args, **options):

        organizations = Organization.objects.all()

        with open(options['csv_file_path']) as f_csv:
            reader = csv.reader(f_csv, delimiter=',')

            organizations = Organization.objects.all()

            n = 0

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

                    assignment, a_creted = Assignment.objects.get_or_create(
                        organization=organization, person=person)

                    # internal numbers
                    if row[3].strip():
                        for int_number in row[3].strip().split(' '):
                            #print(int_number)
                            o_int_number, created = (
                                TelephoneNumber.objects.get_or_create(
                                    number=int_number, type='internal'))

                            assignment.telephone_numbers.add(o_int_number)

                    # external numbers
                    if row[11].strip():
                        for ext_number in row[11].strip().split(' '):
                            if ext_number.startswith('51'):
                                ext_number = '0' + ext_number
                            # print(ext_number)
                            o_ext_number, created = (
                                TelephoneNumber.objects.get_or_create(
                                    number=ext_number, type='external'))

                            assignment.telephone_numbers.add(o_ext_number)

                    # fax numbers
                    if row[12].strip():
                        for fax_number in row[12].strip().split(' '):
                            if fax_number.startswith('51'):
                                fax_number = '0' + ext_number
                            print(fax_number)
                            o_fax_number, created = (
                                TelephoneNumber.objects.get_or_create(
                                    number=fax_number, type='fax'))

                            assignment.telephone_numbers.add(o_fax_number)

                    print(person, organization, " ** ", assignment)


                # n += 1
                # if n == 30:
                #     break


                    # if person:
                    #     if person.cdr_ab_id != row[0]:
                    #         person.cdr_ab_id = row[0]
                    #         person.save()


