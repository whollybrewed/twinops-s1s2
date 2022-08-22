from OMSimulator import OMSimulator, Types
import json
oms = OMSimulator()
model, status = oms.importFile("s1.ssp")
print(Types.Status(status))

oms.setResultFile(model, "results.csv", bufferSize=10)

oms.instantiate(model)
oms.setReal('s1.Root.Reaction_model.Temperature', 299.15)
oms.setReal('s1.Root.Reaction_model.grams_yeast', 11.5)
oms.setReal('s1.Root.Reaction_model.sg_0', 1.054)
oms.setReal('s1.Root.Reaction_model.batch_volume', 20)


oms.initialize(model)
oms.simulate(model)
with open('control.json', 'w') as f:
    command = {"command": int(oms.getReal('s1.Root.control_model.control_signal')[0])}
    f.write(json.dumps(command))
oms.terminate(model)
oms.delete(model)