# First name, last name DataFrame reshaping

We will be reading in the `2019-stats.csv` containing customer observations from a small online business in the Europe. The data is in a very odd format, pay attention to the character separating the features.

Read the CSV into a `df` DataFrame object.

Split the features into their own columns.

Split the column containing customer names into two columns `'Frist name', 'Last name'`. Remove the original column containing the joined first and last names.

The final state of the `df` should have the following columns,

['Salary', 'Country', 'Sex', 'First name', 'Last name']
