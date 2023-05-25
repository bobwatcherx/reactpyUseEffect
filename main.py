from fastapi import FastAPI
from reactpy import component,html,use_state,use_effect
from reactpy.backend.fastapi import configure
import requests


@component
def myhome():

	alldata,set_alldata = use_state([])
	myurl = use_state("https://jsonplaceholder.typicode.com/todos")


	def sample():
		r = requests.get(myurl.value)
		if r.status_code == 200:
			data = r.json()
			set_alldata(data)
		else:
			print("ERRROR")


	# INSERT USE EFFECT HERE

	use_effect(sample)


	return html.div(
		html.h1("get api placeholder"),
		# AND NOW I LOOP FOR alldata IN LIST

		html.ul([
			html.li(
		f"{i['id']} / {i['title']} - {i['completed']}"
		
		) for i  in alldata
			])


		)




app = FastAPI()
configure(app,myhome)