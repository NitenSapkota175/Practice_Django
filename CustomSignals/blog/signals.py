from django.dispatch import Signal, receiver

# Creating a signal
notification = Signal()

# Receiver function
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")
