"""Welcome to Reflex!."""

# Import all the pages.
from moflexapp01.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""
    label = "What is your name ?"
    def handle_title_input_change(self, val):
        self.value=val
        


# Create the app.
app = rx.App()
