# Salary with dollar sign and separators

Read the `2019-stats-cleaner.csv` into a `df`. The CSV is in the state we left our previous exercise with columns `'Salary', 'Country', 'Sex', 'First name', 'Last name'`. As you can see below the `Salary` column is of object dtype. Let's make that numeric.

| # |Salary|
| - |------- |
| 0 | $90.000,00 |
| 1 | $27.500,00 |
| 2 | $105.900,00 |
| 3 | $22.750,00 |
| 4 | $320.200,00 |
| 5 | $53.988,00 |
| 6 | $99.800,00 |
| 7 | $48.630,00 |
| 8 | $475.800,00 |
| 9 | $150.380,00 |

Remove the `$`(dollar sign) and `.`(period) acting as the thousands separator. Then replace the `,`(comma) with a `.`(period)

Convert the `Salary` column to float dtype.

All of these changes should be permanently assigned to the `df` object.
