

getFeatureInfo: function (evt) {
    var url = this.getFeatureInfoUrl(evt.latlng);
    const Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();
    var data = Http.onreadystatechange = (e) => {
      console.log(JSON.parse(Http.responseText))
    };
    return data;
},

getFeatureInfoUrl: function (latlng) {
    var point = this._map.latLngToContainerPoint(latlng, this._map.getZoom()),
    size = this._map.getSize(),

    params = {
      request: 'GetFeatureInfo',
      service: 'WMS',
      srs: 'EPSG:4326',
      styles: this.wmsParams.styles,
      transparent: this.wmsParams.transparent,
      version: this.wmsParams.version,
      format: this.wmsParams.format,
      bbox: this._map.getBounds().toBBoxString(),
      height: size.y,
      width: size.x,
      layers: this.wmsParams.layers,
      query_layers: this.wmsParams.layers,
      info_format: 'application/json'
    };

    params[params.version === '1.3.0' ? 'i' : 'x'] = point.x;
    params[params.version === '1.3.0' ? 'j' : 'y'] = point.y;

    var url = this._url + L.Util.getParamString(params, this._url, true);
    if(typeof this.wmsParams.proxy !== "undefined") {
        // check if proxyParamName is defined (instead, use default value)
        if(typeof this.wmsParams.proxyParamName !== "undefined")
            this.wmsParams.proxyParamName = 'url';
        // build proxy (es: "proxy.php?url=" )
        _proxy = this.wmsParams.proxy + '?' + this.wmsParams.proxyParamName + '=';
        url = _proxy + encodeURIComponent(url);
    }
    return url;
},