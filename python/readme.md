# python -- using pyOSC

### STUPID 2 vs 3 NONSENSE:

Sources, might actually be the same by now, followed links BLINDLY from StackOverflow after realizing I have no idea which Python kids think is cool these days:

[Python2 sources](https://trac.v2.nl/wiki/pyOSC) | [Python 3 sources](https://github.com/ptone/pyosc)

Note that BOTH are included in this repo. And as of tonight's test, I got the trivial Python 3 example to execute with Python 2.7.10 without any issues....

### Usage:

Make sure that the Max patch OPEN_ME is open and:

```
python send.py
```

(Will make it go "bing" if your Audio is on...)


(Note -- it's a lot more code to do the udpsend to Python, and it's really late, so please see pyOSC `examples/knect-rcv.py` in Python 3 folder if you need to send from Max to Python...)

### Odot in Python?

We do have our set of bindings, but they're rather unfriendly right now (e.g. no way to install them automatically, for example) and I don't feel comfortable asking my students to test my software -- that's rather unethical, imo. But if you really want it, you can bug me about it. I also can't remember if I tested it thoroughly against Py2 / Py3 nonsense, though I remember cursing about that, vaguely.

### P.S. Python 3 is *superior*.
