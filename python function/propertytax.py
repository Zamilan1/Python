# create a list of properties
property_list = {

"value_of_property = 0.60"
"land = 10000"
"assessment = 6000"
"tax = 72"
"assessment_value = 100"
"accre_assess = 43.20"
}

def calculate_property_value(value_property):
    

    property_list_updated = {k: v*value_property for k, v in property_list.items()}
    
    # calculate the assessment value
    assessment_value = sum(property_list_updated.values())
    
    # calculate the property tax
    tax = 0.60 * assessment_value
    
    return assessment_value, tax

# ask for the actual value of piece of property
value_property = float(input("Enter value of piece of property: "))

# calculate the assessment value and property tax
assessment_value, tax = calculate_property_value(value_property)

# display the results
print(f"The assessment value of the property is {assessment_value}")
print(f"The property tax is {tax}")