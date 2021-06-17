let panorama;
let map;
let marker;
let latlng;
var json = {};
json.list = [];

function processSVData(data, status) {
    if (status === "OK") {
        const location = data.location;
        latLng = location.latLng;
        marker.setPosition(location.latLng);
        panorama.setPano(location.pano);
        panorama.setPov({
            heading: 270,
            pitch: 0,
        });
        panorama.setVisible(true);
    } else {
        console.error("Street View data not found for this location.");
    }
}

function initialize() {
    const mimuw = { lat: 52.211916160272324, lng: 20.98251877698795};
    const sv = new google.maps.StreetViewService();

    map = new google.maps.Map(document.getElementById("map"), {
        center: mimuw,
        zoom: 14,
        disableDefaultUI: true,
        clickableIcons: false,
    });

    panorama = new google.maps.StreetViewPanorama(
        document.getElementById("pano"),
        {
            position: mimuw,
            pov: {
                heading: 34,
                pitch: 10,
            },
        }
    );

    marker = new google.maps.Marker({
        position: mimuw,
        map,
    });
    
    map.setStreetView(panorama);
    map.addListener("click", (event) => {
        sv.getPanorama({ location: event.latLng, radius: 50 }, processSVData);
    });
}

function add() {
    json.list.push({ "lat": latLng.lat(), "lng": latLng.lng() });
    document.getElementById("coords").innerHTML = JSON.stringify(json);
}

function send() {
    json["name"] = document.getElementById('name').value;
    document.getElementById("coords").innerHTML = JSON.stringify(json);
    var xhr = new XMLHttpRequest();
    var url = "/confirm";
    xhr.open("POST", url);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(json));
}
