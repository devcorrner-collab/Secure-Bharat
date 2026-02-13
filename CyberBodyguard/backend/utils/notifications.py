def show_notification(title, message, timeout=5000):
    """Show desktop notification"""
    try:
        from plyer import notification
        notification.notify(
            title=title,
            message=message,
            timeout=timeout
        )
    except Exception as e:
        print(f" Notification Error: {e}")
