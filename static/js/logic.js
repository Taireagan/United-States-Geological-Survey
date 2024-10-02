// Creating initial map object:
// We set the longitude, latitude, and starting zoom level.
let myMap = L.map("map", {
    center: [39.8283, -98.5795],
    zoom: 5
  });

// Function to get color based on depth
function getColor(depth) {
    return depth > 90 ? "#ff5f65" :
           depth > 70 ? "#fca35d" :
           depth > 50 ? "#fdb72a" :
           depth > 30 ? "#f7db11" :
           depth > 10 ? "#9dff00" :
                        "#00ff00"; 
}


// Add a tile layer to our map (background map image)
// We use the addTo() method to add objects to our map.
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);

  let url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";


  d3.json(url).then(function(response) {

    // Store the array pf earthquake data from the API's GeoJSON. Each feature will represent an earthquake event
    let features = response.features;


    // Create a loop to iterate through every earthquake  in the feature array.
    features.forEach(function(feature) {
        let location = feature.geometry;
        if (location) {
            let coords = [location.coordinates[1], location.coordinates[0]];
            let depth = location.coordinates[2];
            let magnitude = feature.properties.mag;
            let place = feature.properties.place;
            let time = new Date(feature.properties.time);
                        
            let popupContent = `<strong>Location:</strong> ${place}<br>
                                <strong>Magnitude:</strong> ${magnitude}<br>
                                <strong>Depth:</strong> ${depth} km<br>
                                <strong>Time:</strong> ${time.toLocaleString()}`;
                        
            L.circle(coords, {
                fillOpacity: 0.75,
                color: "white",
                fillColor: getColor(depth), // Adjust color to depth of magnitude
                radius: magnitude * 20000 // Adjust radius to the magnitude
            }).bindPopup(popupContent).addTo(myMap);
        }
                
    });
            
    // Create a function to create the legned for the map
    function createLegend() {
        let legend = L.control({position: 'bottomright'});
            
        legend.onAdd = function () {
            let div = L.DomUtil.create('div', 'legend');
            let depthRanges = [
                { range: '-10-10', color: getColor(5) },
                { range: '10-30', color: getColor(20) },
                { range: '30-50', color: getColor(40) },
                { range: '50-70', color: getColor(60) },
                { range: '70-90', color: getColor(80) },
                { range: '90+', color: getColor(90) }
            ];
            
            div.innerHTML = '<h4>Legend</h4>';
            
            depthRanges.forEach(function(item) {
                div.innerHTML +=
                    '<i style="background:' + item.color + '"></i> ' +
                    item.range + '<br>';
            });
            
            return div;
        };
            
        legend.addTo(myMap);
    }
      
    // Create the legend
    createLegend();
});         


