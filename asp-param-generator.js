let daily = {
    __VIEWSTATE: null,
    __VIEWSTATEGENERATOR:null,
    __EVENTVALIDATION:null
}


// Fetches the values 
const fetch_daily_vars = async () => {

// Change this to call it through a cors server. which will allow us to fetch request
fetch('https://ggpx.info/guestreg.aspx')
  .then(body => {  
    const parser = new DOMParser();
    const html = parser.parseFromString(body, 'text/html');
    daily.__VIEWSTATE = html.getElementById('__VIEWSTATE')['value'];
    daily.__EVENTVALIDATION = html.getElementById('__EVENTVALIDATION')['value']
    daily.__VIEWSTATEGENERATOR = html.getElementById('__VIEWSTATEGENERATOR')['value']
   })
}
