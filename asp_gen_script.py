import requests as req

# TODO: make this update the db every time it is ran on a chron job
homepage = req.get("https://ggpx.info/guestreg.aspx")

homepage = homepage.text

viewstate = homepage.split('id="__VIEWSTATE" value="')[1].split('"')[0]
viewstateGenerator = homepage.split('id="__VIEWSTATEGENERATOR" value="')[1].split('"')[0]
eventvalidation = homepage.split('id="__EVENTVALIDATION" value="')[1].split('"')[0]

print(f"viewstate: {viewstate}")
print(f"viewstateGenerator: {viewstateGenerator}")
print(f"eventvalidation: {eventvalidation}")
