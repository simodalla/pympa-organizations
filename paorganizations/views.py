# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Organizations,
	Office,
	Person,
)


class OrganizationsCreateView(CreateView):

    model = Organizations


class OrganizationsDeleteView(DeleteView):

    model = Organizations


class OrganizationsDetailView(DetailView):

    model = Organizations


class OrganizationsUpdateView(UpdateView):

    model = Organizations


class OrganizationsListView(ListView):

    model = Organizations


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

