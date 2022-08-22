from OMSimulator import OMSimulator, Types
import json
import requests

oms = OMSimulator()
model, status = oms.importFile("s1s2.ssp")
print(Types.Status(status))

oms.setResultFile(model, "results.csv", bufferSize=10)

oms.instantiate(model)
oms.setReal('s1s2.Root.Reaction_model.Temperature', 299.15)
oms.setReal('s1s2.Root.Reaction_model.grams_yeast', 11.5)
oms.setReal('s1s2.Root.Reaction_model.sg_0', 1.054)
oms.setReal('s1s2.Root.Reaction_model.batch_volume', 20)
oms.setReal('s1s2.Root.control_model.T_set', 22)
oms.setReal('s1s2.Root.control_model.T_sensor', 19)


oms.initialize(model)
oms.simulate(model)
url = "https://b3de-104-28-250-40.eu.ngrok.io/pump"
headers = {'Content-type': 'application/json'}
command = {"command": int(oms.getReal('s1s2.Root.control_model.control_signal')[0])}
r = requests.post(url, data=json.dumps(command), headers=headers)
oms.terminate(model)
oms.delete(model)