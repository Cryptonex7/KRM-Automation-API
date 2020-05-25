#! Company Wise Analysis
import pandas as pd
import services.student as st

company = st.stu_data[st.stu_data['company'] == 'Accenture']

# ? Profile Offered and Students hired in Each Profile
company_profile = company.groupby(
    'profile')['placed'].sum().sort_values(ascending=False)
values = []
for row in company_profile:
    values.append(row)
profiles = company[company['company'] == 'Accenture']['profile'].unique()

comp_profile_pie = {
    'values': values,
    'labels': profiles.tolist(),
    'type': 'pie',
    'title': 'Travel history analysis'
}

# ? CGPA of Students Placed
cgpa_grouped = company.groupby('CGPA')['placed'].sum().reset_index()
cgpa_grouped['CGPA'] = cgpa_grouped['CGPA'].astype('object')
cgpa_grouped_soted = cgpa_grouped.sort_values(by='placed', ascending=True)
comp_cgpa_hbar = {
    'x': pd.Series(cgpa_grouped_soted['placed']).tolist(),
    'y': pd.Series(cgpa_grouped_soted['CGPA']).tolist(),
    'type': 'bar',
    'orientation': 'h',
    'title': 'CGPA of Students placed',
    'x_label': 'Hired Number of Students',
    'y_label': 'CGPA of Hired Students'
}

# ? Branch of Students Placed
branch_grouped = company.groupby('Branch')['placed'].sum().reset_index()
comp_branch_pie = {
    'values': pd.Series(branch_grouped['placed']).tolist(),
    'labels': pd.Series(branch_grouped['Branch']).tolist(),
    'type': 'pie',
    'title': 'Travel history analysis'
}

# ? Gender of Students Placed
gender_grouped = company.groupby('Gender')['placed'].sum().reset_index()
comp_gender_pie = {
    'values': pd.Series(gender_grouped['placed']).tolist(),
    'labels': pd.Series(gender_grouped['Gender']).tolist(),
    'type': 'pie',
    'title': 'Travel history analysis'
}
