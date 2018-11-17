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
