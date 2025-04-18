import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='Analysis section')
st.title('Mumbai Flats Analytics')
st.warning("Prices are in Cr")

st.subheader(':green[Average Price Across Mumbai]')
data = pd.read_csv('data//location.csv')
fig = px.scatter_mapbox(data,lat='latitude',lon='longitude',size='flat_price',
                         color='flat_price', hover_name='location',zoom=8.5,
                         mapbox_style="open-street-map",color_continuous_scale='plotly3')
st.plotly_chart(fig,use_container_width=True)

df = pd.read_csv('data//data_for_model.csv')[['flat_type','flat_price','location1',
                                                 'buildupArea_sqft','bedrooms','bathrooms']]
st.divider()

st.subheader("Summary of Key Insights")
# Basic calculations
avg_flat_price = df['flat_price'].mean()
median_area = df['buildupArea_sqft'].median()
most_common_bedrooms = df['bedrooms'].mode()[0]

# Calculate top location by price
location_price = df.groupby('location1')['flat_price'].mean().sort_values(ascending=False)
top_location = location_price.index[0]



# ---------------------------
# Display Insights in Streamlit
# ---------------------------
st.title("Summary of Key Insights")

# Display metrics as cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Flats", value=f"{df.shape[0]}")
with col2:
    st.metric(label="Average Flat Price", value=f"₹{avg_flat_price:,.2f}")
with col3:
    st.metric(label="Median Buildup Area", value=f"{median_area} sqft")

# Display other insights
st.subheader("Additional Insights")
st.write(f"**Most Common Bedroom Count:** {most_common_bedrooms}")
st.write(f"**Top Location by Price:** {top_location}")

st.subheader("Top 10 Locations by Average Price per Sq Ft")
# Calculate price per square foot
df['price_per_sqft'] = df['flat_price'] / df['buildupArea_sqft']

# Group by location and sort the top 10
avg_price_location = df.groupby('location1')['price_per_sqft'].mean().sort_values(ascending=False).head(10)



# Plot using Matplotlib + Seaborn
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=avg_price_location.index, y=avg_price_location.values, palette='viridis', ax=ax)
ax.set_title('Top 10 Locations by Average Price per Sq Ft', fontsize=16)
ax.set_xlabel('Location', fontsize=12)
ax.set_ylabel('Average Price per Sq Ft', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Display the plot in Streamlit
st.pyplot(fig)
st.divider()




st.subheader("Top 10 Locations with Most Flats")


# Calculate flats count by location
top_locations = df['location1'].value_counts().head(10)

# Plot using Matplotlib + Seaborn
fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(x=top_locations.index, y=top_locations.values, palette='viridis', ax=ax)
ax.set_title('Top 10 Locations with Most Flats', fontsize=16)
ax.set_xlabel('Location', fontsize=12)
ax.set_ylabel('Number of Flats', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Display the plot in Streamlit
st.pyplot(fig)

st.divider()
st.subheader(":green[Relation Between Builup Area and Price]")
fig3 = px.scatter(data_frame=df,x='buildupArea_sqft',y='flat_price',color='bedrooms',
                  color_continuous_scale='plotly3')
st.plotly_chart(fig3,use_container_width=True)
st.divider()


st.subheader(":green[BHK Pie Chart]")
locations1 = df['location1'].unique().tolist()
locations1.insert(0,'Overall')
selected_location1 = st.selectbox("Select Location1",locations1)
if selected_location1 == 'Overall':
    fig3 = px.pie(data_frame=df,names='bedrooms')
    st.plotly_chart(fig3,use_container_width=True)
else:
    d1 = df[df['location1'] == selected_location1]   
    fig4 = px.pie(data_frame=d1,names='bedrooms') 
    st.plotly_chart(fig4,use_container_width=True)
st.divider()


st.subheader(":green[Histplot of price]")
fig5 = plt.figure(figsize=(10, 6))
sns.histplot(df['flat_price'],kde=True)
st.pyplot(fig5,use_container_width=True)


# Pie chart for top locations share
st.write("### Top Locations Share")
top_locations = df['location1'].value_counts().head(10)  # Get the top 5 locations
fig, ax = plt.subplots()
ax.pie(top_locations, labels=top_locations.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3', len(top_locations)))
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
ax.set_title('Top 10 Locations Share')
st.pyplot(fig)




