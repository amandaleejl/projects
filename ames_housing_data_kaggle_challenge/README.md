# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) 

# Project 2: Ames Housing Project

### Context and Problem Statement

To predict the price of houses at sale in Iowa by understanding the correlations between variables and thus creating a regression model. Through this we can identify and determine the various features that contributes to the value of the house.

---

## Executive Summary

This Jupyter notebook walks through the clean up of the train dataset, explores various sample statistics, trends and correlations. It includes creating a regression model based on the Ames Housing Dataset, to predict the prices of houses at sale. The success of the model will be evaluated by scores obtained.

This is important to investigate as it serves as a way for potential house buyers and owners to have a gauge on the housing of prices, to help with their decision making.

### Contents:
- [Data Dictionary](#Data-Dictonary)
- [Data Import & Cleaning](#Data-Import-and-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Preprocessing and Modeling](#Preprocessing-and-Modeling)
- [Evaluation and Conceptual Understanding](#Evaluation-and-Conceptual-Understanding)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)
---

### Data Dictionary

|Feature|Description|Type|
|---|---|---|
|MS SubClass|Identifies the type of dwelling involved in the sale.|int64|
|MS Zoning|Identifies the general zoning classification of the sale.|object|
|Lot Frontage|Linear feet of street connected to property.|float64|
|Lot Area|Lot size in square feet.|int64|
|Street|Type of road access to property.|object|
|Alley|Type of alley access to property.|object|
|Lot Shape|General shape of property.|object|
|Land Contour|Flatness of the property.|object|
|Utilities|Type of utilities available.|object|
|Lot Config|Lot configuration.|object|
|Land Slope|Slope of the property.|object|
|Neighborhood|Physical locations within Ames city limits (map available).|object|
|Condition 1|Proximity to various conditions|object|
|Condition 2|Proximity to various conditions (if more than one is present)|object|
|Bldg Type|Type of dwelling|object|
|House Style|Style of dwelling|object|
|Overall Qual|Rates the overall material and finish of the house|int64|
|Overall Cond|Rates the overall condition of the house|int64|
|Year Built|Original construction date|int64|
|Year Remod/Add|Remodel date (same as construction date if no remodeling or additions)|int64|
|Roof Style|Type of roof|object|
|Roof Matl|Roof Material|object|
|Exterior 1|Exterior covering on house|object|
|Exterior 2|Exterior covering on house (if more than one material)|object|
|Mas Vnr Type|Masonry veneer type|object|
|Mas Vnr Area|Masonry veneer area in square feet|float64|
|Exter Qual|Evaluats the quality of the material on the exterior|object|
|Exter Cond|Evaluates the present condition of the material on the exterior|object|
|Fondation|Type of foundation|object|
|Bsmt Qual|Evaluates the height of the basement|object|
|Bsmt Cond|Evaluates the general condition of the basement|object|
|Bsmt Exposure|Refers to walkout or garden level walls|object|
|BsmtFin Type 1|Rating of basement finished area|object|
|BsmtFin SF 1|Type 1 finished square feet|float64|
|BsmtFin Type 2|Rating of basement finished area (if multiple types)|object|
|BsmtFin SF 2|Type 2 finished square feet|float64|
|Bsmt Unf SF|Unfinished square feet of basement area|float64|
|Total Bsmt SF|Total square feet of basement area|float64|
|Heating|Type of heating|object|
|HeatingQC|Heating quality and condition|object|
|Central Air|Central air conditioning|object|
|Electrical|Electrical system|object|
|1st Flr SF|First Floor square feet|int64|
|2nd Flr SF|Second floor square feet|int64|
|Low Qual Fin SF (Continuous)|Low quality finished square feet (all floors)|int64|
|Gr Liv Area (Continuous)|Above grade (ground) living area square feet|int64|
|Bsmt Full Bath|Basement full bathrooms|float64|
|Bsmt Half Bath|Basement half bathrooms|float64|
|Full Bath|Full bathrooms above grade|int64|
|Half Bath|Half baths above grade|int64|
|Bedroom|Bedrooms above grade (does NOT include basement bedrooms)|int64|
|Kitchen|Kitchens above grade|int64|
|KitchenQual|Kitchen quality|object|
|TotRmsAbvGrd|Total rooms above grade (does not include bathrooms)|int64|
|Functional|Home functionality (Assume typical unless deductions are warranted)|object|
|Fireplaces|Number of fireplaces|int64|
|FireplaceQu|Fireplace quality|object|
|Garage Type|Garage location|object|
|Garage Yr Blt|Year garage was built|float64|
|Garage Finish|Interior finish of the garage|object|
|Garage Cars|Size of garage in car capacity|float64|
|Garage Area|Size of garage in square feet|float64|
|Garage Qual|Garage quality|onject|
|Garage Cond|Garage condition|object|
|Paved Drive|Paved driveway|object|
|Wood Deck SF|Wood deck area in square feet|int64|
|Open Porch SF|Open porch area in square feet|int64|
|Enclosed Porch| Enclosed porch area in square feet|int64|
|3Ssn Porch|Three season porch area in square feet|int64|
|Screen Porch| Screen porch area in square feet|int64|
|Pool Area|Pool area in square feet|int64|
|Pool QC|Pool quality|object|
|Fence|Fence quality|object|
|Misc Feature| Miscellaneous feature not covered in other categories|object|
|Misc Val|$Value of miscellaneous feature|int64|
|Mo Sold| Month Sold (MM)|int64|int64|
|Yr Sold|Year Sold (YYYY)|int64|
|Sale Type|Type of sale|object|
|SalePrice|Sale price|int64|

---

### Conclusions and Recommendations:

In the eventual modelling process, Lasso was chosen to fit the model as it provided for the best R2 score. The features that appear to add the most value to a home is if it belongs to a certain neighborhood, number of bathrooms, the type of exterior covering the house and the overall quality of the house. If the house were to belong to the neighborhood Crawford, it seems to add the most value to a home.

However, if the house is located in Meadow Village, the value of the house would be greated affected negatively. From closer research by looking at the Map of Ames, it seems that Meadow Village has quite vast open spaces that do not contain many houses in that area. Thus, it could be a reason as to why the value of the house would be affected negatively if located there.

Homeowners could change the exterior material of the house to Brick Face, have more bathrooms and also upkeep with the maintence and overall quality of material and finish of the house, so as to strive for a better value of their homes.

Some of the other neighborhoods that also seem like good investments include Somerset and Northridge Heights. Homeowners can consider looking to invest in houses in those areas as they tend to contribute to a higher sale price. Potential homeowners looking to purchase will be able to know a rough gauge of the higher price neighborhoods are and which area would be more suited to their price range.

I believe that the overall model is quite specific to Iowa. Taking Singapore for an example, the way houses are built here are very different without the luxury of vast space areas and pools. Thus, if we were to apply the model to elsewhere, it would require a different set of data that would be applicable to that housing area. 

A suggestion for improvement of the model would be to gather more data such as the accessibility to transportation and perhaps how safe the neighborhood is, which can be determine by crime rates. By gathering more data and fine tuning to the specific area, I believe will help make the model more universal.

---

### Sources:

- [City Map of Ames ](https://beacon.schneidercorp.com/Application.aspx?AppID=165&LayerID=2145&PageTypeID=1&PageID=1110)



