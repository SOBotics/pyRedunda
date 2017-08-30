For this example, we'll be taking the Redunda object as `redunda`.

Redunda can receive events for the bot. To download these events, one can use:

    redunda.getEvents()

This function will return all the events in a json form.

To see the number of unread events, one can use

    redunda.eventCount

which will contain the number of unread events. Using `redunda.getEvents()` will set this count to 0 till another event is received.
