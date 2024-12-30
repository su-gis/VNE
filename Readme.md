
# Vulnerable Neighborhood Explorer (VNE)

<h3 align="center" style="margin-top:-10px">Vulnerable Neighborhood Explorer (VNE) is an open-source visual analytics tool for exploring social vulnerability across different neighborhoods</h3> 



VNE is a cyberGIS-based visual analytics tool that allows users to (1) delineate neighborhoods based on their selection of variables describing socioeconomic and demographic profiles and (2) explore which neighborhoods are susceptible to the impacts of disasters based on specific socioeconomic and demographic characteristics. [Firefox](https://www.mozilla.org/en-US/firefox/new/) or [Google Chrome](https://www.google.com/chrome/download) is the recommended web browser for reaping the best performance of VNE.

## Getting Started
**You can run VNE in your Jupyter Notebook/Lab installed on your PC as well as in CybearGISX. We recommend that you use CyberGISX because all the required packages have been integrated in CyberGISX.**<br/><br/>

**To use it in CyberGISX, follow steps below:**
1. If you do not have a CyerGISX account, create a CyberGISX account with your institution's email address or Google email address at  [https://cybergisxhub.cigi.illinois.edu](https://cybergisxhub.cigi.illinois.edu)
2. Once you log in CyberGISX, go to [https://cybergisxhub.cigi.illinois.edu/notebook/vulnerable-neighborhood-explorer](https://cybergisxhub.cigi.illinois.edu/notebook/vulnerable-neighborhood-explorer), and click the button "Open with CyberGISX".  Wait for 3 to 5 seconds. All related source codes will be automatically copied, and the main notebook will be opened. Then, click the “play button” at the top to run.

**A video tutorial on using VNE in CyberGISX**

https://github.com/user-attachments/assets/ecac065e-9e07-4622-b243-ecd0bb946d66




## Input parameter description
<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th><b>Parameter</b></th>
      <th><b>Description</b></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>‘title’</b></td>
      <td>Enter a descriptive title for the visualization. Texts will be placed at the top of the result visualization.</td>
    </tr>
    <tr>
      <td><b>‘subject’</b></td>
      <td>Specify the subject matter (e.g., COVID-19). Texts will be placed at the top of the maps, column bar charts, and box plots.</td>
    </tr>
    <tr>
      <td><b>‘inputCSV’</b></td>
      <td>Provide the path to your input CSV file. The file should include socioeconomic, demographic, and health status data. Ensure that the first column is labeled <code>geoid</code> and the second column is labeled <code>year</code>. All subsequent columns will be available for selection in the Variables input box below.</td>
    </tr>
    <tr>
      <td><b>‘shapefile’</b></td>
      <td>Enter the path to the shapefile. A shapefile is used to visualize polygons on the map. The first column header must start with <code>geoid</code>, and the code should match the <code>geoid</code> column of another input CSV file that you enter for <code>inputCSV</code> and <code>disasterInputCSV</code>.</td>
    </tr>
    <tr>
      <td><b>‘disasterInputCSV’</b></td>
      <td>Enter the path to your input CSV file containing data representing the number of disaster-affected people. In the case of COVID-19, the file can contain the number of confirmed cases, COVID-19 testing cases, and deaths. Ensure that the first column is labeled <code>geoid</code>.</td>
    </tr>
    <tr>
      <td><b>‘rate1’</b></td>
      <td>Primarily used for disease data. Computes the percentage using two variables in <code>disasterInputCSV</code>. For example, if the CSV file contains columns like <code>total_count</code> (number of confirmed cases) and <code>total_test</code> (number of individuals tested), you can define <code>Confirmed (%) = total_count / total_test * 100</code>. This will compute and display <code>total_Confirmed (%)</code> in the result visualization. Similarly, <code>rate2</code> can be used as <code>Death (%) = total_deaths / total_cases * 100</code> to compute and visualize the fatality rate.</td>
    </tr>
    <tr>
      <td><b>‘normalizationCSV’</b></td>
      <td>Enter the path to your input CSV file. The first column should contain column headers from <code>disasterInputCSV</code>, and the second column should contain column headers from <code>inputCSV</code>. For example, entering <code>total_count</code> in the first column and <code>Population</code> in the second column will compute <code>total_count / Population * normalizationUnit</code>.</td>
    </tr>
    <tr>
      <td><b>‘normalizationUnit’</b></td>
      <td>Set the normalization value (e.g., 10,000). For instance, if you set this to 10,000 and use <code>total_count / Population</code> from <code>normalizationCSV</code>, it will compute <code>total_count / Population * 10,000</code>. The result will be visualized as <code>total_count (/10K pop)</code> on the first map, column bar charts, and box plots.</td>
    </tr>
    <tr>
      <td><b>‘years’</b></td>
      <td>List the years for the analysis. This value should match the second column of the input CSV. It will be displayed at the top of the neighborhood map.</td>
    </tr>
    <tr>
      <td><b>‘method’</b></td>
      <td>Clustering algorithms used to identify neighborhood types. Enter one of the following methods: <code>kmeans</code>, <code>ward</code>, <code>affinity_propagation</code>, <code>spectral</code>, <code>gaussian_mixture</code>. For detailed information about each method, refer to the <i>Neighborhood Clustering Methods</i> section in the <i>Analyze Module</i> of the Geospatial Neighborhood Analysis Package (GEOSNAP).</td>
    </tr>
    <tr>
      <td><b>‘nClusters’</b></td>
      <td>Specify the number of clusters.</td>
    </tr>
    <tr>
      <td><b>‘variables’</b></td>
      <td>Select variables to be computed from <code>inputCSV</code>. Below is the full description of eighteen variables used in the example:</td>
    </tr>
    <tr>
      <td colspan="2">
        <ul>
          <li><b>Median monthly housing costs:</b> Median monthly housing costs.</li>
          <li><b>% below poverty:</b> Percentage of the population in poverty.</li>
          <li><b>% unemployed:</b> Percentage of the unemployed population.</li>
          <li><b>% with 4-year college degree:</b> Percentage of the population with at least a four-year college degree.</li>
          <li><b>% manufacturing:</b> Percentage of manufacturing employees (by industries).</li>
          <li><b>% service industry:</b> Percentage of service employees (by industries).</li>
          <li><b>% structures more than 30 years old:</b> Percentage of structures built more than 30 years ago.</li>
          <li><b>% households moved <10 years ago:</b> Percentage of household heads who moved into the unit less than 10 years ago.</li>
          <li><b>% multiunit structures:</b> Percentage of housing units in multi-unit structures.</li>
          <li><b>% owner-occupied housing:</b> Percentage of owner-occupied housing units.</li>
          <li><b>% vacant housing:</b> Percentage of vacant housing units.</li>
          <li><b>% > 60 years old:</b> Percentage of the population aged 60 years and over.</li>
          <li><b>% < 18 years old:</b> Percentage of the population aged 17 years and under.</li>
          <li><b>% white:</b> Percentage of persons of white race, not Hispanic origin.</li>
          <li><b>% Asian:</b> Percentage of persons of Asian race (and Pacific Islander).</li>
          <li><b>% Hispanic:</b> Percentage of persons of Hispanic origin.</li>
          <li><b>% black:</b> Percentage of persons of black race, not Hispanic origin.</li>
          <li><b>% foreign:</b> Percentage of the foreign-born population.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>‘Distribution_of_Subject’</b></td>
      <td>A1 in Fig1. Enter <code>True</code> to display or <code>False</code> not to display.</td>
    </tr>
    <tr>
      <td><b>‘Zscore_Means_across_Clusters’</b></td>
      <td>A in Fig2. Enter <code>True</code> to display or <code>False</code> not to display.</td>
    </tr>
    <tr>
      <td><b>‘Zscore_Means_of_Each_Cluster’</b></td>
      <td>B in Fig2. Enter <code>True</code> to display or <code>False</code> not to display.</td>
    </tr>
    <tr>
      <td><b>‘Number_of_Column_Charts_for_Subject_Clusters’</b></td>
      <td>The number of column bar charts displayed in Fig1.</td>
    </tr>
    <tr>
      <td><b>‘Number_of_BoxPlots_for_Subject_Clusters’</b></td>
      <td>The number of box plots displayed in Fig1.</td>
    </tr>
  </tbody>
</table>

## Example Result Visualization

**Example visaulizations are available in the folders below:**<br/>
*	VNE_Chicago<br/>
*	VNE_Chicago2<br/>
*	VNE_Chicago_kmeans_C5 <br/>
*	VNE_Chicago_kmeans_C5 <br/>
*	New_York_kmeans_C5<br/>
*	Phoenix_kmeans_C5<br/>
*	Miami_kmeans_C5<br/>
*	US_kmeans_C5<br/>
*	Chicago_extended_kmeans_C5<br/>
*	Illinois_kmeans_C5 <br/>

## A Case Study

Exploring Neighborhood-level Social Vulnerability to COVID-19 in Chicago. 

Two images (Fig 1 and 2) below show the result visualization of VNE, which allow users to explore socioeconomic and demographic disparity in COVID-19 outbreaks as well as vulnerable neighborhoods and their socioeconomic and demographic characteristics. Two input data were used: 
<ul>
<li>COVID-19 confirmed and test cases at the zip code level in Chicago. They were downloaded from the website of the Illinois Department of Public Health. The data used reflects the duration of the COVID-19 outbreak until July 11th, 2020, when the data was downloaded.</li> 

<li> American Community Survey (ACS) 5-year estimates from 2014 to 2018. From ACS, 18 variables representing different socioeconomic and demographic statuses were collected.</li>
</ul>

 <p align="center">Fig 1. The first part of the visualization of VNE.
<img height=800 src="https://su-gis.org/VNE/images/Fig_S1.png" alt="CyberGIS_Vis.PNG"/>
</p>

 <p align="center">Fig 2. The second part of the visualization of VNE. 
<img height=600 src="https://su-gis.org/VNE/images/Fig_S2.png" alt="CyberGIS_Vis.PNG"/>
</p>

 
## Data
* [American Community Survey (ACS) 5-year estimates from 2014 to 2018](https://www.census.gov/data/developers/data-sets/acs-5year.2018.html#list-tab-Z8NDSX202E05P3SE5O)
* [COVID-19 Zip Level Tests and Cases](https://dph.illinois.gov/covid19/data/data-portal/zip-level-tests-and-cases.html)
## Related Resources
* [CyberGISX](https://cybergisxhub.cigi.illinois.edu/) 
* [Leaflet](https://leafletjs.com) 
* [PlotlyJS](https://plot.ly/javascript/) 
* [D3](https://d3js.org/) 
* [GEOSNAP](https://github.com/spatialucr/geosnap) 

## Contributors

Su Yeon Han<sup>1</sup>, Joon-Seok Kim<sup>2</sup>, Jooyoung Yoo<sup>3</sup>, Jeon-Young Kang<sup>4</sup>, Alexander Michels<sup>5</sup>, Fangzheng Lyu<sup>5</sup>, Furqan Baig<sup>5</sup>, Jinwoo Park<sup>5</sup>, Shaowen Wang<sup>5</sup>

<sup>1</sup> Geography and Environmental Studies, Texas State University, San Marcos, TX, USA  
<sup>2</sup>Spatial Sciences Institute, University of Southern California  
<sup>3</sup> Computer Science, Emory University  
<sup>4</sup> Department of Geography, Kyung Hee University, South Korea  
<sup>5</sup>CyberGIS Center for Advanced Digital and Spatial Studies, University of Illinois at Urbana-Champaign, Urbana, IL, USA  

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/cybergis/VNE/blob/master/LICENSE) file for details.

-------------

If you have questions, please contact Dr. Su Yeon Han at su.han@txstate.edu at Geography and Environmental Studies, Texas State University

