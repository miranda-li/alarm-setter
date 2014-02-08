from flask import Flask, render_template, request
from datetime import timedelta, datetime


app = Flask (__name__)
#only include while testing
app.config["DEBUG"] = True

@app.route("/")
def home():
	return render_template("page.html")
		

@app.route("/results", methods=["GET","POST"])
def results():
	if request.method == "POST":
		
		leave_time = str(request.form["time"])
		
		morning_items = [request.form["teeth"],request.form["shower"], request.form["dress"], request.form["eat"], request.form["makeup"], request.form["hair"], request.form["bed"], request.form["other"]]
		morning_items = [int(i if i else 0) for i in morning_items]
		
	final_result = find_time(morning_items, leave_time)
	
	return render_template("results.html", final_result = final_result)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, page not found."

def find_time(a,b):

	b = datetime.strptime(b, '%H:%M')
	sum_of_time = 0
	for time in a: # [10,20,30]
		sum_of_time += time
	change_in_time = timedelta(minutes=-(sum_of_time))
	new_time =  b + change_in_time
	new_time = new_time.strftime('%H:%M')
	#b = b.time()
	return new_time

if __name__=="__main__":
	app.run(host="0.0.0.0")