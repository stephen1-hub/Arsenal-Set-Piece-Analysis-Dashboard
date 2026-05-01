import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(layout="wide")
st.title("Arsenal Corner Analysis Dashboard")

# -------------------------
# LOAD DATA
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("corners_data.csv")  # save your dataframe first
    return df

df = load_data()

if 'zone' not in df.columns:
    def get_zone(x, y):
        if x > 108:
            if y < 26:
                return "Near Post"
            elif y > 54:
                return "Far Post"
            else:
                return "Central"
        return "Edge/Outside"

    df['zone'] = df.apply(lambda row: get_zone(row['X'], row['Y']), axis=1)

df['X'] = pd.to_numeric(df['X'], errors='coerce')
df['Y'] = pd.to_numeric(df['Y'], errors='coerce')

# If values are small → scale them
if df['X'].max() <= 1:
    df['X'] = df['X'] * 120
    df['Y'] = df['Y'] * 80

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.header("Filters")

players = st.sidebar.multiselect(
    "Select Players",
    options=df['player'].unique(),
    default=df['player'].value_counts().head(5).index
)

df['X'] = pd.to_numeric(df['X'], errors='coerce')
df['Y'] = pd.to_numeric(df['Y'], errors='coerce')

# Scale if needed
if df['X'].max() <= 1:
    df['X'] = df['X'] * 120
    df['Y'] = df['Y'] * 80

def get_zone(x, y):
    if x > 108:
        if y < 26:
            return "Near Post"
        elif y > 54:
            return "Far Post"
        else:
            return "Central"
    return "Edge/Outside"

df['zone'] = df.apply(lambda row: get_zone(row['X'], row['Y']), axis=1)

st.write(df[['X', 'Y', 'zone']].head())
st.write(df['zone'].value_counts())

zones = st.sidebar.multiselect(
    "Select Zones",
    options=df['zone'].unique(),
    default=df['zone'].unique()
)

# Filter data
filtered_df = df[
    (df['player'].isin(players)) &
    (df['zone'].isin(zones))
]

# -------------------------
# METRICS
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Shots", len(filtered_df))
col2.metric("Total xG", round(filtered_df['xG'].sum(), 2))
col3.metric("Avg xG", round(filtered_df['xG'].mean(), 3))

# -------------------------
# PITCH MAP
# -------------------------
st.subheader("Shot Map")

pitch = Pitch(
    pitch_type='statsbomb',
    pitch_color='#0e1117',
    line_color='white'
)

fig, ax = pitch.draw(figsize=(10, 7))

# Draw zones
ax.add_patch(plt.Rectangle((108, 0), 12, 26, fill=False, edgecolor='yellow', linewidth=2))
ax.add_patch(plt.Rectangle((108, 26), 12, 28, fill=False, edgecolor='red', linewidth=2))
ax.add_patch(plt.Rectangle((108, 54), 12, 26, fill=False, edgecolor='blue', linewidth=2))

# Plot shots
for player in filtered_df['player'].unique():
    player_data = filtered_df[filtered_df['player'] == player]
    
    pitch.scatter(
        player_data['X'],
        player_data['Y'],
        s=player_data['xG'] * 1000,
        label=player,
        ax=ax,
        edgecolors='white',
        alpha=0.9
    )

# Title
ax.set_title("Corner Shot Map | Size = xG", color='white')

# Legend
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))

st.pyplot(fig)

# -------------------------
# BAR CHART - ZONES
# -------------------------
st.subheader("Shots by Zone")

zone_counts = filtered_df['zone'].value_counts()

fig2, ax2 = plt.subplots()
zone_counts.plot(kind='bar', ax=ax2)
ax2.set_title("Shot Distribution by Zone")

st.pyplot(fig2)

# -------------------------
# PLAYER ANALYSIS
# -------------------------
st.subheader("Top Players")

player_counts = filtered_df['player'].value_counts()

st.dataframe(player_counts)