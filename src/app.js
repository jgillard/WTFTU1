// Using Tutorial 1 content (Cards)

var UI = require('ui');
var ajax = require('ajax');

// Create a Card with title and subtitle
var card = new UI.Card({
  title:'WTFTU1',
  subtitle:'Summoning...'
});

// Display the Card
card.show();

// Make the request
ajax(
  {
    url: 'https://wtftu1.herokuapp.com'
  },
  function(data) {
    // Show to user
    card.subtitle(data);
    var body;
    if (data.length == 4) {
      body = 'But it probably won\'t turn up';
    } else {
      body = 'What were you expecting?';
    }
    card.body(body);
  },  
  function(error) {
    // Failure!
    console.log('Failed fetching weather data: ' + error);
  }
);