# click-clock-bitcoin API
# This is a little daily project.

- You can find the current value of bitcoin by using this website. 
- FastAPI is used to create API
- Deta is used to deploy this API

JavaScript codes :

- service.jws 
```
import {fetch} from 'wix-fetch'

export function btc() {
    const url = 'https://pp4xad.deta.dev/btc/btc_service/';
    console.log("Url : " + url);

    return fetch(url, {method : 'get'}).then(response => response.json())
}
```
- homepage

```
export function section2_viewportEnter(event) {
	// This function was added from the Properties & Events panel. To learn more, visit http://wix.to/UcBnC-4
	// Add your code for this event here: 
	var intervalId = setInterval(function(){
  // call your function here
	    btc()
	          .then(currencyInfo => {
	              $w("#text1").text = currencyInfo + "$";
	              });
	}, 1000);

}

```
