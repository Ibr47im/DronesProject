from flask import Flask, render_template, request
import Drone
import GroundControlStation
import asyncio

app = Flask(__name__)
gr = GroundControlStation.GroundControlStation()

async def main():
    dr = Drone.Drone()
    await dr.init_drone()
    await dr.start_drone_receive()

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html')


@app.route("/startdrone")
def startdrone():
    asyncio.run(main())
    return render_template('index.html')

@app.route("/arm")
def arm():
    try:
        gr.arm()
        return render_template('index.html')
    except Exception as e:
        print("error: ",e)
        return '{"can not arm the drone for some reason"}'

@app.route("/takeoff")
def take_off():
    try:
        gr.takeoff(10)
        return render_template('index.html')
    except Exception as e:
        print("error: ",e)
        return '{"take_off" : "failed"}'

@app.route("/land")
def land():
    try:
        gr.land()
        return render_template('index.html')
    except Exception as e:
        print("error:",e)
        return '{"There was an error while executing this method"}'

# @app.route("/disarm")
# def disarm():
#     try:
#         gr.disarm()
#         return render_template('index.html')
#     except Exception as e:
#         print("error:",e)
#         return '{"There was an error while executing this method"}'

@app.route("/goto")
def goto():
    try:
        gr.goto()
        return render_template('index.html')
    except Exception as e:
        print("error:",e)
        return '{"There was an error while executing this method"}'

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
    
    

