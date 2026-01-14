from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Full Name"
    )

    email = models.EmailField(
        verbose_name="Email Address",
        db_index=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Phone Number"
    )

    subject = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Subject",
        db_index=True
    )

    message = models.TextField(
        verbose_name="Message"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="Read"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Received At",
        db_index=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        subject = self.subject if self.subject else "No Subject"
        return f"{self.name} | {subject}"
