from OSC import OSCClient, OSCBundle

client = OSCClient()
client.connect(("localhost", 54345))

### Create a bundle:
bundle = OSCBundle()
bundle.append({'addr': "/frequency", 'args':[440.]})
bundle.append({'addr': "/envelope/line", 'args': [1., 20, 0., 1000]})

client.send(bundle)