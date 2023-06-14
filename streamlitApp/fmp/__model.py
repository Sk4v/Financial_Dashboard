class Model:
    def __init__(self):
        self.values = []
        self.response = None

    def from_json(self,response):
        json_params = response.json()[0]
        self.from_dict(json_params)
        self.response = response

    def from_json_list(self,param_list,response):
        json_params = response.json()
        for element in json_params:
            param_list.append(element)

