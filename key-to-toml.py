# key-to-toml.py - Sunday, November 7, 2021
""" Convert JSON secrets to TOML """
import os
import toml
from datetime import datetime
from os.path import exists


def json2toml(input_filename, output_filename):
	if exists(input_filename):
		with open(input_filename) as json_file:
			json_text = json_file.read()

		config = {"textkey": json_text}
		toml_config = toml.dumps(config)

		if exists(output_filename):
			os.rename(output_filename, output_filename + '~.%s' % datetime.now().astimezone().timestamp())
		with open(output_filename, "w") as target:
			target.write(toml_config)


input_filename = "firestore-key.json"
output_filename = ".streamlit/secrets.toml"
json2toml(input_filename, output_filename)


input_filename = "adminsdk-key.json"
output_filename = ".streamlit/adminsdk-secrets.toml"
json2toml(input_filename, output_filename)
