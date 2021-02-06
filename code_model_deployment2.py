from azureml.core import Model
from azureml.core.webservice import AciWebservice, Webservice
model = best_run.register_model(model_name='model_name', model_path='./outputs/model_name.pkl',
                       model_framework=Model.Framework.SCIKITLEARN)
aci_config AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=2,
                                                enable_app_insights=True, auth_enabled=True)  
service_name = 'my-sklearn-service'
service = Model.deploy(ws, service_name, [model], deployment_config=aci_config)
service.wait_for_deployment(show_output = True)
print(service.get_logs())


import requests
import json
# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = ''
# If the service is authenticated, set the key or token
key = ''
# Two sets of data to score, so we get two results back
data = {
  YOUR SAMPLE DATA
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)
# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'
# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
