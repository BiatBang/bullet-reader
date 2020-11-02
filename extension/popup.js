'use strict';

document.getElementById("load-bullets-btn").onclick = (element) => {
    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        // alert(url)
        // use `url` here inside the callback because it's asynchronous!
        fetch('http://localhost:8080/load?url=' + url)
            .then(function(response) {
                if (response.status !== 200) {
                  console.log('Looks like there was a problem. Status Code: ' +
                    response.status);
                  return;
                }
                alert("bullets loaded!")
            }).catch(err => {
                console.log(err)
            })
    });
}