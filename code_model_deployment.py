#Truco:

### ModelDeployment:
model = Model.register(workspace = ws,
                        model_path ="outputs/automl_hearth.pkl",
                        model_name = "automl_hearth")

# model = Model.register(model_path = "./models/automl_hearth.pkl",
#                       model_name = "automl_hearth.pkl",
#                       description = "Best model trained with AutoML",
#                       workspace = ws, model_framework=Model.Framework.SCIKITLEARN)
print(model.name)
--------------------------------------------------------------------------

# Define Deployment

aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=2,
                                              enable_app_insights=True) 

# deployment_config = AciWebservice.deploy_configuration()

-------------------------------------------------------------------------

# Create the environment

env = Environment.from_conda_specification(name='myenv',file_path = 'env.yml')

# myenv = Environment(workspace=ws, name="myenv")

inference_config = InferenceConfig(entry_script='./score.py',
                                    environment=env)

f = open("envnew.yml", "w")
f.write(env.python.conda_dependencies.serialize_to_string())
f.close()

print("packages", env.python.conda_dependencies.serialize_to_string())
-------------------------------------------------------------------------------

service_name = 'my-service'

service = Model.deploy(ws, service_name, [model], inference_config, deployment_config=aci_config)

-------------------------------------------------------------------------------

service.wait_for_deployment(True)
print(service.state)


-------------------------------------------------------------------------------

scoring_uri = 'http://973f9601-a8f9-4bd4-9ade-76ee4b5d8d78.southcentralus.azurecontainer.io/score'
headers = {'Content-Type':'application/json'}

test_data = json.dumps({'data':[{
    'age':75,
    'anaemia':0,
    'creatinine_phosphokinase':582,
    'diabetes':0,
    'ejection_fraction':20,
    'high_blood_pressure':1,
    'platelets':265000,
    'serum_creatinine':1.9,
    'serum_sodium':130,
    'sex':1,
    'smoking':0,
    'time':4}
    ]
        })

test_data2 = json.dumps({'data':[{
    'age':40,
    'anaemia':0,
    'creatinine_phosphokinase':321,
    'diabetes':0,
    'ejection_fraction':35,
    'high_blood_pressure':0,
    'platelets':265000,
    'serum_creatinine':1,
    'serum_sodium':130,
    'sex':1,
    'smoking':0,
    'time':198}
    ]
        })


response = requests.post(scoring_uri, data=test_data2, headers=headers)

print("Result:",response.text)

----------------------------------------------------------------
print(service.get_logs())
-----------------------------------------------------------

print(response.status_code)
print(response.elapsed)
print(response.json())
-----------------------------------------------------------
service.delete()


