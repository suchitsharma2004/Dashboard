# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objs as go

# # Set page configuration
# st.set_page_config(page_title="Dashboard", page_icon="🏢", layout="wide")

# # Load data (replace with your data loading method)
# file_path = r'/Users/suchitsharma/Documents/GitHub/Dashboard/Project-2024-07-16.xlsx'
# df = pd.read_excel(file_path)

# # Sidebar filters
# st.sidebar.title('Filters')
# filter_active_inactive = st.sidebar.selectbox('Active/Inactive', ['All', 'Active', 'Inactive'])
# filter_director = st.sidebar.selectbox('Project Director', ['All'] + df['project_director'].unique().tolist())
# filter_hod = st.sidebar.selectbox('Project HOD', ['All'] + df['project_hod'].unique().tolist())
# filter_manager = st.sidebar.selectbox('Project Manager', ['All'] + df['project_manager'].unique().tolist())
# filter_lead = st.sidebar.selectbox('Team Lead', ['All'] + df['project_teamlead'].unique().tolist())

# # Filter data based on selected filters
# filtered_data = df.copy()

# if filter_active_inactive != 'All':
#     filtered_data = filtered_data[filtered_data['is_active'] == (1 if filter_active_inactive == 'Active' else 0)]

# if filter_director != 'All':
#     filtered_data = filtered_data[filtered_data['project_director'] == filter_director]

# if filter_hod != 'All':
#     filtered_data = filtered_data[filtered_data['project_hod'] == filter_hod]

# if filter_manager != 'All':
#     filtered_data = filtered_data[filtered_data['project_manager'] == filter_manager]

# if filter_lead != 'All':
#     filtered_data = filtered_data[filtered_data['project_teamlead'] == filter_lead]

# # Main content
# # st.title("Project Status Overview")

# # Metrics boxes
# statuses = ['completed', 'onhold', 'inprogress', 'to_be_started']

# # Calculate number of projects in each status
# num_projects = {
#     status.replace('_', ' ').title(): filtered_data[filtered_data['status'] == status].shape[0]
#     for status in statuses
# }

# # Display metrics in boxes
# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     st.metric(label='Completed', value=num_projects['Completed'])
# with col2:
#     st.metric(label='Onhold', value=num_projects['Onhold'])
# with col3:
#     st.metric(label='Inprogress', value=num_projects['Inprogress'])
# with col4:
#     st.metric(label='to_be_started', value=num_projects['To Be Started'])

# # Rightmost column for additional analytics
# # st.header("Additional Analytics")
# col5, col6 = st.columns([3,1])

# # Pie chart for project status distribution
# status_counts = filtered_data['status'].value_counts().reset_index()
# status_counts.columns = ['status', 'count']
# fig_pie = px.pie(status_counts, values='count', names='status', title='Project Status Distribution', hole=0.4)
# # st.plotly_chart(fig_pie, use_container_width=True, width=350, height=350)  # Adjust width and height as needed
# col6.plotly_chart(fig_pie, use_container_width=True)

# # Horizontal bar graph for completed percentage of projects in progress
# in_progress_data = filtered_data[filtered_data['status'] == 'inprogress'].copy()
# in_progress_data['completed_percent'] = (in_progress_data['total_achievement'] / in_progress_data['sample']) * 100

# fig_completed_percent = px.bar(in_progress_data.sort_values(by='completed_percent'), 
#                                x='completed_percent', y='name', 
#                                orientation='h', 
#                                title='Completed Percentage of Projects in Progress',
#                                labels={'completed_percent': 'Completed %', 'name': 'Project ID'},
#                                color='completed_percent',
#                                color_continuous_scale='viridis')

# # st.plotly_chart(fig_completed_percent, use_container_width=True, width=350, height=400)  # Adjust width and height as needed
# col5.plotly_chart(fig_completed_percent, use_container_width=True)
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Dashboard", page_icon="🏢", layout="wide")

# Load data (replace with your data loading method)
file_path = r'/Users/suchitsharma/Documents/GitHub/Dashboard/Project-2024-07-16.xlsx'
df = pd.read_excel(file_path)
df['estimated_time'] = pd.to_timedelta(df['estimated_time'])
df['remaining_time'] = pd.to_timedelta(df['remaining_time'])
# Convert estimated_time and remaining_time to numeric
# df['estimated_time'] = pd.to_numeric(df['estimated_time'], errors='coerce')
# df['remaining_time'] = pd.to_numeric(df['remaining_time'], errors='coerce')

