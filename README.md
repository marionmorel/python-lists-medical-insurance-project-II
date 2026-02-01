# Working with Python Lists: Medical Insurance Costs Project
## Data Scientist: Analytics - Codecademy

You are a doctor sorting through medical insurance cost data for some patients.

Using your knowledge of Python lists, you will store medical data and see what valuable insights you can gain from that data.

Let’s get started!

### Tasks

#### Exploring List Data

1. First, take a look at the two lists in <code>script.py</code>.

The list <code>names</code> stores the names of ten individuals, and <code>insurance_costs</code> stores their medical insurance costs.

Let’s add additional data to these lists:

* Append a new individual, <code>"Priscilla"</code>, to names.
* Append her insurance cost, <code>8320.0</code>, to <code>insurance_costs</code>.

2. Currently, the <code>names</code> and <code>insurance_costs</code> lists are separate, but we want each insurance cost to be paired with a name.

Create a new variable called <code>medical_records</code> that combines <code>insurance_costs</code> and <code>names</code> into a list using the <code>zip()</code> function.

The list should have the following structure:

```
[(cost_0, name_0), (cost_1, name_1), (cost_2, name_2), ...]
```

3. Print out <code>medical_records</code> in the terminal, and make sure the output is what you expected.

4. Let’s explore our medical data.

We want to see how many medical records we’re dealing with. Create a variable called <code>num_medical_records</code> that stores the length of <code>medical_records</code>.

5. Print <code>num_medical_records</code> with the following message:

```
There are {number of medical records} medical records. 
```

#### Selecting List Elements
 
6. Select the first medical record in <code>medical_records</code>, and save it to a variable called <code>first_medical_record</code>.

7. Print <code>first_medical_record</code> with the following message:

```
Here is the first medical record: {first medical record}
```

#### Sorting Lists

8. Sort <code>medical_records</code> so that the individuals with the lowest insurance costs appear at the start of the list.

Print the sorted <code>medical_records</code> with the following message:

```
Here are the medical records sorted by insurance cost: {sorted list}
```

#### Slicing Lists

9. Let’s look at the three cheapest insurance costs in our medical records.

Slice the <code>medical_records</code> list, and store the three cheapest insurance costs in a list called <code>cheapest_three</code>.

10. Print <code>cheapest_three</code> with the following message:

```
Here are the three cheapest insurance costs in our medical records: {cheapest three}
``` 

11. Let’s look at the three most expensive insurance costs in our medical records.

Slice the <code>medical_records</code> list, and store the three most expensive insurance costs in a list called <code>priciest_three</code>.

12. Print priciest_three with the following message:

```
Here are the three most expensive insurance costs in our medical records: {priciest three}
```

#### Counting Elements in a List

13. Some individuals in our medical records have the same name. For example, the name “Paul” shows up twice.

Count the number of occurrences of “Paul” in the <code>names</code> list, and store the result in a variable called <code>occurrences_paul</code>.

Print occurrences_paul with the following message:

```
There are {occurrences Paul} individuals with the name Paul in our medical records. 
```

#### Extra

14. Great job! In this project, you worked with Python lists to store medical insurance cost data and then gained meaningful insight into that data.

You now have a better understanding of how to interact with data in lists – an important skill for a data scientist to have.

Our dataset in this project was pretty small – we only dealt with 11 medical records. However, as you progress in your data science journey, you will encounter larger and more complex datasets. You are now better prepared to work with data in lists moving forward.

If you’d like additional practice on lists, here are some ways you might extend this project:

* Sort the medical records alphabetically by name. You’ll have to create a new list using <code>zip()</code> to do this.
* Select the medical records starting at index 3 and ending at index 7 and save it in a variable called <code>middle_five_records</code>.
 
Happy coding!