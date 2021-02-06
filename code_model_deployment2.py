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

Eventually solution: !pip install -U --upgrade-strategy eager azureml-sdk[automl,widgets,notebooks]==1.21.0

-------------------------------------------
scoring_uri = 'http://973f9601-a8f9-4bd4-9ade-76ee4b5d8d78.southcentralus.azurecontainer.io/score'
headers = {'Content-Type':'application/json'}

test_data = json.dumps({'data':[{
    'pclass': 0.8419164182590155,
    'age': -0.34907541344456255,
    'sibsp': -0.47908676070718687,
    'parch': -0.444999501816175,
    'fare': -0.4902404567566683,
    'age_NA': -0.5014319838391105,
    'fare_NA': -0.027650063180466557,
    'sex_male': 0.743496915331831,
    'cabin_Missing': 0.5393765119990418,
    'cabin_Rare': -0.42592011250734235,
    'embarked_Q': -0.32204029159373954,
    'embarked_Rare': -0.03911805059269843,
    'embarked_S': 0.6573935670276714,
    'title_Mr': 0.8525918887485938,
    'title_Mrs': -0.42592011250734235,
    'title_Rare': -0.27494677157229536
    }
    ]
        })

test_data2 = json.dumps({'data':[{
    'pclass': -15460978645168200,
    'age': 0.8912042887450313,
    'sibsp': -0.47908676070718687,
    'parch': -0.444999501816175,
    'fare': 19569900306355100,
    'age_NA': -0.5014319838391105,
    'fare_NA': -0.027650063180466557,
    'sex_male': -13449954927569300,
    'cabin_Missing': -18539924853119600,
    'cabin_Rare': 23478581326275300,
    'embarked_Q': -0.32204029159373954,
    'embarked_Rare': -0.03911805059269843,
    'embarked_S': -15211587854766800,
    'title_Mr': -11728941046668400,
    'title_Mrs': -0.42592011250734235,
    'title_Rare': -0.27494677157229536

    }
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
