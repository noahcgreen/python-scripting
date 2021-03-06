Scripting is a boilerplate library for one-off Python scripts when you don't have an IDE or the like to work with. It
was primarily designed for Windows where scripts can be run via double-click, but it (probably) works just as well in
a variety of situations.


Here's an example what a script might look like pre-Scripting:

.. code-block:: python

    import traceback


    def do_something():
        ...
        return 200

    if __name__ == '__main__':  # Run as script
        try:  # Exceptions will close the terminal window
            print(do_something())
        except Exception:
            traceback.print_exc()  # Debug
        finally:
            input()  # Keep the window open

If all you're writing is a simple script and don't want to deal with extensive error handling, chances are you'll end
up with something like the above. If you write such scripts often, however, the amount of boilerplate adds up and
quickly becomes tedious to maintain.

Post-Scripting:

.. code-block:: python

    import scripting


    @scripting.main
    def do_something():
        ...
        return 200

Scripting takes care of exception handling, output formatting, and maintaining the terminal window for you so that you
can focus on getting your script done in the shortest amount of time possible.


Installation
------------

.. code-block:: bash

    $ pip install python-scripting
