const tilesProvider = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

let myMap = L.map('myMap').setView([-34.884116, -57.898350], 12)

L.tileLayer(tilesProvider,	{ maxZoom: 18 }).addTo(myMap)

let marker = L.marker([-34.884116, -57.898350]).addTo(myMap);

marker.bindPopup("<b>Orquesta Escuela Berisso(Esc 7)</b>").openPopup();

let marker2 = L.marker([-34.876053, -57.892904]).addTo(myMap);

marker2.bindPopup("<b>Orquesta Escuela Berisso(Esc 6)</b>").openPopup();

let marker3 = L.marker([-34.876361, -57.855907]).addTo(myMap);

marker3.bindPopup("<b>Orquesta Escuela Berisso(Esc 22)</b>").openPopup();

let marker4 = L.marker([-34.880483, -57.869852]).addTo(myMap);

marker4.bindPopup("<b>Orquesta Escuela Berisso(Esc 17)</b>").openPopup();

navigator.geolocation.getCurrentPosition(
  (pos) => {
    const { coords } = pos
    const { latitude, longitude } = coords
    L.marker([latitude, longitude]).addTo(myMap).bindPopup("<b>Mi ubicacion actual</b>").openPopup()

    setTimeout(() => {
      myMap.panTo(new L.LatLng(latitude, longitude))
    }, 5000)
  },
  (error) => {
    console.log(error)
  },
  {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  })
