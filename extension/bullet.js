var vid = document.getElementsByTagName("video")[0];
vid.addEventListener('playing', function(e) {
    console.log('The video is playing!');
    let time = Math.round(e.srcElement.currentTime)
    console.log(time)
    fetch('http://localhost:8080/read?time=' + time)
        .then(function(response) {
            if (response.status !== 200) {
                console.log('Looks like there was a problem. Status Code: ' +
                response.status);
                return;
            }
        }).catch(err => {
            console.log(err)
        })
});

vid.addEventListener('pause', function(e) {
    console.log('The video is on pause!');
    fetch('http://localhost:8080/stop')
        .then(function(response) {
            if (response.status !== 200) {
                console.log('Looks like there was a problem. Status Code: ' +
                response.status);
                return;
            }
        }).catch(err => {
            console.log(err)
        })
});