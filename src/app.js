var UI = require('ui');
var Vector2 = require('vector2');
var ajax = require('ajax');

function getLoc() {
  function locationSuccess(pos) {
    lat = pos.coords.latitude;
    long = pos.coords.longitude;
    console.log('lat= ' + lat + ' lon= ' + long);
  }
  function locationError(err) {
    console.log('location error (' + err.code + '): ' + err.message);
  }
  navigator.geolocation.getCurrentPosition(locationSuccess, locationError, {maximumAge: 600000, timeout: 5000});
}

function getBus() {
  ajax(
    {
      url: 'https://wtftu1.herokuapp.com',
      type: 'json'
    },
    function(data) {
      if(lat < 52.33 && lat > 52.23 & long < -1.50 && long > -1.60) { 
        card.subtitle('Parade: ' + data.info.toUni + '\n2nd: ' + data.info.toUni2); // in Leam
        card.body('But they probably won\'t turn up');
      } else if(lat < 52.40 && lat > 52.37 & long < -1.54 && long > -1.68) { 
        card.subtitle('AL3: ' + data.info.toLeam + '\n2nd: ' + data.info.toLeam2); // at Uni
        card.body('But they probably won\'t turn up');
      } else {
        card.subtitle('Where the frack are you?');
        card.body('What were you expecting?');
      }
    },  
    function(error) {
      console.log('Failed fetching bus data: ' + error);
    }
  );
}

// SPLASH SCREEN
var splash = new UI.Window({ fullscreen: true });
var image = new UI.Image ({
  position: new Vector2(0, 0),
  size: new Vector2(144, 168),
  image: 'images/splash.png'
});
splash.add(image);
splash.show();

// GET LOCATION
getLoc();

// MAKE MAIN SCREEN
var card = new UI.Card({
  title:'WTFTU1',
  subtitle:'Summoning...'
});

// SHOW MAIN SCREEN
setTimeout(function() {
  card.show();
  splash.hide();
}, 2000);

// GET TIMETABLE DATA
getBus();

// SEE THE SPLASH ANYTIME!
card.on('click', 'select', function() {
  splash.show();
});

// UPDATE BY THE MINUTE
function update() {
  setTimeout(function() {
    getBus();
    update();
  }, 60000);
}
update();