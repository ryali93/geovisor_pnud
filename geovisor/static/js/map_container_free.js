window.addEventListener("map:init", function (event) {
var map = event.detail.map.setView( [-15, -75], 4);

//Download GeoJSON data with Ajax
var estaciones = L.tileLayer.wms("http://localhost:8080/geoserver/climatic-data/wms", {
  layers: "climatic-data:opendata_historic",
  iconUrl: 'img/red.png',
  format: 'image/png',
  transparent: true
});

estaciones.bindPopup(function (error, featureCollection) {
   if (error || featureCollection.features.length === 0) {
     return false;
   } else {
     return 'ESTACION: ' + featureCollection.features[0].properties.NOM;
   }
});

var departamentos = L.tileLayer.wms("http://localhost:8080/geoserver/bd/wms", {
   layers: "bd:gpo_departamentos",
   format: 'image/png',
   transparent: true
});

var departamentos_2 = L.esri.dynamicMapLayer({
   url: "https://geocatminapp.ingemmet.gob.pe/arcgis/rest/services/SERV_CARTOGRAFIA_DEMARCACION_WGS84/MapServer",
   layers: ["0"]
});

var provincias = L.tileLayer.wms("http://localhost:8080/geoserver/bd/wms", {
   layers: "bd:gpo_provincias",
   format: 'image/png',
   transparent: true
});

var gpo_puno = L.tileLayer.wms("http://localhost:8080/geoserver/bd/wms", {
   layers: "bd:gpo_dep_puno",
   format: 'image/png',
   transparent: true
});

var estaciones_colombia = L.esri.dynamicMapLayer({
   url: "http://dhime.ideam.gov.co/arcgis/rest/services/CNE/EstacionesQ_edit/MapServer",
   useCors: false
});


var imerg_7day = L.esri.dynamicMapLayer({
   url: "https://gis1.servirglobal.net/arcgis/rest/services/Global/IMERG_Accumulations/MapServer",
   layers: [3]
});

var zonavida = L.tileLayer.wms("http://idesep.senamhi.gob.pe/geoserver/g_05_06/wms", {
   layers: "05_06_001_03_001_521_0000_00_00",
   format: 'image/png',
   transparent: true
});

var zonavida_2 = L.esri.dynamicMapLayer({
   url: "http://idesep.senamhi.gob.pe/geoserver/g_05_06/wms",
   layers: ["05_06_001_03_001_521_0000_00_00"]
});




zonavida_2.bindPopup(function (error, featureCollection) {
    if (error || featureCollection.features.length === 0) {
      console.log(error);
      console.log(featureCollection);
      return false;
    } else {
      console.log(featureCollection);
      return 'Risk Level: ' + featureCollection.features[0].properties["Pixel Value"];
    }
});

var groupedOverLayers = {
  "Base": {
    "Estaciones Colombia": estaciones_colombia,
    "Departamentos": departamentos,
    "Departamentos_2": departamentos_2,
    "Provincias": provincias,
    "Puno": gpo_puno
  },
  "Data": {
    "imerg_7day": imerg_7day,
    "Zona de Vida": zonavida
  }
};

L.control.groupedLayers(null, groupedOverLayers, {
    collapsed: false,
    position: 'topleft'
}).addTo(map);
//L.control.layers(overlayMaps).addTo(map);


/////////////////////////////////////
//
//var url = 'http://localhost:8080/geoserver/climatic-data/wms';
//var dep = L.tileLayer.betterWms(url, {
//    layers: 'climatic-data:departamentos',
//    transparent: true,
//    format: 'image/png'
//}).addTo(map);

////////////////////////////////////


L.control.scale({
  imperial: false
}).addTo(map);



});
