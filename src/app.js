var UI = require('ui');
var Vector2 = require('vector2');
var ajax = require('ajax');
var Light = require('ui/light');

// SPLASH SCREEN
var splash = new UI.Window({ fullscreen: true });
var image = new UI.Image ({
  position: new Vector2(0, 0),
  size: new Vector2(144, 168),
  image: 'images/splash.png'
});
splash.add(image);
splash.show();
Light.on();

// GET LOCATION
var lat;
var long;
function locationSuccess(pos) {
  lat = pos.coords.latitude;
  long = pos.coords.longitude;
  console.log('lat= ' + lat + ' lon= ' + long);
}
function locationError(err) {
  console.log('location error (' + err.code + '): ' + err.message);
}
navigator.geolocation.getCurrentPosition(locationSuccess, locationError, {maximumAge: 600000, timeout: 5000});

var card = new UI.Card({
  title:'WTFTU1',
  subtitle:'Summoning...'
});

// MAIN SCREEN
setTimeout(function() {
  Light.auto();
  card.show();
  splash.hide(); // Hide the splash screen to avoid showing it when the user press Back.
}, 3000);

// GET TIMETABLE DATA
ajax(
  {
    url: 'https://wtftu1.herokuapp.com',
    type: 'json'
  },
  function(data) {
    if(lat < 52.33 && lat > 52.23 & long < -1.50 && long > -1.60) { 
      card.subtitle('To Uni: ' + data.info.toUni); // in Leam
      card.body('But it probably won\'t turn up');
    } else if(lat < 52.40 && lat > 52.37 & long < -1.54 && long > -1.68) { 
      card.subtitle('To Leam: ' + data.info.toLeam); // at Uni
      card.body('But it probably won\'t turn up');
    } else {
      card.subtitle('Where the frack are you?');
      card.body('What were you expecting?');
    }
  },  
  function(error) {
    console.log('Failed fetching weather data: ' + error);
  }
);