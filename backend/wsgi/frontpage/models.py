from django.db import models
from filebrowser.fields import FileBrowseField


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(
        help_text='The image provided will redirect to this url onclick'
    )
    image = FileBrowseField('Image',
                            max_length=200,
                            directory='sponsor/',
                            extensions=['.jpg', '.png', '.jpeg', '.gif'],
                            blank=False,
                            null=False,
                            help_text='This image will appear on the frontpage')

    def __repr__(self):
        return self.name
