from django.core.management.base import BaseCommand, CommandError

from ...models import Organization


class Command(BaseCommand):
    help = 'Init data of paorganizations app'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        organizations = [('AdOpera', 'adoperasrl.it'),
                         ('AscInsieme', 'ascinsieme.it'),
                         ('Casalecchio di Reno', 'comune.casalecchio.bo.it'),
                         ('Fondazione Rocca Bentivoglio',
                          'roccadeibentivoglio.it'),
                         ('Monte San Pietro', 'comune.montesanpietro.bo.it'),
                         ('Sasso Marconi', 'comune.sassomarconi.bo.it'),
                         ('Se-cim', 'se-cim.it'),
                         ('Unione UCRLS', 'unionerenolavinosamoggia.bo.it'),
                         ('Valsamoggia', 'comune.valsamoggia.bo.it'),
                         ('Zola Predosa', 'comune.zolapredosa.bo.it'),]

        for to in organizations:
            org, created = Organization.objects.get_or_create(
                email_domain=to[1], defaults={'title': to[0]})
            print(org, created)


        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
