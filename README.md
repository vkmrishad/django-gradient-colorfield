# django-gradient-colorfield

This module fills the need of having a **colorfield** that's usable in both
django models and forms.

Makes use of [lgcolor](https://github.com/vkmrishad/gradient-color-picker).

## Installation
- Add ``gradient_colorfield folder to project root``
- Add ``gradient_colorfield`` to your ``INSTALLED_APPS``
- Collect static files with ``./manage.py collectstatic``

## Usage
In your models, you can use it like this:

```python
from django.db import models

from gradient_colorfield.fields import GradientColorField


class AppModel(models.Model):
   header_background = GradientColorField(verbose_name=u'Header Background',
                                          default='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)'
                                          )
   footer_background = GradientColorField(verbose_name=u'Footer Background',
                                          default='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)'
                                          )

   def __str__(self):
       return 'Gradient{}'.format(self.id)
```

In your ModelForm, you can use it like this:

```python
from django import forms
from app.models import AppModel

class AppForm(forms.ModelForm):
   class Meta:
       model = AppModel
       fields = ['header_background', 'footer_background']

```

In your FormWidget, you can use it like this:

```python
from django import forms

from gradient_colorfield.fields import GradientColorWidget

class AppForm(forms.ModelForm):
    header_background = forms.CharField(label='Header Background', max_length=20, widget=GradientColorWidget(),
                                        initial='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)',
                                       )
    footer_background = forms.CharField(label='Footer Background', max_length=20, widget=GradientColorWidget(),
                                       initial='linear-gradient(to bottom, #00f260 0%, #0575e6 100%)')
```

In your Template, you can use it like this:

```python
{{form.media}}

{% for field in form %}
    {{field}}
{% endfor %}
```

## Run Sample App
- Create virtualenv ``virtualenv -p $(which python3.6) env3`` -- Python 3.6
- Activate virtualenv ``source env3/bin/activate``
- Install Dependency``pip install -r requirements.txt``
- Migrate ``cd sample-app && python manage.py migrate``
- Run Django Sample-app ``python manage.py runserver``
