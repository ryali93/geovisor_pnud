<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" version="1.0.0" xmlns:gml="http://www.opengis.net/gml">
  <UserLayer>
    <sld:LayerFeatureConstraints>
      <sld:FeatureTypeConstraint/>
    </sld:LayerFeatureConstraints>
    <sld:UserStyle>
      <sld:Name>pp_anual_utm19s</sld:Name>
      <sld:FeatureTypeStyle>
        <sld:Rule>
          <sld:RasterSymbolizer>
            <sld:ChannelSelection>
              <sld:GrayChannel>
                <sld:SourceChannelName>1</sld:SourceChannelName>
              </sld:GrayChannel>
            </sld:ChannelSelection>
            <sld:ColorMap type="ramp">
              <sld:ColorMapEntry color="#31007e" label="355.806365966797" quantity="355.806365966797"/>
              <sld:ColorMapEntry color="#17d78b" label="528.24991607666" quantity="528.24991607666"/>
              <sld:ColorMapEntry color="#9fff00" label="700.693466186523" quantity="700.693466186523"/>
              <sld:ColorMapEntry color="#ff0000" label="873.137016296387" quantity="873.1370162963869"/>
              <sld:ColorMapEntry color="#ffd7eb" label="1045.58056640625" quantity="1045.58056640625"/>
            </sld:ColorMap>
          </sld:RasterSymbolizer>
        </sld:Rule>
      </sld:FeatureTypeStyle>
    </sld:UserStyle>
  </UserLayer>
</StyledLayerDescriptor>
