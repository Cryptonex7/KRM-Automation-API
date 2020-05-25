import pandas as pd

stu_data = pd.read_csv('./data/StudentDatabase.csv')
comp_data = pd.read_csv('./data/company_schema.csv')

# & Student Anaylsis
# ? Students Placed Year Wise
year_wise = pd.DataFrame({
    'year': [2015, 2016, 2017, 2018, 2019],
    'students': [comp_data['hired_15'].sum(), comp_data['hired_16'].sum(), comp_data['hired_17'].sum(), comp_data['hired_18'].sum(), comp_data['hired_19'].sum()]
})

stud_hired_per_year_bar = {
    'x': pd.Series(year_wise['year']).tolist(),
    'y': pd.Series(year_wise['students']).tolist(),
    'type': 'bar',
    'title': 'Students Hired per Year',
    'x_label': 'Year',
    'y_label': 'Students'
}
stud_hired_per_year_pie = {
    'values': pd.Series(year_wise['students']).tolist(),
    'labels': pd.Series(year_wise['year']).tolist(),
    'type': 'pie',
    'title': 'Travel history analysis'
}

# ? Gender Distribution of Student Placed
stud_gender_pie = {
    'values': pd.Series(stu_data['Gender']).tolist(),
    'type': 'pie',
    'title': 'Travel history analysis'
}

# ? Branch Distribution of Student Placed
stud_branch_pie = {
    'values': pd.Series(stu_data['Branch']).tolist(),
    'type': 'pie',
    'title': 'Travel history analysis'
}

# ? Package Grabbed in a Given Year
stu_data['placed'] = 1
ctc_grouped = stu_data.groupby('CTC')['placed'].sum().reset_index()
ctc_grouped_sorted = ctc_grouped.sort_values(by='placed', ascending=False)
# horizontal bar-graph
stud_package_hbar = {
    'x': pd.Series(ctc_grouped_sorted['placed']).tolist(),
    'y': pd.Series(ctc_grouped_sorted['CTC']).tolist(),
    'orientation': 'h',
    'type': 'bar',
    'title': 'Package of Placed Students',
    'x_label': 'Placed Students',
    'y_label': 'CTC'
}

# ? CGPA Corelation with CTC
cgpa = [5, 6, 7, 8, 9, 10]
avg_ctc = [
    stu_data[stu_data['CGPA'] == 5]['CTC'].mean(),
    stu_data[stu_data['CGPA'] == 6]['CTC'].mean(),
    stu_data[stu_data['CGPA'] == 7]['CTC'].mean(),
    stu_data[stu_data['CGPA'] == 8]['CTC'].mean(),
    stu_data[stu_data['CGPA'] == 9]['CTC'].mean(),
    stu_data[stu_data['CGPA'] == 10]['CTC'].mean()
]

stud_cgpa_line = {
    'x': cgpa,
    'y': avg_ctc,
    'type': 'line',
    'title': 'CGPA Corelation with CTC',
    'x_label': 'CGPA',
    'y_label': 'CTC'
}

# ? Profile offered by Recruiters
profile_grouped = stu_data.groupby('profile')['placed'].sum().reset_index()
profile_grouped_sorted = profile_grouped.sort_values(
    by='placed', ascending=True
)
# horizontal bar-graph
stud_profile_hbar = {
    'x': pd.Series(profile_grouped_sorted['placed']).tolist(),
    'y': pd.Series(profile_grouped_sorted['profile']).tolist(),
    'orientation': 'h',
    'type': 'bar',
    'title': 'Profile of Placed Students',
    'x_label': 'Placed Students',
    'y_label': 'Profile'
}
