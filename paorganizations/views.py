# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (Organization, Office, Person, )


class OrganizationCreateView(CreateView):

    model = Organization


class OrganizationDeleteView(DeleteView):

    model = Organization


class OrganizationDetailView(DetailView):

    model = Organization


class OrganizationUpdateView(UpdateView):

    model = Organization


class OrganizationListView(ListView):

    model = Organization


class OfficeCreateView(CreateView):

    model = Office


class OfficeDeleteView(DeleteView):

    model = Office


class OfficeDetailView(DetailView):

    model = Office


class OfficeUpdateView(UpdateView):

    model = Office


class OfficeListView(ListView):

    model = Office


class PersonCreateView(CreateView):

    model = Person


class PersonDeleteView(DeleteView):

    model = Person


class PersonDetailView(DetailView):

    model = Person


class PersonUpdateView(UpdateView):

    model = Person


class PersonListView(ListView):

    model = Person

