from flask import Flask, Jsonify, make_response, json, Response 
from flask restx import Resoure, Api
import json

app Flask("app_name")
api Api(app)

ns api.namespace ('options', description='Provide option List)

@ns.route("/postgredbapp/env/<env>/app/<appl>/server/<server>")
@ns.route("/postgredbapp/env/<env>/app/<appl>")
@ns.route("/postgredbapp/env/<env>")

class Options (Resource):

	def builddatalist(self, datalist, value, keyname, keyvalue) :
		for row in value:
			dataval = {}
			dataval['name'] = row[keyname]
			dataval['value'] = row[keyvalue]
			datalist.append(dataval)
		retuen datalist
			
	def get(self, env, appl=None, server=None)
		with open("database.json".format(""), "r") as f:
             json_val json.load (f)
             datalist = []
             for envrow in json_val:
				if(envrow ["envname"] == env):
                   envvalue = envrow["envvalue"]
                   if(appl != None):
                      for approw in envvalue:
                        if(approw["appvalue"]) == appl):
							servervalue = approw["servers"]
							if (server != None):
							  for serverrow in servervalue:
							    if(serverrow["servername"]) == server):
								  schemavalue = serverrow["schemas"]
								  # to get list of schemas of a particular app in a given env
								  datalist = self.builddatalist(datalist, schemavalue, "schemaname", "schemavalue")
					        else:
							  # to get list of servers of a particular app in a given env
							  datalist = self.builddatalist(datalist, servervalue, "servername", "servervalue")
							  break
			        else:
					# to get list of apps in a given env
					datalist = self.builddatalist(datalist, envvalue, "appname", "appvalue")
					break
			returnval = json.dumps(datalist)
			return returnval
			
if __name__ = "__main__":
    app.run(port=5000, debug=False, host='0.0.0.0')