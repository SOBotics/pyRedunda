For this example, we'll be taking the name of the Redunda object as `redunda`.

# Sending a status ping

To send a status ping to Redunda, one needs to do

    redunda.sendStatusPing()

Once one sends a status ping to Redunda, the library gathers a lot of information from Redunda. I'll be recommending sending a status ping to Redunda once every 60 seconds as if one instance hasn't sent out a status ping for quite a long time, the instance might be declared dead and another instance might take over. 

# Interpreting the information received while sending a status ping

Once the bot sends a status ping to Redunda, the following information is gathered:

 - `location` (`str`): This is a string which contains the location of the instance specified on Redunda.
 - `shouldStandby` (`bool`): This is a bool which is `True` if the bot should be in standby; `False` when it shouldn't.
 - `eventCount` (`int`): This is an int which contains the total number of events which have been received by Redunda for the bot which are unread.

One can simply access these values by doing:

    print(redunda.location)
    print(redunda.shouldStandby)
    print(redunda.eventCount)
