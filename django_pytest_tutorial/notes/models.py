from django.db import models
from django.utils.translation import gettext as _


class Note(models.Model):
    title = models.CharField(
        max_length=200, help_text=_('The title for the note.')
    )
    summary = models.TextField(
        blank=True, null=True,
        help_text=_('Briefly describe your note.')
    )
    text = models.TextField(
        help_text=_('The actual note you want to write.')
    )
    owner = models.ForeignKey(
        'accounts.CustomUser', related_name='note', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(
        auto_now_add=True, help_text=_('The time when this note was created.')
    )

    def __str__(self):
        return f"Note by {self.owner} on {self.created_on}"
