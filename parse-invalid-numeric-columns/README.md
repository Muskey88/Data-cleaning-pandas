# Parse invalid numeric columns

We are going to be working some property data, have a look at `property-data.csv` to get an understanding of what we are working with.

Read the property CSV into a `df` object.

Cast the following columns to numeric type `BEDROOMS`, `BATHROOMS` and `SQUARE_FEET`.

Finally, return `df` and rows containing `NaN` values permanently dropped.
