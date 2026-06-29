from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sse_starlette.sse import EventSourceResponse
import asyncio

app = FastAPI()


@app.get("/")
async def home():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SSE Counter</title>
    </head>
    <body>

        <h1>Live Counter using SSE</h1>

        <h2 id="counter">Waiting...</h2>

        <script>
            const source = new EventSource("/events");

            source.onmessage = function(event){
                document.getElementById("counter").innerHTML = event.data;
            };

            source.onerror = function(){
                console.log("Connection closed");
            };
        </script>

    </body>
    </html>
    """)


@app.get("/events")
async def events():

    async def event_generator():

        counter = 1

        while True:

            yield {
                "data": f"Counter : {counter}"
            }

            counter += 1

            await asyncio.sleep(1)

    return EventSourceResponse(event_generator())