# Sidebar filters
st.sidebar.title('Filters')
filter_active_inactive = st.sidebar.selectbox('Active/Inactive', ['All', 'Active', 'Inactive'])
filter_director = st.sidebar.selectbox('Project Director', ['All'] + df['project_director'].unique().tolist())
filter_hod = st.sidebar.selectbox('Project HOD', ['All'] + df['project_hod'].unique().tolist())
filter_manager = st.sidebar.selectbox('Project Manager', ['All'] + df['project_manager'].unique().tolist())
filter_lead = st.sidebar.selectbox('Team Lead', ['All'] + df['project_teamlead'].unique().tolist())
lagging_filter = st.sidebar.checkbox('Show lagging projects')

# Filter data based on selected filters
filtered_data = df.copy()

if filter_active_inactive != 'All':
    filtered_data = filtered_data[filtered_data['is_active'] == (1 if filter_active_inactive == 'Active' else 0)]

if filter_director != 'All':
    filtered_data = filtered_data[filtered_data['project_director'] == filter_director]

if filter_hod != 'All':
    filtered_data = filtered_data[filtered_data['project_hod'] == filter_hod]

if filter_manager != 'All':
    filtered_data = filtered_data[filtered_data['project_manager'] == filter_manager]

if filter_lead != 'All':
    filtered_data = filtered_data[filtered_data['project_teamlead'] == filter_lead]

# Metrics boxes
statuses = ['completed', 'onhold', 'inprogress', 'to_be_started']

# Calculate number of projects in each status
num_projects = {
    status.replace('_', ' ').title(): filtered_data[filtered_data['status'] == status].shape[0]
    for status in statuses
}

# Display metrics in boxes
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label='Completed', value=num_projects['Completed'])
with col2:
    st.metric(label='Onhold', value=num_projects['Onhold'])
with col3:
    st.metric(label='Inprogress', value=num_projects['Inprogress'])
with col4:
    st.metric(label='To Be Started', value=num_projects['To Be Started'])

# Rightmost column for additional analytics
col5, col6 = st.columns([3, 1])

# Pie chart for project status distribution
status_counts = filtered_data['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']
fig_pie = px.pie(status_counts, values='count', names='status', title='Project Status Distribution', hole=0.4)
col6.plotly_chart(fig_pie, use_container_width=True)

# Filter for projects nearing deadline but lagging behind if checkbox is checked
if lagging_filter:
    filtered_data['elapsed_time'] = filtered_data['estimated_time'] - filtered_data['remaining_time']
    filtered_data['time_ratio'] = filtered_data['elapsed_time'] / filtered_data['estimated_time']
    filtered_data['completion_ratio'] = filtered_data['total_achievement'] / filtered_data['sample']

    lagging_projects = filtered_data[(filtered_data['status'] == 'inprogress') & 
                                     (filtered_data['completion_ratio'] < 0.6) & 
                                     (filtered_data['time_ratio'] > 0.6)]
    lagging_projects['completed_percent'] = lagging_projects['completion_ratio'] * 100

    fig_lagging_projects = px.bar(lagging_projects.sort_values(by='completed_percent'), 
                                  x='completed_percent', y='name', 
                                  orientation='h', 
                                  title='Lagging Projects (80% time, <80% completed)',
                                  labels={'completed_percent': 'Completed %', 'name': 'Project ID'},
                                  color='completed_percent',
                                  color_continuous_scale='viridis')

    col5.plotly_chart(fig_lagging_projects, use_container_width=True)
else:
    # Horizontal bar graph for completed percentage of projects in progress
    in_progress_data = filtered_data[filtered_data['status'] == 'inprogress'].copy()
    in_progress_data['completed_percent'] = (in_progress_data['total_achievement'] / in_progress_data['sample']) * 100

    fig_completed_percent = px.bar(in_progress_data.sort_values(by='completed_percent'), 
                                   x='completed_percent', y='name', 
                                   orientation='h', 
                                   title='Completed Percentage of Projects in Progress',
                                   labels={'completed_percent': 'Completed %', 'name': 'Project ID'},
                                   color='completed_percent',
                                   color_continuous_scale='viridis')

    col5.plotly_chart(fig_completed_percent, use_container_width=True)
