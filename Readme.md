
# Vulnerable Neighborhood Explorer (VNE)

<h2 align="center" style="margin-top:-10px">Vulnerable Neighborhood Explorer (VNE) is an open-source visual analytics tool for exploring social vulnerability across different neighborhoods</h2> 
<br\><br\>


VNE is a cyberGIS-based visual analytics tool that allows users to (1) delineate neighborhoods based on their selection of variables describing socioeconomic and demographic profiles and (2) explore which neighborhoods are susceptible to the impacts of disasters based on specific socioeconomic and demographic characteristics. [Firefox](https://www.mozilla.org/en-US/firefox/new/) or [Google Chrome](https://www.google.com/chrome/download) is the recommended web browser for reaping the best performance of VNE


## QuickStart

**Example visaulizations are available in the folders below:**<br/>
*	VNE_Chicago_kmeans_C5 <br/>
*	New_York_kmeans_C5<br/>
*	Phoenix_kmeans_C5<br/>
*	Miami_kmeans_C5<br/>
*	US_kmeans_C5<br/>
*	Chicago_extended_kmeans_C5<br/>
*	Illinois_kmeans_C5 <br/>

## Getting Started
**You can run VNE in your Jupyter Notebook installed on your PC as well as in CybearGISX. We recommend that you use CyberGISX because all the required packages have been integrated in CyberGISX.**<br/><br/>

**To use it in CyberGISX, follow steps below:**
1. If you do not have a CyerGISX account, create a CyberGISX account with your institution's email address or Google email address at  [https://cybergisxhub.cigi.illinois.edu](https://cybergisxhub.cigi.illinois.edu)
2. Once you log in CyberGISX, go to [https://cybergisxhub.cigi.illinois.edu/notebook/vulnerable-neighborhood-explorer](https://cybergisxhub.cigi.illinois.edu/notebook/vulnerable-neighborhood-explorer), and click the button "Open with CyberGISX".  Wait for 3 to 5 seconds. All related source codes will be automatically copied, and the main notebook will be opened. Then, click the “play button” at the top to run.

## Input parameter description
<ul> 
<li>‘title’: Texts will be placed at the top of the result visualization.</li>
<li>‘subject’: Texts will be placed at the top of the maps, column bar charts, and box plots.</li>
<li>‘inputCSV’: User’s CSV file normally containing socioeconomic, demographic, and health status.</li>
<li>‘shapefile’: A shapefile to visualize polygons on the map. The first column header must start with ‘geoid,’ and the code should match with the 'geoid' column of another input CSV file that you enter for inputCSV' and 'disasterInputCSV’.</li>
<li>‘disasterInputCSV’: User’s CSV file containing data representing the number of disaster-affected people. In the case of COVID-19, the file can contain the number of confirmed cases, COVID-19 testing cases, and deaths.</li>  
<li>‘rate1’: It can be used mostly for disease data. The purpose is to compute the percentage using two variables in ‘disasterInputCSV.’ For example, when the CSV file contains the columns such as ‘total_count’ (i.e., the number of confirmed cases of disease) and ‘total_test’ (i.e., the number of individuals being tested for the disease), you can pass 'Confirmed (%) =_count/_tested.' Then, confirmed cases (e.g., the number of confirmed cases/ the number of people who got COVID-19 testing *100) will be computed and shown as  ‘total_Confirmed (%)’ in the result visualization. As a next parameter, ‘rate2’ can also be used as 'rate2': 'Death (%) = _deaths/_cases' to compute and visualize the fatality rate (i.e., the number of deaths from disease/the number of infected individuals * 100).</li>
<li>‘normalizationCSV’: This parameter is for data normalization. The name of CSV file should be entered. The first column of CSV should contain column headers in ‘disasterInputCSV’, the second column should contain column headers in ‘inputCSV’. For example, if you enter ‘total_count’ in the first column and ‘Population’ in the second column of the same row, it will compute ‘total_count’/’Population’ multiplied by the value entered in the next parameter, ‘normalizationUnit’.</li>
<li>‘normalizationUnit’: The normalization unit that you need for the normalization above. For example, if you enter the value 10000 here and ‘total_count’/’Population’ to the above parameter, ’normalizationCSV’. It will compute ‘total_count’/’Population’ * 10000, and the result will be visualized as ‘total_count (/10K pop) on the first map, column bar charts, and box plots.</li>
<li>‘years’: ‘inputCSV’ must contain the year column, and the year should be entered.</li> 
<li>‘method’: Clustering algorithms are used to identify neighborhood types. It is required to enter one of the following clustering methods: ‘kmeans’, ‘ward’, ‘affinity_propagation’, ‘spectral’, ‘gaussian_mixture’, ‘hdbscan’,‘ward_spatial’, ‘spenc’, ‘skater’, ‘azp’, ‘max_p’. For detailed information about each of methods, see the ‘Neighborhood Clustering Methods’ in the ‘Analyze Module’ of the Geospatial Neighborhood Analysis Package (GEOSNAP) </li>
<li>‘nClusters’: The number of clusters </li>
<li>‘variables’: Select variables to be computed from ‘inputCSV’. Here is the full description of eighteen variables in Fig 1 in the manuscript.
    <ul>
        <li>Median monthly housing costs: Median monthly housing costs </li>
        <li>% below poverty: percentage of population in poverty </li>
        <li>% unemployed: percentage of unemployed population </li>
        <li>% with 4year college degree: percentage of populationwith at least a four-year college degree </li>
        <li>% manufacturing: percentage of manufacturing employees (by industries) </li>
        <li>% service industry: percentage of service employees (by industries) </li>
        <li>% structures more than 30 years old: percentage of structures built more than 30 years ago </li>
        <li>% households moved <10 years ago: percentage of household heads moved into unit less than 10 years ago </li>
        <li>% multiunit structures: percentage of housing units in multi-unit structures </li>
        <li>% owner occupied housing: percentage of owner-occupied housing units </li>
        <li>% vacant housing: percentage of vacant housing units </li>
        <li>% > 60 years old: percentage of population aged 60 years and over </li>
        <li>% < 18 years old: percentage of population aged 17 years and under </li>
        <li>% white: percentage of persons of white race, not Hispanic origin </li>
        <li>% Asian: percentage of persons of Asian race (and Pacific Islander) </li>
        <li>% Hispanic: percentage of persons of Hispanic origin </li>
        <li>% black	: percentage of persons of black race, not Hispanic origin </li>
        <li>% foreign: born percentage of foreign-born population </li>
    </ul> 
 </li>
 
<li>‘Distribution_of_Subject’: A1 in Fig1. Enter ‘True’ to display or ‘False’ not to display</li> 
<li>‘Zscore_Means_across_Clusters’: A in Fig2. Enter ‘True’ to display or ‘False’ not to display</li> 
<li>‘Zscore_Means_of_Each_Cluster’: B in Fig2. Enter ‘True’ to display or ‘False’ not to display</li> 
<li>‘Number_of_Barcharts_for_Subject_Clusters’: The number of bar charts shows up in section B of Fig1</li>
<li>‘Number_of_BoxPlots_for_Subject_Clusters’: The number of box plots shows up in section C of Fig1</li>
</ul> 

## A Case Study

Exploring Neighborhood-level Social Vulnerability to COVID-19 in Chicago. 

Two images (Fig 1 and 2) below show the result visualization of VNE, which allow users to explore socioeconomic and demographic disparity in COVID-19 outbreaks as well as vulnerable neighborhoods and their socioeconomic and demographic characteristics. Two input data were used: 
<ul>
<li>COVID-19 confirmed and test cases at the zip code level in Chicago. They were downloaded from the website of the Illinois Department of Public Health. The data used reflects the duration of the COVID-19 outbreak until July 11th, 2020, when the data was downloaded.</li> 

<li> American Community Survey (ACS) 5-year estimates from 2014 to 2018. From ACS. From ACS, 18 variables representing different socioeconomic and demographic statuses were collected.</li>
</ul>

 



 <p align="center">Fig 1. The first part of the visualization of VNE.
<img height=800 src="http://su-gis.iptime.org/VNE/images/Fig_S1.png" alt="CyberGIS_Vis.PNG"/>
</p>

 <p align="center">Fig 2. The second part of the visualization of VNE. 
<img height=600 src="http://su-gis.iptime.org/VNE/images/Fig_S2.png" alt="CyberGIS_Vis.PNG"/>
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

Su Yeon Han¹, Jeon-Young Kang², Fangzheng Lyu³, Furqan Baig³, Jinwoo Park³, Shaowen Wang³ 

¹ Geography and Environmental Studies, Texas State University, San Marcos, TX, USA
² Department of Geography, Kyung Hee University, South Korea
³ CyberGIS Center for Advanced Digital and Spatial Studies, University of Illinois at Urbana-Champaign, Urbana, IL, USA

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/cybergis/VNE/blob/master/LICENSE) file for details.

-------------

If you have questions, please contact Dr. Su Yeon Han at su.han@txstate.edu at Geography and Environmental Studies, Texas State University

