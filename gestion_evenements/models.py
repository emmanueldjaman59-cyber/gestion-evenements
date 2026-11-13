from django.db import models


class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    lieu = models.CharField(max_length=200)
    date_evenement = models.DateField()
    heure = models.TimeField()

    def __str__(self):
        return self.titre


class Inscription(models.Model):
    participant = models.CharField(max_length=150)
    email = models.EmailField()

    evenement = models.ForeignKey(
        Evenement,
        on_delete=models.CASCADE,
        related_name="inscriptions"
    )

    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email", "evenement"],
                name="unique_email_par_evenement"
            )
        ]

    def __str__(self):
        return f"{self.participant} - {self.evenement.titre}"