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

var departamentos = L.esri.dynamicMapLayer({
   url: "https://geocatminapp.ingemmet.gob.pe/arcgis/rest/services/SERV_CARTOGRAFIA_DEMARCACION_WGS84/MapServer",
   layers: ["0"]
});

var provincias = L.esri.dynamicMapLayer({
   url: "https://geocatminapp.ingemmet.gob.pe/arcgis/rest/services/SERV_CARTOGRAFIA_DEMARCACION_WGS84/MapServer",
   layers: ["1"]
});

var distritos = L.esri.dynamicMapLayer({
   url: "https://geocatminapp.ingemmet.gob.pe/arcgis/rest/services/SERV_CARTOGRAFIA_DEMARCACION_WGS84/MapServer",
   layers: ["2"]
});

//var raster_tdps = L.esri.dynamicMapLayer({
//   url: "https://tiles.arcgis.com/tiles/xyhOybaVXpstyizb/arcgis/rest/services/services_raster_tdps/MapServer",
//   layers: ["2"]
//});

var tdps_tmax = L.esri.tiledMapLayer({
    url: "https://tiles.arcgis.com/tiles/xyhOybaVXpstyizb/arcgis/rest/services/tdps_tmax/MapServer",
    opacity: 0.6,
    minZoom: 6,
    maxZoom: 13,
    detectRetina: false
});

tdps_tmax.bindPopup(function (error, rasterTiled) {
    console.log(rasterTiled);
    console.log(error)
});

var tdps_tmin = L.esri.tiledMapLayer({
    url: "https://tiles.arcgis.com/tiles/xyhOybaVXpstyizb/arcgis/rest/services/tdps_tmin/MapServer",
    opacity: 0.6,
    minZoom: 6,
    maxZoom: 13,
    detectRetina: false
});

tdps_tmin.bindPopup(function (error, featureCollection) {
    return 'ESTACION: '
});

var tdps_dem = L.esri.tiledMapLayer({
    url: "https://tiles.arcgis.com/tiles/xyhOybaVXpstyizb/arcgis/rest/services/tdps_dem/MapServer",
    opacity: 0.6,
    minZoom: 6,
    maxZoom: 13,
    detectRetina: false
});

var tdps_etp = L.esri.tiledMapLayer({
    url: "https://tiles.arcgis.com/tiles/xyhOybaVXpstyizb/arcgis/rest/services/tdps_etp/MapServer",
    opacity: 0.6,
    minZoom: 6,
    maxZoom: 13,
    detectRetina: false
});

var tdps_pp = L.esri.tiledMapLayer({
    url: "https://tiles.arcgis.com/tiles/xyhOybaVXpstyizb/arcgis/rest/services/tdps_pp/MapServer",
    opacity: 0.6,
    minZoom: 6,
    maxZoom: 13,
    detectRetina: false
});

var cuencas_tdps = L.esri.featureLayer({
   url: "https://services8.arcgis.com/xyhOybaVXpstyizb/arcgis/rest/services/gpo_cuencas_tdps/FeatureServer/0"
});

cuencas_tdps.bindPopup(function (layer) {
    return L.Util.template('<a href="../cuenca/{codigo}/"><strong>{nombre}</strong>.</a>', layer.feature.properties);
  });

var groupedOverLayers = {
  "Base": {
    "Departamentos": departamentos,
    "Provincias": provincias,
    "Distritos": distritos
  },
  "Data": {
    "Temp. Máxima": tdps_tmax,
    "Temp. Mínima": tdps_tmin,
    "DEM": tdps_dem,
    "ETP": tdps_etp,
    "Precipitación": tdps_pp
  },
  "Cuencas": {
    "Cuencas TDPS": cuencas_tdps
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

//L.control.scale({
//  imperial: false
//}).addTo(map);

////////////////////////////////////

});
