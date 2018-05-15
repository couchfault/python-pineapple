# python-pineapple
WiFi pineapple API Wrapper written in python

## Documentation
Documentation is a work in progress. It may not be complete for a while, but I believe the code to be very readable and if you do know python it shouldn't be too hard to figure out.
Some hints:
- All modules have the same name they do on the pineapple (all lower case). To see what a module can do just run `help(fruit.getModule(modulename))`
- To find out more about the WiFi Pineapple API itself, set `debug = True` when instantiating your `Pineapple()`s and it will log the HTTP requests it makes
- Read the WiFi Pineapple php source located on your pineapple at `/pineapple/modules/$modulename/api/module.php` as well as the corresponding python files in this project

## Examples:
##### Instantiate a Pineapple object:
<pre>
API_TOKEN = "xxxxxxxxxx..."
from pineapple.pineapple import Pineapple
fruit = Pineapple(API_TOKEN)
</pre>
##### Add a notification:
<pre>
fruit.getModule("notifications").addNotification("test")
</pre>
##### Start PineAP
<pre>
fruit.getModule("pineap").enable()
</pre>
##### Deauth/dissasoc the clients `73:65:62:6b:69:6e` and `6e:65:73:67:69:61` from the bssid `6e:74:64:69:63:6b` 5 times on channel 1
<pre>
fruit.getModule("pineap").deauth('6e:74:64:69:63:6b', ['73:65:62:6b:69:6e', '6e:65:73:67:69:61'], 5, 1)
</pre>

*To generate API tokens, use the [API Tokens](https://github.com/735tesla/Pineapple-API-Tokens-Module/) module*
